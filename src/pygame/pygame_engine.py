import sys

import pygame
from src.contracts import IEngine
from src.objects import Color, GameObject
from src.pygame.exceptions import PygameValueError


class PygameEngine(IEngine):
    def __init__(self):
        self._screen = None
        self._clock = None

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

            pygame.display.flip()
            self._clock.tick(fps)

    def add_game_object(self, game_object: GameObject) -> None:
        ...
