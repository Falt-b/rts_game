import pygame
import iso_grid
from sys import exit

WIDTH = 1280
HEIGHT = 880
FPS = 10
BG_COLOR = (20, 20, 20)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("rts_game")
    clock = pygame.time.Clock()

    center = pygame.Vector2(WIDTH / 2, 0)

    test_grid = iso_grid.Iso_Grid((64, 64), center)
    iso_grid.generate_grid(20, 20, test_grid, "images/test_tile.png", 2)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        display.fill(BG_COLOR)

        cords = test_grid.screen_to_grid(pygame.Vector2(pygame.mouse.get_pos()))
        tile_index = int(cords.x + cords.y * 20)
        if tile_index > 399:
            tile_index = 399
        test_grid.slect_tile(tile_index)

        test_grid.draw_grid(display)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    exit()
