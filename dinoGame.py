import pygame
import random
from dino import Dino
from cactus import Cact
import os

WIN_HEIGHT = 400
WIN_WIDTH = 800

GROUND_LANE_Y = WIN_HEIGHT - 150
pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 35)

class DinoGame:
    def __init__(self):
        pygame.font.init()
        pygame.display.set_caption("Dino")
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.distance = 0
        self.points = 0
        self.run = True
        self.dinos = []
        self.nets = []
        self.genomes = []
        self.cacts = [Cact()]
        self.cacts_pased = []
        self.cact_spawn_timer = 0
        self.cact_spawn_interval = 1000

    def draw_window(self, distance, points, GEN):
        self.win.fill("white")

        pygame.draw.line(self.win, (0, 0, 0), (0, GROUND_LANE_Y + 55), (WIN_WIDTH, GROUND_LANE_Y + 55))

        text = STAT_FONT.render("Distance: " + str(round(distance, -1)), 1, (0, 0, 0))
        self.win.blit(text, (WIN_WIDTH - 10 - round(text.get_width(), -1), 10))

        text = STAT_FONT.render("Points: " + str(points), 1, (0, 0, 0))
        self.win.blit(text, (10, 10))

        text = STAT_FONT.render("GEN: " + str(GEN), 1, (0, 0, 0))
        self.win.blit(text, (250, 10))

        text = STAT_FONT.render("Alive: " + str(self.number_of_dinos()), 1, (0, 0, 0))
        self.win.blit(text, (450, 10))

        for dino in self.dinos:
            dino.draw(self.win)

        for cact in self.cacts:
            cact.draw(self.win)

        pygame.display.update()

    def remove_cacts_outside_map(self):
        for cact in self.cacts:
            if (cact.isOutside()):
                self.cacts.remove(cact)

    def calculate_distances(self):
        distances = []
        xOfDisnos = self.dinos[0].x
        for i, cact in enumerate(self.cacts):
            if (not (cact in self.cacts_pased)):
                distances.append(abs(xOfDisnos - cact.x))
        while len(distances) <= 4:
            distances.append(1000)
        return distances

    def spawn_cactus(self):
        if self.cact_spawn_timer <= 0:
            self.cacts.append(Cact())
            self.cact_spawn_timer = random.randint(20, 50)  # Randomize spawn timer
        else:
            self.cact_spawn_timer -= 1

    def number_of_dinos(self):
        return len(self.dinos)

    def spirits_movement(self):
        for dino in self.dinos:
            dino.movement_controller()

        for cact in self.cacts:
            cact.movement_controller()

    def check_dino_colision(self, dino):
        for cact in self.cacts:
            if cact.coilde(dino):
                return True
        return False

    def check_cacts_passed(self, dino):
        for cact in self.cacts:
            if dino.x > cact.x and cact not in self.cacts_pased:
                self.cacts_pased.append(cact)
                return True
        return False
