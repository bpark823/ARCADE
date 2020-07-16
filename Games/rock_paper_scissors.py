import random
from random import choice
import pygame, sys, os
from pygame.locals import *

# Colors
WHITE = [255, 255, 255]
BLACK = 0, 0, 0

BLUE = pygame.Color('dodgerblue1')

# Fonts
size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size, 0, 32)
fps = 60
clock = pygame.time.Clock()



class Button:
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = width
        self.height = height


class RPS_GANG:

    def __init__(self):
        pygame.init()
        self.com_score = 0
        self.player_score = 0
        self.background = pygame.image.load(os.path.join('images', "rps_bg.png"))
        screen.blit(self.background, (0, 0))
        self.font = pygame.font.Font('images/PressStart2P-Regular.ttf', 50)
        self.rock = pygame.image.load(os.path.join("images", "rock.png"))
        self.paper = pygame.image.load(os.path.join("images", "paper.png"))
        self.scissor = pygame.image.load(os.path.join("images", "scissors.png"))
        self.title = pygame.image.load(os.path.join("images", "RockPaperScissors_title.jpg"))
        self.rock_button = pygame.image.load(os.path.join("images", "r_button.png"))
        self.paper_button = pygame.image.load(os.path.join("images", "p_button.png"))
        self.scissors_button = pygame.image.load(os.path.join("images", "s_button.png"))
        self.pc_rock = pygame.image.load(os.path.join("images", "pc_rock.png"))
        self.pc_paper = pygame.image.load(os.path.join("images", "pc_paper.png"))
        self.pc_scissors = pygame.image.load(os.path.join("images", "pc_scissors.png"))
        self.random_pc_choice = " "
        self.r_button = pygame.Rect(25, 450, 250, 116)
        self.p_button = pygame.Rect(270, 450, 250, 116)
        self.s_button = pygame.Rect(525, 450, 250, 116)
        screen.blit(self.title, (0, 0))
        screen.blit(self.rock_button, (25, 450))
        screen.blit(self.paper_button, (270, 450))
        screen.blit(self.scissors_button, (525, 450))


    def player(self, x, y):
        self.player_choice = ' '
        if self.r_button.collidepoint(x, y): # fix this shit
            self.player_choice = 'rock'
            screen.blit(self.rock, (50, 250))
            print('cum')
        elif self.p_button.collidepoint(x, y):
            self.player_choice = 'paper'
            screen.blit(self.paper, (50, 250))
            print('cum')
        elif self.s_button.collidepoint(x, y):
            self.player_choice = 'scissors'
            screen.blit(self.scissor, (50, 250))
            print('cum')
        return self.player_choice

    def com(self):

        choices = ["rock", "paper", "scissors"]
        pc_choice = random.choice(choices)
        if pc_choice == "rock":
            self.random_pc_choice = pc_choice
            pc_choice = self.pc_rock
            print("shit test")
        elif pc_choice == "paper":
            self.random_pc_choice = pc_choice
            pc_choice = self.pc_paper
            print("shit test")
        else:
            self.random_pc_choice = pc_choice
            print("shit test")
            pc_choice = self.pc_scissors
        return screen.blit(pc_choice, (500, 250))

    def reset(self):
        screen.blit(self.background, (0,0))
        screen.blit(self.title, (0, 0))
        screen.blit(self.rock_button, (25, 450))
        screen.blit(self.paper_button, (270, 450))
        screen.blit(self.scissors_button, (525, 450))

    def player_keep_score(self):
        point = 0
        if self.random_pc_choice == self.player_choice:
            pass
        elif (self.random_pc_choice == "rock" and self.player_choice == "paper") or (
                self.random_pc_choice == "paper" and self.player_choice == "scissors") or (
                self.random_pc_choice == "scissors" and self.player_choice == "rock"):
            point += 1
            self.player_score = point
        else:
            pass
        return point

    def com_keep_score(self):
        pc_point = 0
        if self.random_pc_choice == self.player_choice:
            pass
        elif (self.random_pc_choice == "rock" and self.player_choice == "scissors") or (
                self.random_pc_choice == "paper" and self.player_choice == "rock") or (
                self.random_pc_choice == "scissors" and self.player_choice == "paper"):
            pc_point += 1
            self.com_score = pc_point
        else:
            pass
        return pc_point

    def winner_display_message(self, message):
        self.player_score += self.player_keep_score()
        text = self.font.render("{}:{}".format(self.player_score, self.com_score), 1, BLACK)
        screen.blit(text, (325, 150))
        pygame.time.delay(1000)
        screen.fill(BLACK)
        text = self.font.render(message, 1, WHITE)
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1500)

    def loser_display_message(self, message):
        self.com_score += self.com_keep_score()
        text = self.font.render("{}:{}".format(self.player_score, self.com_score), 1, BLACK)
        screen.blit(text, (325, 150))
        pygame.time.delay(1000)
        screen.fill(BLACK)
        text = self.font.render(message, 1, WHITE)
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1500)

    def game(self):
        global click
        run = True
        while run:

            clock.tick(fps)
            mx, my = pygame.mouse.get_pos()
            if self.r_button.collidepoint((mx, my)) or self.p_button.collidepoint((mx, my)) or self.s_button.collidepoint((mx, my)):
                if click:
                    self.reset()
                    self.player(mx, my)
                    self.com()
                    self.player_score += self.player_keep_score()
                    self.com_score += self.com_keep_score()
                    text = self.font.render("{}:{}".format(self.player_score, self.com_score), 1, BLACK)
                    screen.blit(text, (325, 150))
                    pygame.display.update()



            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if self.player_score == 5:
                self.winner_display_message("YOU WIN!")
                break
            elif self.com_score == 5:
                self.loser_display_message("YOU LOSE!")
                break
            pygame.display.flip()
