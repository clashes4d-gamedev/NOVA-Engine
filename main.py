from pygame import mouse
import lib
import pygame
import sys
import time


class Main():
    def __init__(self) -> None:
        self.width = 1280
        self.height = 720
        self.win = lib.window.mk_win(self.width, self.height, resizable=True)
        lib.window.set_pos(100, 100, centered=True)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.menu_btn = 'res/pl_btn_img.png'
        self.zoom = 2
        self.cx = 0
        self.cy = 0
        self.g_cell = 0
        self.properties_width = self.width//4.5
        # objects = {object: {properties{desc: 'deofdfasfd', collider: rect}, scripts:{script1: 'path to script'}}}
        self.objects = {}


    def update(self):
        last_time = time.time()
        while True:
            delta_time = time.time() - last_time
            lib.window.clear((0, 0, 0))
            mouse = lib.ui.get_mouse()

            self.g_cell = lib.grid.draw(self.width + self.zoom - self.properties_width, self.zoom, self.win, (64,64,64))
            self.cx, self.cy = lib.grid.check_mouse(mouse)
            pygame.draw.rect(self.win, (64,64,64), (self.cx, self.cy, self.g_cell, self.g_cell))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.VIDEORESIZE:
                    self.width = event.w
                    self.height = event.h
                    self.win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE | pygame.SRCALPHA, vsync=1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    curr_x, curr_y = self.cx, self.cy
                    if event.button == 1:
                        self.objects['cumdumpster_01'] = lib.object.create('some cumdumpster', curr_x, curr_y, self.g_cell, self.g_cell)

                    if event.button == 4:
                        if self.zoom > 5:
                            self.zoom -= 1

                    if event.button == 5:
                        if self.zoom < 100:
                            self.zoom += 1

            lib.ui.create_properties_window(self.win, self.cx, self.cy, self.properties_width, self.objects)

            lib.window.update()
            self.clock.tick(self.fps)
            last_time = time.time()


if __name__ == '__main__':
    Main().update()
