import pygame
import os
import time
import random
import neat

DINO_IMGS_RUN = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinorun0000.png")), (67, 84)),
                 pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinorun0001.png")), (67, 84))]
DINO_IMGS_JUMP = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinoJump0000.png")), (67, 84))]

WIN_WIDTH = 800
WIN_HEIGHT = 400
GROUND_LANE_Y = WIN_HEIGHT - 150


class Dino:
    JUMP_FORCE = 0
    IS_JUMP = False
    JUMP_COUNT = 10
    G = 0.5
    ANIM_LONG = 4
    WIDTH = DINO_IMGS_RUN[0].get_size()[0]
    HEIGHT = DINO_IMGS_RUN[0].get_size()[1]

    def __init__(self, x):
        self.x = x
        self.y = GROUND_LANE_Y
        self.img_count = 0
        self.img = DINO_IMGS_RUN[0]
        self.THICK_COUNT = 0

    def jump(self):
        self.JUMP_FORCE = 4.5
        self.IS_JUMP = True

    def movement_controller(self):
        if (self.IS_JUMP):
            self.THICK_COUNT += 1
            d = -1 * (self.JUMP_FORCE * self.THICK_COUNT - 0.5 * self.G * (self.THICK_COUNT) ** 2)
            if GROUND_LANE_Y >= self.y + d:
                self.y = self.y + d
            else:
                self.THICK_COUNT = 0
                self.IS_JUMP = False
                self.y = GROUND_LANE_Y

    def draw(self, win):

        self.img_count += 1
        if self.img_count < self.ANIM_LONG:
            self.img = DINO_IMGS_RUN[0]
        elif self.img_count < self.ANIM_LONG * 2:
            self.img = DINO_IMGS_RUN[1]
        elif self.img_count > self.ANIM_LONG * 2:
            self.img_count = 0

        new_rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y - 20)).center)
        win.blit(self.img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
