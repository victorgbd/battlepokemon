from Game import Game
class Main:
    def __init__(self):
        self.game = Game()

    def start(self):
        self.game.start()


if __name__ == "__main__":
    main = Main()
    main.start()