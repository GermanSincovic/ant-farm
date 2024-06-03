import pygame


class Food:
    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.size = None
        self.value = None

    def redraw(self):
        pygame.draw.circle(pygame.display.get_surface(), (0, 255, 0), (self.position_x, self.position_y), self.size, 1)
