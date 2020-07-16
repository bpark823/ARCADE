import requests
import json
import pygame

# colors
WHITE = [255, 255, 255]
BLACK = 0, 0, 0

fps = 60
clock = pygame.time.Clock()
size = WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Chuck Norris Knowledge")
screen = pygame.display.set_mode(size, 0, 32)
font = pygame.font.SysFont('Bangers', 20)

def wisdom():
    screen.fill(WHITE)
    site = "http://api.icndb.com/jokes/random"
    data = requests.get(site)
    chuck_wisdom = json.loads(data.text)
    store = chuck_wisdom["value"]["joke"]
    text = font.render(store, 1, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()


def display_wisdom():
    pygame.init()
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        wisdom()
        pygame.time.delay(3000)
        break


