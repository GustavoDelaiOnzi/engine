import sys
from typing import List, Tuple

import pygame

from src.contracts import IEngine, ITranslateGameObjects
from src.objects import Color, GameObject
from src.pygame_lib.exceptions import PygameValueError


class PygameEngine(IEngine):
    def __init__(self, translate_game_objects: ITranslateGameObjects):
        self._screen = None
        self._clock = None
        self._rects: List[Tuple[pygame.Rect, Tuple[int, int, int]]] = []
        self._translate_game_objects = translate_game_objects

    def init(self, width: int, height: int, caption: str) -> None:
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        self._screen = screen
        self._clock = pygame.time.Clock()

    def start(self, fill_color: Color, fps: int):
        if not self._screen or not self._clock:
            raise PygameValueError('Must init first.')

        while True:  # TODO: custom inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._screen.fill(fill_color.to_tuple())

            for rect in self._rects:
                pygame.draw.rect(self._screen, rect[1], rect[0])

            pygame.display.flip()
            self._clock.tick(fps)

    def add_game_objects(self, game_objects: List[GameObject]) -> None:
        translated_objects = self._translate_game_objects.translate(game_objects)
        self._rects.extend(translated_objects)
