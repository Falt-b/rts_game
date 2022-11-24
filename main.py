import pygame
import iso_grid
from sys import exit

WIDTH = 1280
HEIGHT = 880
FPS = 60
BG_COLOR = (20, 20, 20)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("rts_game")
    clock = pygame.time.Clock()

    test_grid = iso_grid.Iso_Grid((64, 64), (640 - 32, 160 - 32))
    iso_grid.generate_grid(20, 20, test_grid, "test_tile.png", 2)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        display.fill(BG_COLOR)

        test_grid.draw_grid(display)
        # test_grid.draw(display)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    exit()
