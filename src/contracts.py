from abc import ABC, abstractmethod

from src.objects import Color, GameObject


class IEngine(ABC):
    @abstractmethod
    def init(self, width: int, height: int, caption: str) -> None: ...

    @abstractmethod
    def start(self, fill_color: Color, fps: int) -> None: ...

    @abstractmethod
    def add_game_object(self, game_object: GameObject) -> None: ...
