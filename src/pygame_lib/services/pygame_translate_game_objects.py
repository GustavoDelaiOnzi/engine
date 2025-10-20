from typing import List, Tuple

import pygame

from src.contracts import ITranslateGameObjects
from src.objects import GameObject, Rect


class PygameTranslateGameObjects(ITranslateGameObjects):
    def translate(self, game_objects: List[GameObject]) -> List[Tuple[pygame.Rect, Tuple[int, int, int]]]:
        objs = []
        for game_object in game_objects:
            if isinstance(game_object, Rect):
                rect = pygame.Rect(game_object.x, game_object.y, game_object.width, game_object.height)
                color = game_object.color
                objs.append((rect, (color.red, color.green, color.blue)))
        return objs
