import pygame
import os

class Window():
    def __init__(self):
        self.width = 0
        self.height = 0
        self.resizable = False


    def mk_win(self, width, height, caption='NOVA', resizable=False):
        self.width = width
        self.height = height
        self.resizable = resizable
        if self.resizable is False:
            self.win = pygame.display.set_mode((self.width, self.height), vsync=1)
            
        else:
            self.win = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE, vsync=1)

        pygame.display.set_caption(caption)

        return self.win

    def set_pos(self, posx, posy, centered=False):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (posx, posy)

        if centered is True:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        else:
            os.environ['SDL_VIDEO_CENTERED'] = '0'

    def clear(self, clr):
        self.win.fill(clr)

    def update(self):
        pygame.display.update()

        
