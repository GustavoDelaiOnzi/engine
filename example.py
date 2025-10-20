def main():
    from src.objects import Color
    from src.pygame.pygame_engine import PygameEngine

    engine = PygameEngine()
    black = Color(red=0, green=0, blue=0)

    engine.init(width=600, height=600, caption='Nao sei')
    engine.start(black, 30)


if __name__ == '__main__':
    main()
