import sys, pygame

screen_size = width, height = (640, 480)
bg = (0, 0, 0)
color = (100, 100, 100)
pos = (width//2, height//2)
r = 10

screen = pygame.display.set_mode(screen_size)

running = True

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg)
    pygame.draw.circle(screen, color, pos, r)
    pygame.display.flip()
