import pygame
import chess

SQUARE_SIZE = 80
colors = [(238, 238, 210), (118, 150, 86)]
PIECES = {}

def load_images():
    pieces = ["wp", "bp", "wr", "br", "wn", "bn", "wb", "bb", "wq", "bq", "wk", "bk"]
    for piece in pieces:
        PIECES[piece] = pygame.transform.scale(
            pygame.image.load(f"assets/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))

class Board:
    def __init__(self, screen):
        self.screen = screen
        load_images()

    def draw_board(self):
        for r in range(8):
            for c in range(8):
                color = colors[(r + c) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, board):
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                row = 7 - (square // 8)
                col = square % 8
                piece_str = piece.color and "w" or "b"
                piece_str += piece.symbol().lower()
                self.screen.blit(PIECES[piece_str], pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_valid_moves(self, board, selected_square):
        for move in board.legal_moves:
            if move.from_square == selected_square:
                to = move.to_square
                row = 7 - (to // 8)
                col = to % 8
                pygame.draw.circle(self.screen, (0, 0, 0), (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 10)