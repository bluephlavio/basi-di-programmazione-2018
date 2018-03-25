import pygame

# COLORI
colore_sfondo = (3, 4, 43)
colore_cerchio = (232, 119, 20)

# IMMAGINI
icona = pygame.image.load('img\icon.jpg') # carica l'icona
icona = pygame.transform.smoothscale(icona, (32, 32)) # modifica le dimensioni a 32 x 32 pixels

# DIMENSIONI
larghezza = 640
altezza = 480
dimensioni = (larghezza, altezza)
raggio_cerchio = 10

# POSIZIONI E VELOCITA'
vel = 5
pos = [larghezza//2, altezza//2]

# SCHERMO
pygame.display.set_mode(dimensioni, pygame.RESIZABLE) # crea la finestra
pygame.display.set_caption('Controller') # imposta il titolo
pygame.display.set_icon(icona) # imposta l'icona
schermo = pygame.display.get_surface()

# INPUT
def movimento(): # calcola lo spostamento
    tasti = pygame.key.get_pressed()
    dx, dy = 0, 0
    if tasti[pygame.K_LEFT]:
        dx -= vel
    if tasti[pygame.K_RIGHT]:
        dx += vel
    if tasti[pygame.K_DOWN]:
        dy += vel
    if tasti[pygame.K_UP]:
        dy -= vel
    return dx, dy

# TEMPO
tempo = pygame.time.Clock()

# MAIN LOOP
running = True
while running:

    tempo.tick(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.VIDEORESIZE:
            # Gestisce il cambiamento di dimensione della finestra
            dimensioni = e.size # legge le nuove dimensioni dall'evento generato dall'utente
            pygame.display.set_mode(dimensioni,pygame.RESIZABLE) # reimposta lo schermo con le nuove dimensioni
            schermo = pygame.display.get_surface()

    # Calcola la nuova posizione dell'oggetto
    ds = movimento()
    dx = ds[0]
    dy = ds[1]
    pos[0] += dx
    pos[1] += dy

    # Disegna la scena
    schermo.fill(colore_sfondo)
    pygame.draw.circle(schermo, colore_cerchio, pos, raggio_cerchio)
    pygame.display.flip()


