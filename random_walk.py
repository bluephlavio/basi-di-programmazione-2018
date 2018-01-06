import sys, random, pygame

pygame.init()

bg = (0, 0, 0)
color = (100, 100, 100)
radius = 10
size = (640, 480)
x, y = map(lambda x: int(x/2), size)
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']

screen = pygame.display.set_mode(size)

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    direction = random.choices(directions)[0]
    if direction == 'LEFT':
        x -= 1
    elif direction == 'RIGHT':
        x += 1
    elif direction == 'UP':
        y -= 1
    elif direction == 'DOWN':
        y += 1

    screen.fill(bg)
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
