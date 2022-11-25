import pygame
from math import floor, ceil
from image_loading import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, position: tuple, image: pygame.Surface, *groups) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.offset = pygame.Vector2(0, 0)


class Iso_Grid(pygame.sprite.Group):
    def __init__(self, tile_size: tuple, grid_offset: tuple, *sprites) -> None:
        super().__init__(*sprites)
        self.tile_size = tile_size
        self.half_width = tile_size[0] / 2
        self.quarter_height = tile_size[1] / 4
        self.offset = pygame.Vector2(grid_offset)

    def screen_to_grid(self, position: pygame.Vector2):
        x = floor(
            0.5 * (position.x / self.half_width + position.y / self.quarter_height)
        )
        y = floor(
            0.5 * (-position.x / self.half_width + position.y / self.quarter_height)
        )
        return pygame.Vector2(x - 10, y + 10)

    def grid_to_screen(self, tile: Tile):
        return pygame.Vector2(
            (tile.rect.topleft[0] - tile.rect.topleft[1]) * self.half_width
            - self.half_width,
            (tile.rect.topleft[0] + tile.rect.topleft[1]) * self.quarter_height,
        )

    def slect_tile(self, index: int):
        for sprite in self.sprites():
            sprite.offset.y = 0
        self.sprites()[index].offset.y = -10

    def draw_grid(self, surface: pygame.Surface):
        for tile in self.sprites():
            surface.blit(
                tile.image, self.grid_to_screen(tile) + self.offset + tile.offset
            )


def generate_grid(
    width: int,
    height: int,
    group: Iso_Grid,
    image: str,
    scale: int = 1,
    colorkey: tuple = (0, 0, 0),
):
    img = load_image(image, scale, colorkey)
    for y in range(height):
        for x in range(width):
            Tile((x, y), img, group)
