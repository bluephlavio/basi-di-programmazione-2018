import sys, random, pygame

pygame.init()

size = width, height = (640, 480)
scale = ((width/2)**2 + (height/2)**2)**.5
r0 = 10

directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']

speed = int(input('Inserisci la velocità del random walk: '))

def distance_from_center(x, y):
    return ((x-width/2)**2 + (y-height/2)**2)**.5

def get_bg_by_position(x, y):
    r = int(distance_from_center(x, y) / scale * 255)
    return (min(r, 255), 80, 50)

def get_color_by_position(x, y):
    r = int(distance_from_center(x, y) / scale * 255)
    return (50, 20, min(r, 255))

def get_radius_by_position(x, y):
    return r0 + int(distance_from_center(x, y) / scale * r0)

screen = pygame.display.set_mode(size)
x, y = map(lambda x: int(x/2), size)

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    direction = random.choices(directions)[0]
    if direction == 'LEFT':
        x -= speed
    elif direction == 'RIGHT':
        x += speed
    elif direction == 'UP':
        y -= speed
    elif direction == 'DOWN':
        y += speed

    bg = get_bg_by_position(x, y)
    color = get_color_by_position(x, y)
    radius = get_radius_by_position(x,y)

    screen.fill(bg)
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

    
