import pygame
import random
import math

class Box(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def check_xy(self, pos):
        x, y = False, False
        if pos[0] > 0 and pos[0] < self.width:
            x = True
        if pos[1] > 0 and pos[1] < self.height:
            y = True
        return x, y


class Particle(object):

    def __init__(self, pos, vel, radius=10, color=(80,10,10)):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.color = color

    def bounce(self, box):
        xy = box.check_xy(self.pos)
        for i in (0,1):
            if not xy[i]:
                self.vel[i] = - self.vel[i]

    def update(self, acc, dt, box=None):
        for i in (0,1):
            self.vel[i] += acc[i] * dt
            self.pos[i] += self.vel[i] * dt
        if box:
            self.bounce(box)
        
    def render(self, screen):
        s = x, y = int(self.pos[0]), int(self.pos[1])
        pygame.draw.circle(screen, self.color, s, self.radius)


class System(object):

    def __init__(self, n, box, vel_max):
        self.particles = []
        for i in range(n):
            pos = [random.uniform(0, box.width), random.uniform(0, box.height)]
            angle = random.uniform(0, 2 * math.pi)
            vel_mag = random.uniform(0, vel_max)
            vel = [vel_mag * math.cos(angle), vel_mag * math.sin(angle)]
            particle = Particle(pos, vel)
            self.particles.append(particle)

    def check_collision(self, i, j):
        p1, p2 = self.particles[i], self.particles[j]
        x1, y1 = p1.pos[0], p1.pos[1]
        x2, y2 = p2.pos[0], p2.pos[1]
        dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx**2 + dy**2)
        if d < p1.radius + p2.radius:
            return True
        return False

    def collide(self, i, j):
        p1, p2 = self.particles[i], self.particles[j]
        x1, y1 = p1.pos[0], p1.pos[1]
        x2, y2 = p2.pos[0], p2.pos[1]
        dr = dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx**2 + dy**2)
        v1 = vx1, vy1 = p1.vel[0], p1.vel[1]
        v2 = vx2, vy2 = p2.vel[0], p2.vel[1]
        versor = dx / d, dy / d
        vt1 = vx1 * versor[0] + vy1 * versor[1]

    def update(self, dt, box=None):
        for particle in self.particles:
            particle.update((0,0), dt, box)

    def render(self, screen):
        for particle in self.particles:
            particle.render(screen)


screen_size = width, height = 640, 400
bg_color = 20,80,240
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

box = Box(width, height)
system = System(10, box, 0.1)

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill(bg_color)
    dt = clock.tick(1000)
    system.update(dt, box)
    system.render(screen)
    pygame.display.flip()
