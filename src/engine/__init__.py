from src.factories import factories
from src.objects import Rect
from src.pygame_lib.pygame_engine import PygameEngine as _PygameEngine


class PygameEngine(_PygameEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(translate_game_objects=factories.make_translate_game_objects())


__all__ = ["PygameEngine", "Rect"]
