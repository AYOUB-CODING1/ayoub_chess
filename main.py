import pygame
import sys
import chess
import chess.engine
import game_logic
import board

pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayoub Chess")
clock = pygame.time.Clock()
game_board = board.Board(screen)
game = game_logic.Game(game_board, screen)  
font = pygame.font.SysFont(None, 40)

def show_text(text):
    overlay = pygame.Surface((WIDTH, 80))
    overlay.fill((20, 20, 20))
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(overlay, (0, HEIGHT // 2 - 40))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - 20))

running = True
while running:
    screen.fill((255, 255, 255))
    game_board.draw_board()
    game_board.draw_pieces(game.board)
    if game.selected:
        game_board.draw_valid_moves(game.board, game.selected)
    game.update()

    if game.result:
        show_text(game.result)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.result:
                game.handle_click(pygame.mouse.get_pos())

    clock.tick(60)

pygame.quit()
sys.exit()
