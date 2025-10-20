from src.contracts import IEngine, ITranslateGameObjects
from src.pygame_lib.pygame_engine import PygameEngine
from src.pygame_lib.services.pygame_translate_game_objects import \
    PygameTranslateGameObjects


class Factories:
    @classmethod
    def make_translate_game_objects(cls) -> ITranslateGameObjects:
        return PygameTranslateGameObjects()

    @classmethod
    def make_engine(cls) -> IEngine:
        return PygameEngine(translate_game_objects=cls.make_translate_game_objects())


factories = Factories()
