from src.factories import factories
from src.objects import Rect


def main():
    from src.objects import Color

    engine = factories.make_engine()
    black = Color(red=0, green=0, blue=0)
    red = Color(red=255, green=0, blue=0)
    rect = Rect(x=0, y=0, width=100, height=100, color=red)

    engine.add_game_objects([rect])
    engine.init(width=600, height=600, caption='Nao sei', fill_color=black, fps=30)
    while engine.is_running:
        rect.x += 1  # Rect must move to the right
        engine.update()


if __name__ == '__main__':
    main()
