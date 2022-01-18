import pygame

class Grid():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sizebtwn = 0

    def draw(self, w, rows, surface, color):
        self.sizebtwn = w // rows  # Distance between Lines
        self.x = 0
        self.y = 0
        for i in range(rows):
            self.x = self.x + self.sizebtwn
            self.y = self.y + self.sizebtwn
            pygame.draw.line(surface, color, (self.x, 0), (self.x, w))
            pygame.draw.line(surface, color, (0, self.y), (w, self.y))

        return self.sizebtwn

    def check_mouse(self, mouse):
        gx, gy = mouse[0][0] // self.sizebtwn, mouse[0][1] // self.sizebtwn

        cx, cy = gx * self.sizebtwn, gy * self.sizebtwn

        return cx, cy
