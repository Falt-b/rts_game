import pygame
import numpy as np
from image_loading import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, position: tuple, image: pygame.Surface, *groups) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)


class Iso_Grid(pygame.sprite.Group):
    def __init__(self, tile_size: tuple, grid_offset: tuple, *sprites) -> None:
        super().__init__(*sprites)
        self.tile_size = tile_size
        self.offset = pygame.Vector2(grid_offset)
        self.iso_matrix = np.array(((0.5, 0.25), (-0.5, 0.25)))

    def draw_grid(self, surface: pygame.Surface):
        for tile in self.sprites():
            grid_pos = np.matmul(tile.rect.topleft, self.iso_matrix)
            surface.blit(
                tile.image, (grid_pos[0] + self.offset[0], grid_pos[1] + self.offset[1])
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
    img_width = img.get_width()
    img_height = img.get_height()
    for y in range(height):
        for x in range(width):
            Tile((x * img_width, y * img_height), img, group)
