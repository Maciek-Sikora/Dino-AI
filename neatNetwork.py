import pygame
import os
import neat
from dino import Dino
from cactus import Cact
from dinoGame import DinoGame


class NeatNetwork:
    def __init__(self):
        self.GEN = 0
        self.clock = pygame.time.Clock()
        self.restart()

    def restart(self):
        self.distance = 0
        self.points = 0
        self.run = True
        self.nets = []
        self.ge = []
        self.dinoGame = DinoGame()

    def create_genomes(self, genomes, config):
        for _, g in genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
            self.nets.append(net)
            self.dinoGame.dinos.append(Dino(200))
            g.fitness = 0
            self.ge.append(g)

    def main(self, genomes, config):
        self.restart()
        self.create_genomes(genomes, config)
        pygame_icon = pygame.image.load(os.path.join("imgs", "dinorun0000.png"))
        pygame.display.set_icon(pygame_icon)
        self.GEN += 1
        while self.run:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.run = False
                    quit()
                    break

            if self.dinoGame.number_of_dinos() <= 0:
                self.run = False
                break

            dists = self.dinoGame.calculate_distances()
            for x in range(self.dinoGame.number_of_dinos()):
                self.ge[x].fitness += 0.05
                output = self.nets[x].activate((self.dinoGame.dinos[x].y, dists[0], dists[1], dists[2]))

                if output[0] > 0.4:
                    self.dinoGame.dinos[x].jump()

            self.dinoGame.spawn_cactus()
            self.dinoGame.spirits_movement()
            self.dinoGame.remove_cacts_outside_map()

            for x, dino in reversed(list(enumerate(self.dinoGame.dinos))):
                if self.dinoGame.check_dino_colision(dino):
                    self.distance = 0
                    self.ge[x].fitness -= 1
                    self.dinoGame.dinos.pop(x)
                    self.nets.pop(x)
                    self.ge.pop(x)
                if self.dinoGame.check_cacts_passed(dino):
                    self.points += 1
                    for g in self.ge:
                        g.fitness += 2
            self.distance += 1
            self.dinoGame.draw_window(self.distance, self.points, self.GEN)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    network = NeatNetwork()
    winner = p.run(network.main, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
