import numpy as np
import pygame
import math
import random


class Particle:

    def __init__(self, pos=[0,0], vel=[0,0]):
        self.s = np.array(pos, dtype=float)
        self.v = np.array(vel, dtype=float)
        
    def update(self, acc=[0,0], dt=1):
        a = np.array(acc, dtype=float)
        self.s += self.v * dt
        self.v += a * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.screen_coords(), 10)

    def screen_coords(self):
        return int(self.s[0]), int(self.s[1])


class System:

    def __init__(self, n, pos_gen, vel_gen, ptype=Particle):
        self.particles = []
        for i in range(n):
            s = next(pos_gen)
            v = next(vel_gen)
            p = ptype(pos=s, vel=v)
            self.particles.append(p)

    def update(self, dt=1):
        for p in self.particles:
            p.update(dt=dt)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for p in self.particles:
            p.draw(screen)


def normal_2d_gen(mu=0, sigma=1):
    while True:
        yield np.random.normal(mu, sigma, 2)

def uniform_2d_gen(low=-1.0, high=1.0):
    while True:
        yield np.random.uniform(low, high, 2)

