from dataclasses import dataclass


@dataclass
class Color:
    red: int
    blue: int
    green: int


@dataclass
class GameObject:
    x: int
    y: int
    color: Color


@dataclass
class Rect(GameObject):
    width: int
    height: int
