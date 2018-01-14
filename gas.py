import pygame
import numpy as np

class Particle:

    def __init__(self, s, v):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)

    def coordinates(self):
        return tuple(map(int, self.s))

    def update(self, dt, box=None):
        self.s += self.v * dt
        if box:
            x, y = self.coordinates()
            vx, vy = self.v[0], self.v[1]
            if (x < 0 and vx < 0) or (x > box.width and vx > 0):
                self.v[0] = -self.v[0]
            if (y < 0 and vy < 0) or (y > box.height and vy > 0):
                self.v[1] = -self.v[1]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.coordinates(), 10)


class Box:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.particles = []

    def resize(self, width, height):
        self.width = width
        self.height = height

    def size(self):
        return (self.width, self.height)
        
    def create(self, n, sigma):
        for i in range(n):
            s = np.random.uniform((0, 0), (self.width, self.height), 2)
            v = np.random.normal(0, sigma, 2)
            particle = Particle(s, v)
            self.particles.append(particle)

    def update(self, dt):
        for p in self.particles:
            p.update(dt, box=self)

    def draw(self, screen):
        for p in self.particles:
            p.draw(screen)



box = Box(640, 480)
box.create(100, 10)
screen = pygame.display.set_mode((box.width, box.height), pygame.RESIZABLE)
clock = pygame.time.Clock()
dt = .1

running = True

while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.VIDEORESIZE:
            width, height = e.size
            box.resize(width, height)
            screen = pygame.display.set_mode(box.size(), pygame.RESIZABLE)

    screen.fill((0, 0, 0))
    box.update(dt)
    box.draw(screen)
    pygame.display.flip()

        
