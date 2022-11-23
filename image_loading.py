import pygame


def load_image(file_name: str, scale: int = 1, clolor_key: tuple = (0, 0, 0)):
    image = pygame.image.load(file_name).convert()
    image.set_colorkey(clolor_key)
    width, height = (image.get_width(), image.get_height())
    return pygame.transform.scale(image, (width * scale, height * scale))
