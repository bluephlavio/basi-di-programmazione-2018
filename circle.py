import pygame

# DIMENSIONI
dimensioni = (640, 480) # larghezza e altezza (in pixels)
raggio_cerchio = 10 # raggio del cerchio (in pixels)

# COLORI
# (0, 0, 0) -> nero
# (255, 255, 255) -> bianco
# (255, 0, 0) -> rosso
# (0, 255, 0) -> verde
# (0, 0, 255) -> blu
colore_sfondo = (0, 0, 0) # sfondo
colore_cerchio = (255, 255, 255) # cerchio

# POSIZIONE
# (0, 0) -> angolo in alto a sinistra
# (640, 480) -> angolo in basso a destra
x = int(input('Inserisci la coordinata x: ')) # coordinata x (in pixels)
y = int(input('Inserisci la coordinata y: ')) # coordinata y (in pixels)
posizione = (x, y) # tupla (lista) con le coordinate x e y

# Crea la finestra con le dimensioni richieste
screen = pygame.display.set_mode(dimensioni) 

# Crea una variabile booleana per controllare se il programma 
# deve continuare l'esecuzione o uscire
running = True

# Main loop
while running:

    # Processa gli eventi in input e prende le relative decisioni
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    # Pulisce lo schermo con un colore
    screen.fill(colore_sfondo)
    # Disegna il cerchio nella posizione richiesta
    pygame.draw.circle(screen, colore_cerchio, posizione, raggio_cerchio)
    # Manda a schermo il disegno finale
    pygame.display.flip()
