import pygame
import grid
from sys import exit

WIDTH = 640
HEIGHT = 640
FPS = 60
BG_COLOR = (20, 20, 20)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("rts_game")
    clock = pygame.time.Clock()

    test_grid = grid.Grid(64, 64, 320 - 32, 160 - 32)
    grid.generate_grid(10, 10, "grid_tile.png", (0, 0, 0), test_grid)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        display.fill(BG_COLOR)

        test_grid.custom_draw(display)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    exit()
