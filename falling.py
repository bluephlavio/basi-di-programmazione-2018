import sys, pygame

size = width, height = (640, 480)
bg = (0, 0, 0)
color = (100, 100, 100)
r = 10
pos = [size[0]//2, 0]
vel = [5, 0]
acc = [0, 1]
dt = 1

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

while running:

    clock.tick(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    if pos[1] < height - (r + vel[1]*dt):
        pos[0] += vel[0]*dt
        pos[1] += vel[1]*dt
        vel[0] += acc[0]*dt
        vel[1] += acc[1]*dt

    screen.fill(bg)
    pygame.draw.circle(screen, color, pos, r)
    pygame.display.flip()
