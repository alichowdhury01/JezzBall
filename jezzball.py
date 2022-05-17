import pygame as pg
from pyparsing import White

class Ball:
    def __init__(self):
        self.BALL_HEIGHT = 30
        self.BALL_LENGTH = 30

class Wall:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        self.life = 3     

class Menu:
    def __init__(self):
        pass

class Jezzball:
    def __init__(self, MENU, PLAYER, WALL, BALL_HEIGHT, BALL_LENGTH):
        pg.display.set_caption("JezzBall")
        self.WINDOW_HEIGHT, self.WINDOW_LENGTH = 1280, 800
        self.WINDOW = pg.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_LENGTH))
        self.MENU = MENU
        self.PLAYER = PLAYER
        self.WALL = WALL
        self.BALL_HEIGHT = BALL_HEIGHT
        self.BALL_LENGTH = BALL_LENGTH
        self.BALL = pg.Rect(self.WINDOW_HEIGHT/2 - 15, self.WINDOW_LENGTH/2 - 15, self.BALL_HEIGHT, self.BALL_LENGTH)
        self.WHITE = 255, 255, 255

    
    def draw_window(self):
        self.WINDOW.fill(self.WHITE)
        pg.display.update()
        

    def surfacel(self):
        pass

    def main(self):
        self.RUN  = True
        while self.RUN:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.RUN = False
            self.draw_window()


if __name__ == "__main__":
    ball = Ball()
    wall = Wall()
    player = Player()
    menu = Menu()
    jezzball = Jezzball(menu, player, wall, ball.BALL_HEIGHT, ball.BALL_LENGTH)
    jezzball.main()