import pygame
import iso_grid
import input_handler
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

    center = pygame.Vector2(WIDTH / 2, 0)

    test_grid = iso_grid.Iso_Grid(20, 20, 64, 64, center[0], 0, center[0], 0)
    test_grid.generate_grid("images/test_tile.png", 2)

    mouse = input_handler.Mouse_Handler()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse.get_released()

        display.fill(BG_COLOR)

        cords = test_grid.screen_to_grid(pygame.Vector2(pygame.mouse.get_pos()))
        tile_index = int(cords[0] + cords[1] * 20)
        if tile_index > 399:
            tile_index = 399

        test_grid.offset += mouse.click_drag()

        test_grid.sprites()[tile_index].offset.y = -10

        test_grid.draw_grid(display)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    exit()
