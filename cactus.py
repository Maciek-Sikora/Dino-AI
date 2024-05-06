import pygame
import os
import random

WIN_HEIGHT = 400
WIN_WIDTH = 800

CACTUS_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join("imgs","cactusBig0000.png")), (60,120)),
               pygame.transform.scale(pygame.image.load(os.path.join("imgs","cactusSmall0000.png")), (40, 80))]

GROUND_LANE_Y = WIN_HEIGHT - 150


class Cact:
    VEL = 12
    def __init__(self):
        self.x = WIN_WIDTH + 10
        self.y = GROUND_LANE_Y
        self.img= CACTUS_IMGS[random.randint(0,1)]

    def movement_controller(self):
        self.x -= self.VEL

    def draw(self, win):
        WIDTH = self.img.get_size()[0]
        HEIGHT =  self.img.get_size()[1]
        new_rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y - HEIGHT + 56)).center)
        win.blit(self.img, new_rect.topleft)

    def coilde(self,dino):
        dino_mask = dino.get_mask()
        cact_mask = pygame.mask.from_surface(self.img)
        cact_offset = (self.x - dino.x, self.y - round(dino.y))

        col_point = dino_mask.overlap(cact_mask, cact_offset)

        if col_point:
            return True
        return False

    def isOutside(self):
        return self.x < -50
