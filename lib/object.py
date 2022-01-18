import pygame


class Object():
    def __init__(self) -> None:
        pass

    def create(self, description, x, y, width, height):
        obj = {}
        obj_coll = pygame.Rect(x, y, width, height)

        obj['properties'] = {}
        obj['properties']['description'] = description
        obj['properties']['collider'] = obj_coll

        return obj
