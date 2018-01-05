import sys, pygame

size = (640, 480)
bg = (0, 0, 0)
color = (100, 100, 100)
r = 10
pos = [size[0]//2, size[1]//2]
if len(sys.argv) == 3:
    pos[0] = int(sys.argv[1])
    pos[1] = int(sys.argv[2])

screen = pygame.display.set_mode(size)

running = True

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg)
    pygame.draw.circle(screen, color, pos, r)
    pygame.display.flip()
