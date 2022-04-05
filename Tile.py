import pygame

class tile:
    def __init__(self, x, y, window, size):
        self.x = x
        self.y = y
        self.window = window
        self.type = 0
        self.size = size
        self.offset_x = 0
        self.offset_y = 0
        self.colors = {
            0: (28, 28, 28),
            1: (255, 230, 0),
            2: (43, 255, 234),
            3: (255, 0, 0)
        }

    def draw(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        if self.x * self.size + offset_x < 0 - self.size or self.y * self.size + offset_y < 0 - self.size or self.x * self.size + offset_x > \
                self.window.get_size()[0] + 5 or self.y * self.size + offset_y > self.window.get_size()[1] + 5:
            pass
        else:
            pygame.draw.rect(self.window, self.colors[self.type],
                             pygame.Rect((self.x * self.size + offset_x, self.y * self.size + offset_y),
                                         (self.size - 1, self.size - 1)))
