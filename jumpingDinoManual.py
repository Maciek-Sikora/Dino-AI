import pygame
import os
import time
import random

pygame.font.init()
pygame.display.set_caption("Dino")
WIN_WIDTH = 800
WIN_HEIGHT = 400

DINO_IMGS_RUN = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinorun0000.png")), (67, 84)),
                 pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinorun0001.png")), (67, 84))]
DINO_IMGS_JUMP = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dinoJump0000.png")), (67, 84))]

CACTUS_IMGS = [pygame.transform.scale(pygame.image.load(os.path.join("imgs", "cactusBig0000.png")), (60, 120)),
               pygame.transform.scale(pygame.image.load(os.path.join("imgs", "cactusSmall0000.png")), (40, 80))]

GROUND_LANE_Y = WIN_HEIGHT - 150

STAT_FONT = pygame.font.SysFont("comicsans", 35)


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

    def movementController(self):
        if (self.IS_JUMP):
            self.THICK_COUNT += 1
            d = -1 * (self.JUMP_FORCE * self.THICK_COUNT - 0.5 * self.G * (self.THICK_COUNT) ** 2)
            if (GROUND_LANE_Y >= self.y + d):
                self.y = self.y + d
            else:
                self.THICK_COUNT = 0
                self.IS_JUMP = False
                self.y = GROUND_LANE_Y

    def draw(self, win):

        self.img_count += 1
        if (self.img_count < self.ANIM_LONG):
            self.img = DINO_IMGS_RUN[0]
        elif (self.img_count < self.ANIM_LONG * 2):
            self.img = DINO_IMGS_RUN[1]
        elif (self.img_count > self.ANIM_LONG * 2):
            self.img_count = 0

        new_rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y - 20)).center)
        win.blit(self.img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Cact:
    VEL = 12

    def __init__(self, img):
        self.x = WIN_WIDTH + 10
        self.y = GROUND_LANE_Y
        self.img = img

    def movementController(self):
        self.x -= self.VEL

    def draw(self, win):
        WIDTH = self.img.get_size()[0]
        HEIGHT = self.img.get_size()[1]
        new_rect = self.img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y - HEIGHT + 56)).center)
        win.blit(self.img, new_rect.topleft)

    def coilde(self, dino):
        dino_mask = dino.get_mask()
        cact_mask = pygame.mask.from_surface(self.img)

        cact_offset = (self.x - dino.x, self.y - round(dino.y))

        Col_point = dino_mask.overlap(cact_mask, cact_offset)

        if Col_point:
            return True
        return False


def drawWindow(win, dinos, cacts, dystans, punkty):
    win.fill("white")

    pygame.draw.line(win, (0, 0, 0), (0, GROUND_LANE_Y + 55), (WIN_WIDTH, GROUND_LANE_Y + 55))

    text = STAT_FONT.render("Dystans: " + str(dystans), 1, (0, 0, 0))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Punkty: " + str(punkty), 1, (0, 0, 0))
    win.blit(text, (10, 10))

    for dino in dinos:
        dino.draw(win)

    for cact in cacts:
        cact.draw(win)
    pygame.display.update()


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
dystans = 0
punkty = 0
run = True
dinos = [Dino(200)]
cacts = [Cact(CACTUS_IMGS[1])]
cacts_pased = []
while run:
    dists = [300, 300, 300, 300]
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dinos[0].jump()
    for dino in dinos:
        dino.movementController()
        for y, cact in enumerate(cacts):
            if (not (cact in cacts_pased)):
                dists[y] = abs(dino.x - cact.x)
    print(dists)

    for cact in cacts:
        if (cact.x < -50):
            cacts.remove(cact)
            cacts_pased.remove(cact)

    if len(cacts) < 4:
        if random.random() > 0.98:
            cacts.append(Cact(CACTUS_IMGS[1]))

    for cact in cacts:
        cact.movementController()
        for dino in dinos:
            if cact.coilde(dino):
                dystans = 0
            if (dino.x > cact.x and cact not in cacts_pased):
                punkty += 1
                cacts_pased.append(cact)

    dystans += 1
    drawWindow(win, dinos, cacts, dystans, punkty)
