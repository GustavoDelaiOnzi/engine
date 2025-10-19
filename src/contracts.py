from abc import ABC, abstractmethod
from typing import Optional

from src.objects import GameObject


class Engine(ABC):
    @abstractmethod
    def init(self, width: int, height: int, caption: str, fps: Optional[int]) -> None: ...

    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def add_game_object(self, game_object: GameObject) -> None: ...
