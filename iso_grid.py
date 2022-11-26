import pygame
from math import floor, ceil
from image_loading import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, position: tuple, image: pygame.Surface, *groups) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.offset = pygame.Vector2()


class Iso_Grid(pygame.sprite.Group):
    def __init__(
        self,
        grid_width: int,
        grid_height: int,
        tile_width: int,
        tile_height: int,
        x_offset: float,
        y_offset: float,
        center_x: float,
        center_y: float,
        *sprites
    ) -> None:
        super().__init__(*sprites)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.hgrid_width = grid_width * 0.5
        self.hgrid_height = grid_height * 0.5
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.htile_width = tile_width * 0.5
        self.qtile_height = tile_height * 0.25
        self.offset = pygame.Vector2((x_offset, y_offset))
        self.center = (center_x, center_y)

    def generate_grid(self, image: str, scale: int = 1, colorkey: tuple = (0, 0, 0)):
        img = load_image(image, scale, colorkey)
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                Tile((x, y), img, self)

    def screen_to_grid(self, position: pygame.Vector2):
        set_position = (
            position
            + pygame.Vector2(0, self.qtile_height * 0.5)
            + (pygame.Vector2(self.center) - self.offset)
        )
        grid_x = set_position.x / self.htile_width
        grid_y = set_position.y / self.qtile_height
        return pygame.Vector2(
            floor((grid_x + grid_y) * 0.5) - 10,
            floor((-grid_x + grid_y) * 0.5) + 10,
        )

    def grid_to_screen(self, tile: Tile):
        return pygame.Vector2(
            ((tile.rect.topleft[0] - tile.rect.topleft[1]) * self.htile_width)
            - self.htile_width,
            (tile.rect.topleft[0] + tile.rect.topleft[1]) * self.qtile_height,
        )

    def draw_grid(self, surface: pygame.Surface):
        for tile in self.sprites():
            surface.blit(
                tile.image, self.grid_to_screen(tile) + self.offset + tile.offset
            )
