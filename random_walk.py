import pygame
import random
import math

# DIMENSIONI
larghezza = 640
altezza = 480
dimensioni = (larghezza, altezza)
raggio_cerchio = 30
diametro_cerchio = raggio_cerchio * 2

# COLORI e IMMAGINI
colore_sfondo = (255, 255, 255)
colore_cerchio = (0, 0, 0) # Sostituito da immagine
# Carica l'icona da file esterno
icona = pygame.image.load('img\icon.jpg')
# Carica l'immagine del cerchio da file esterno
immagine = pygame.image.load('img\star.png')
# Ridimensiona l'immagine
immagine = pygame.transform.smoothscale(immagine, (diametro_cerchio, diametro_cerchio))

# Calcola il colore in base alle coordinate del cerchio
def colore(x, y):
    x_centro = larghezza//2
    y_centro = altezza//2
    R = math.sqrt(x_centro**2 + y_centro**2)
    delta_x = x - x_centro
    delta_y = y - y_centro
    r = math.sqrt(delta_x**2 + delta_y**2)
    rosso = 200
    verde = 150
    blu = min(100, int(100 * r / R))
    return (rosso, verde, blu)

# DIREZIONI
direzioni = ['SINISTRA', 'DESTRA', 'ALTO', 'BASSO']

# VELOCITA'
velocità = int(input('Inserisci la velocità del random walk: '))

# Crea la finestra
schermo = pygame.display.set_mode(dimensioni)
# Imposta il titolo della finestra
pygame.display.set_caption('Random Walk')
# Imposta l'icona della finestra
pygame.display.set_icon(icona)

# Inizializza le coordinate del cerchio nel centro della finestra
x = larghezza//2
y = altezza//2

running = True

# MAIN LOOP
while running:

    # Processa gli eventi di input e gestisce le azioni da eseguire
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # Scegli una direzione dalla lista direzioni
    direzione = random.choices(direzioni)[0]
    if direzione == 'SINISTRA':
        x -= velocità
    elif direzione == 'DESTRA':
        x += velocità
    elif direzione == 'ALTO':
        y -= velocità
    elif direzione == 'BASSO':
        y += velocità

    posizione = (x - raggio_cerchio, y - raggio_cerchio) # posizione dell'immagine (vertice in alto a sinistra)
    colore_sfondo = colore(posizione[0], posizione[1]) # calcola il colore dello sfondo

    schermo.fill(colore_sfondo) # pulisce lo schermo
    schermo.blit(immagine, posizione) # stampa l'immagine
    pygame.display.flip() # manda il risultato in output

    
