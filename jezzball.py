import sys
import pygame




class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy= 0
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def start_moving(self):
        self.dx = 10
        self.dy = 10

    def move(self):
        self.posX += self.dy
        self.posY += self.dx

    def wall_collision(self):
        self.dy = -self.dy + -self.dx
        self.dx = -self.dx + -self.dy

class CollisionManager:
    def between_ball_wall(self, ball):
        # Top
        if ball.posY - ball.radius <= 0:
            return True

        # Bottom 
        if ball.posY + ball.radius >= HEIGHT:
            return True

        # Top
        if ball.posX + ball.radius <= 0:
            return True

        # Bottom 
        if ball.posX - ball.radius >= WIDTH:
            return True

        return False


WIDTH = 900
HEIGHT = 500

# COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("JeezBall")

def paint_back():
    screen.fill(BLACK)


paint_back()

# Objects 
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 10)
collision = CollisionManager()


playing = False
FPS = 60
clock = pygame.time.Clock()

# Main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # keyboard letter p to start the game 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start_moving()
                playing = True

        if playing:
            paint_back()

        # ball movement
        ball.move()
        ball.draw()


        if collision.between_ball_wall(ball):
            ball.wall_collision()



    pygame.display.update()
