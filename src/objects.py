from dataclasses import dataclass
from typing import Tuple


@dataclass
class Color:
    red: int
    blue: int
    green: int

    def to_tuple(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue


@dataclass
class GameObject:
    x: int
    y: int
    color: Color


@dataclass
class Rect(GameObject):
    width: int
    height: int
