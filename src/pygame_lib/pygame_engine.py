from typing import List

import pygame

from src.contracts import IEngine, ITranslateGameObjects
from src.objects import Color, GameObject
from src.pygame_lib.exceptions import PygameValueError


class PygameEngine(IEngine):
    def __init__(self, translate_game_objects: ITranslateGameObjects):
        self._screen = None
        self._clock = None
        self._fill_color = None
        self._fps = None

        self._is_running = False

        self._rects: List[GameObject] = []
        self._translate_game_objects = translate_game_objects

    @property
    def is_running(self) -> bool:
        return self._is_running

    def init(self, width: int, height: int, caption: str, fill_color: Color, fps: int) -> None:
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        self._screen = screen
        self._clock = pygame.time.Clock()
        self._fill_color = fill_color
        self._fps = fps
        self._is_running = True

    def update(self):
        if not self._screen or not self._clock or not self._fps or not self._fill_color:
            raise PygameValueError('Must init first.')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self._is_running = False
                return

        self._screen.fill(self._fill_color.to_tuple())

        rects = self._translate_game_objects.translate(self._rects)
        for rect in rects:
            pygame.draw.rect(self._screen, rect[1], rect[0])

        pygame.display.flip()
        self._clock.tick(self._fps)

    def add_game_objects(self, game_objects: List[GameObject]) -> None:  # TODO: Validate if rect
        self._rects.extend(game_objects)
