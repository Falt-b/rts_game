import pygame
import numpy as np
from image_loading import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(
        self, position: tuple, image: pygame.Surface, color_key: tuple, *groups
    ) -> None:
        super().__init__(*groups)
        self.image = image.convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect(topleft=position)


class Grid(pygame.sprite.Group):
    def __init__(
        self, tile_width: int, tile_height: int, offset_x: int, offset_y: int, *sprites
    ) -> None:
        super().__init__(*sprites)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.transformation_matrix = np.array(
            (
                (0.5 * tile_width, 0.25 * tile_height),
                (-0.5 * tile_width, 0.25 * tile_height),
            )
        )

    def custom_draw(self, surface):
        for tile in self.sprites():
            grid_position = np.matmul(tile.rect.topleft, self.transformation_matrix)
            surface.blit(
                tile.image,
                (grid_position[0] + self.offset_x, grid_position[1] + self.offset_y),
            )


def generate_grid(width: int, height: int, image: str, color_key: tuple, group: Grid):
    tile_image = load_image(
        image,
        2,
        (0, 0, 0),
    )
    for y in range(height):
        for x in range(width):
            Tile(
                (x, y),
                tile_image,
                color_key,
                group,
            )
