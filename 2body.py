import sys, os, math, pygame
import numpy as np
from numpy.linalg import norm

class Particle:

    def __init__(self, s, v, m, color=(0, 0, 0), density=1, radius=None, image=None, label=None):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.density = float(density)
        self.color = color
        
        self.radius = radius if radius else int(math.sqrt(m / (math.pi * density)))

        font = pygame.font.Font('.\\font\\Quicksand-Light.ttf', 16)
        text = label if label else str(self) 
        self.label = font.render(text, True, (100, 100, 100))

        if image:
            image = image.replace('/', os.sep).replace('\\', os.sep)
            self.image = pygame.image.load(image)
            self.image = pygame.transform.smoothscale(self.image, (2*self.radius, 2*self.radius))
        else:
            self.image = None

    def update(self, force, dt=1):
        f = np.array(force, dtype=float)
        a = f / self.m
        self.v += a*dt
        self.s += self.v*dt

    def draw(self, screen):
        x, y = self.coordinates()
        if self.image:
            ximg, yimg = x - self.image.get_width()//2, y - self.image.get_height()//2
            screen.blit(self.image, (ximg, yimg))
        else:
            pygame.draw.circle(screen, self.color, (x, y), self.radius)
        xlabel, ylabel = x + .5 * self.radius, y - .5 * self.radius - self.label.get_height()
        screen.blit(self.label, (xlabel, ylabel))

    def coordinates(self):
        return tuple(map(int, self.s))

    def __str__(self):
        return f'{self.m}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.s}, {self.v}, {self.m})'


class System:

    G = 6.67e-11

    def __init__(self, scaled=False):
        self.bg = pygame.image.load('.\\img\\bg-light.jpg')
        
        self.size = width, height = self.bg.get_size()
        self.center = center_x, center_y = (width//2, height//2)

        scale = 1e9
        self.G =  System.G * scale**-3
        
        D = 1.5e11
        d = D * scale**-1

        m1 = 2e30
        m2 = 6e29
        m = m1 + m2

        s1 = [center_x - m2*d/m, center_y]
        s2 = [center_x + m1*d/m, center_y]

        v2 = np.array([0, -math.sqrt(self.G*m1/d)], dtype=float)
        v1 = -m2/m1 * v2

        d1 = 1.408e3 * scale**3
        d2 = 5.515e3 * scale**3

        r1 = None if scaled else 100
        r2 = None if scaled else 30
        
        p1 = Particle(s1, v1, m1, density=d1, radius=r1, image='img\\star.png')
        p2 = Particle(s2, v2, m2, density=d2, radius=r2, image='.\\img\\planet.png')

        self.particles = [p1, p2]

    def update(self, dt=86400):
        p1, p2 = self.particles
        
        f1 = self.G*(p1.m*p2.m/norm(p2.s - p1.s)**3)*(p2.s - p1.s)
        f2 = -f1
        
        p1.update(f1, dt)
        p2.update(f2, dt)

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        for p in self.particles:
            p.draw(screen)


pygame.init()

system = System()

icon = pygame.image.load('.\\img\\icon.jpg')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
pygame.display.set_caption('2 body simulation')
screen = pygame.display.set_mode(system.size)

clock = pygame.time.Clock()


running = True

while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    system.update()
    system.draw(screen)
    pygame.display.flip()

