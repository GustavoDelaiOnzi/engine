from abc import ABC, abstractmethod
from typing import List, Tuple

import pygame

from src.objects import Color, GameObject


class IEngine(ABC):
    @property
    @abstractmethod
    def is_running(self) -> bool: ...

    @abstractmethod
    def init(self, width: int, height: int, caption: str, fill_color: Color, fps: int) -> None: ...

    @abstractmethod
    def update(self) -> None: ...

    @abstractmethod
    def add_game_objects(self, game_objects: List[GameObject]) -> None: ...


class ITranslateGameObjects(ABC):
    @abstractmethod
    def translate(self, game_objects: List[GameObject]) -> List[Tuple[pygame.Rect, Tuple[int, int, int]]]: ...
