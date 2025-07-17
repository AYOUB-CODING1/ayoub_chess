import chess
import pygame
import board as board_module

pygame.mixer.init()
move_sound = pygame.mixer.Sound("sounds/move.wav")
check_sound = pygame.mixer.Sound("sounds/check.wav")
checkmate_sound = pygame.mixer.Sound("sounds/checkmate.wav")

def ask_promotion(screen, color):
    pygame.font.init()
    piece_options = ['q', 'r', 'n', 'b']
    selected = None
    piece_images = []
    for p in piece_options:
        key = ('w' if color == chess.WHITE else 'b') + p
        img = board_module.PIECES[key]
        piece_images.append(img)

    window = pygame.Surface((320, 100))
    window.fill((220, 220, 220))

    while selected is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in range(4):
                    x = 160 + i * 80
                    if x <= mx <= x + 80 and 270 <= my <= 350:
                        selected = piece_options[i]

        screen.blit(window, (160, 270))
        for i, img in enumerate(piece_images):
            screen.blit(img, (160 + i * 80, 270))
        pygame.display.flip()

    return {'q': chess.QUEEN, 'r': chess.ROOK, 'n': chess.KNIGHT, 'b': chess.BISHOP}[selected]

class Game:
    def __init__(self, board_view, screen):
        self.board_view = board_view
        self.screen = screen
        self.board = chess.Board()
        self.selected = None
        self.result = None

    def handle_click(self, pos):
        col = pos[0] // 80
        row = 7 - (pos[1] // 80)
        square = chess.square(col, row)

        if self.selected is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected = square
        else:
            piece = self.board.piece_at(self.selected)
            is_pawn = piece and piece.piece_type == chess.PAWN
            is_promotion_row = (square // 8 == 7 and piece.color == chess.WHITE) or (square // 8 == 0 and piece.color == chess.BLACK)

            if is_pawn and is_promotion_row:
                promotion_piece = ask_promotion(self.screen, piece.color)
                move = chess.Move(self.selected, square, promotion=promotion_piece)
            else:
                move = chess.Move(self.selected, square)

            if move in self.board.legal_moves:
                self.board.push(move)
                move_sound.play()
                if self.board.is_check():
                    if self.board.is_checkmate():
                        checkmate_sound.play()
                        self.result = "Checkmate!"
                    else:
                        check_sound.play()
            self.selected = None

    def update(self):
        if self.board.is_stalemate():
            self.result = "Draw by stalemate"
        elif self.board.is_insufficient_material():
            self.result = "Draw (insufficient material)"
