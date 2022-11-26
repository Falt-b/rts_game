import pygame


class Mouse_Handler:
    def __init__(self) -> None:
        self.inputs = [False, False, False]
        self.drag = False
        self.initial_position = pygame.Vector2()

    def get_pressed(self):
        self.inputs = pygame.mouse.get_pressed()

    def get_released(self):
        self.inputs = pygame.mouse.get_pressed()

    def click_drag(self):
        if not self.inputs[0]:
            self.drag = False
            return pygame.Vector2()
        if self.inputs[0] and not self.drag:
            self.initial_position = pygame.Vector2(pygame.mouse.get_pos())
            self.drag = True
            return pygame.Vector2()
        if self.drag:
            self.drag = False
            return pygame.Vector2(pygame.mouse.get_pos()) - self.initial_position
