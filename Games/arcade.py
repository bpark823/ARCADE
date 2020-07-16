import pygame, sys, os
from pygame.locals import *
from guess_the_number import game
from hangman import main
from rock_paper_scissors import RPS_GANG
from chuck_norris import display_wisdom
from snake import Snake
size = WIDTH, HEIGHT = 800, 600
white = [255, 255, 255]
black = 0, 0, 0
TEST = 30, 144, 255, 255
BLUE = 17, 30, 200


class Arcade:
    pygame.init()
    pygame.display.set_caption("ARCADE!")

    def drawTextcenter(self, text, font, color, screen, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=(x + 100, y + 15))
        screen.blit(textobj, textrect)

    def drawText(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        global click
        click = False
        screen = pygame.display.set_mode(size, 0, 32)
        fps = 60
        clock = pygame.time.Clock()
        default_font = pygame.font.Font('images/PressStart2P-Regular.ttf', 17)
        button_font = pygame.font.Font('images/PressStart2P-Regular.ttf', 9)
        bg_main_menu = pygame.image.load(os.path.join("images", "Arcade_Boi.jpg"))

        run = True
        while run:
            screen.fill(white)
            screen.blit(bg_main_menu, (0, 0))
            self.drawText('Welcome to the ARCADE!', default_font, white, screen, 225, 200)
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(300, 260, 200, 25)
            button_2 = pygame.Rect(300, 290, 200, 25)
            button_3 = pygame.Rect(300, 320, 200, 25)
            button_4 = pygame.Rect(300, 350, 200, 25)
            secret_button = pygame.Rect(300, 380, 200, 25)
            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    main()
            if button_3.collidepoint((mx, my)):
                if click:
                    rps = RPS_GANG()
                    rps.game()
            if button_4.collidepoint((mx, my)):
                if click:
                    snake = Snake()
                    snake.game()
            if secret_button.collidepoint((mx, my)):
                if click:
                    display_wisdom()

            pygame.draw.rect(screen, BLUE, button_1)
            self.drawTextcenter('Guess the Number', button_font, white, screen, 300, 260)
            pygame.draw.rect(screen, BLUE, button_2)
            self.drawTextcenter('Hangman', button_font, white, screen, 300, 290)
            pygame.draw.rect(screen, BLUE, button_3)
            self.drawTextcenter('Rock, Paper, Scissors', button_font, white, screen, 300, 320)
            pygame.draw.rect(screen, BLUE, button_4)
            self.drawTextcenter('Snake ', button_font, white, screen, 300, 350)
            pygame.draw.rect(screen, BLUE, secret_button)
            self.drawTextcenter('Push For Wisdom', button_font, white, screen, 300, 380)
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            clock.tick(fps)


myArcade = Arcade()
myArcade.main_menu()
