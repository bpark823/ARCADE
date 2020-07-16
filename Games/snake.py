import pygame, random

size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
fps = 15
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
BLACK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0, 0

class Snake:
    def __init__(self):
        pygame.init()
        screen.fill(BLACK)
        self.more_snake = []
        self.x = 400
        self.y = 300
        self.head = []

        self.x_change = 0
        self.y_change = 0
        self.foodx = 0
        self.foody = 0
        self.font = pygame.font.Font('images/PressStart2P-Regular.ttf', 50)
        self.snake_length = 1
        self.score = 0

    def long_boi(self, length):
        for x in length:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], 10, 10])

    def display_message(self, message):
        pygame.time.delay(1000)
        screen.fill(BLACK)
        screen.blit(self.font.render("Score:{}".format(self.score), 1, WHITE), (0, 0))
        text = self.font.render(message, 1, WHITE)
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1500)


    def game(self):
        run = True
        self.foodx = round(random.randrange(0, WIDTH - 20) / 10.0) * 10.0
        self.foody = round(random.randrange(0, HEIGHT - 20) / 10.0) * 10.0
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.x_change = 0
                        self.y_change = -10
                    elif event.key == pygame.K_a:
                        self.x_change = -10
                        self.y_change = 0
                    elif event.key == pygame.K_s:
                        self.x_change = 0
                        self.y_change = 10
                    elif event.key == pygame.K_d:
                        self.x_change = 10
                        self.y_change = 0


            if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
                self.display_message("YOU LOSE!")
                break
            self.x += self.x_change
            self.y += self.y_change
            screen.fill(BLACK)
            pygame.draw.rect(screen, RED, pygame.Rect(self.foodx, self.foody, 10, 10))
            self.snake_head = []
            self.snake_head.append(self.x)
            self.snake_head.append(self.y)
            self.more_snake.append(self.snake_head)

            if len(self.more_snake) > self.snake_length:
                del self.more_snake[0]
            for x in self.more_snake[:-1]:
                if x == self.snake_head:
                    self.display_message("YOU LOSE!")
                    run = False
                    break


            self.long_boi(self.more_snake)
            if self.x == self.foodx and self.y == self.foody:
                self.foodx = round(random.randrange(0, WIDTH - 20) / 10.0) * 10.0
                self.foody = round(random.randrange(0, HEIGHT - 20) / 10.0) * 10.0
                self.snake_length +=1
                self.score += 1
            screen.blit(self.font.render("Score:{}".format(self.score), 1, WHITE), (0,0))
            pygame.display.update()


            clock.tick(fps)
