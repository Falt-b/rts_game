import pygame


class tile(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)


class Grid(pygame.sprite.Group):
    def __init__(self, *sprites: Union[Sprite, Sequence[Sprite]]) -> None:
        super().__init__(*sprites)
