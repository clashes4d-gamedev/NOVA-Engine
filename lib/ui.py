import pygame
pygame.init()

class UI():
    def __init__(self) -> None:
        pass

    def get_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_btns = pygame.mouse.get_pressed()

        return [mouse_pos, mouse_btns]

    def text_render(self, win, x, y, font, size, color, text):
        pygame.font.init()
        txt = pygame.font.SysFont(font, size)
        txt_surf = txt.render(text, False, color)
        win.blit(txt_surf, (x, y))
        return txt_surf

        # context_actions = {'task': [desc, target(func)]}
    def contex_menu(self, win, ctx_x, ctx_y, mouse, context_actions):
        ctx_rect = pygame.Rect(ctx_x, ctx_y, 100, 500)

        for i in range(len(context_actions)):
            ctx_button_current = self.button(win, mouse[0][0], mouse[0][1], win.get_width(), (win.get_height()/len(context_actions)), mouse, 1,
                        btn_color=(64,64,64),
                        btn_txt_color=(100,100,100),
                        btn_text=context_actions[i][0])

    def button(self, win, x, y, width, height, mouse, btn, img_path='', btn_color=(255,255,255), btn_txt_color=(0,0,0), btn_txt_size=10, btn_font='Arial', btn_text='BTN'):
        button_collider = pygame.Rect(x, y, width, height)
        button_surf = pygame.Surface((button_collider.width, button_collider.height))

        if img_path != '':
            button_img = pygame.image.load(str(img_path), '.png').convert()
            button_img.set_colorkey((0,0,0))
            button_img = pygame.transform.scale(button_img, (button_surf.get_width(), button_surf.get_height()))
            button_surf.blit(button_img, (0,0))
        else:
            button_surf.fill(btn_color)
            self.text_render(button_surf, 0, 0, btn_font, btn_txt_size, btn_txt_color, btn_text)
        win.blit(button_surf, (button_collider.x, button_collider.y))

        if pygame.Rect.collidepoint(button_collider, mouse[0][0], mouse[0][1]):
            if mouse[1][btn] is True:
                return True
            else:
                return False
        else:
            return False


    def create_properties_window(self, win, cx, cy, width, objects, bg_color=()):
        properties_collider = pygame.Rect(win.get_width() - width, 0, width, win.get_height())
        properties_surf = pygame.Surface((properties_collider.width, properties_collider.height))
        if bg_color != tuple():
            properties_surf.fill(bg_color)
        else:
            properties_surf.fill((64, 64, 64))

        # get name of every object in scene
        object_names = []
        for object in objects:
            object_names.append(object)

        # get value of every property in object
        obj_index = 0
        if (pygame.Rect) in objects.values():
            print('cum')
        else:
            for object in objects.values():
                obj_name = object_names[obj_index]

                if object['properties'] != {}:
                    if pygame.Rect.collidepoint(object['properties']['collider'], (cx,cy)):
                        print(object['properties']['collider'])

                else:
                    pass

                if obj_index <= len(objects):
                    obj_index += 1
                else:
                    obj_index = 0
                #print(object)

        win.blit(properties_surf, (properties_collider.x, properties_collider.y))