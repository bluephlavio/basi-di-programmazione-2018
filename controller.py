import pygame

# COLORI
colore_sfondo = (0, 0, 0)
colore_cerchio = (100, 100, 100)

# DIMENSIONI
larghezza = 640
altezza = 480
dimensioni = (larghezza, altezza)
raggio_cerchio = 10

# POSIZIONI E VELOCITA'
vel = 5
pos = [larghezza//2, altezza//2]

# SCHERMO
schermo = pygame.display.set_mode(dimensioni)

# TEMPO
tempo = pygame.time.Clock()

# INPUT
def process_input_1(e):
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
            pos[0] -= vel
        if e.key == pygame.K_RIGHT:
            pos[0] += vel
        if e.key == pygame.K_DOWN:
            pos[1] += vel
        if e.key == pygame.K_UP:
            pos[1] -= vel

def process_input_2():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        pos[0] -= vel
    if pressed[pygame.K_RIGHT]:
        pos[0] += vel
    if pressed[pygame.K_DOWN]:
        pos[1] += vel
    if pressed[pygame.K_UP]:
        pos[1] -= vel


# MAIN LOOP
running = True
while running:

    tempo.tick(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    process_input_2()

    schermo.fill(colore_sfondo)
    pygame.draw.circle(schermo, colore_cerchio, pos, raggio_cerchio)
    pygame.display.flip()


