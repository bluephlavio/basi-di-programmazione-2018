import pygame

pygame.init()

bg = (0, 0, 0)
color = (100, 100, 100)
radius = 10
size = (640, 480)
pos = [size[0]//2, size[1]//2]
speed = 5

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

while running:

    clock.tick(50)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                pos[0] -= speed
            if e.key == pygame.K_RIGHT:
                pos[0] += speed
            if e.key == pygame.K_DOWN:
                pos[1] += speed
            if e.key == pygame.K_UP:
                pos[1] -= speed

    screen.fill(bg)
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.flip()
