import pickle
import pygame
filename = 'dean.pkl'
cookies = 0
# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 1

## load da file
try:
    with open(filename ,'rb') as file:
        data = pickle.load(file)
        print (data)
        cookies = int(data)
except (OSError,pickle.PickleError):
    print ('fout')

cookie_pos = pygame.Rect((screen.get_width() / 2)-100, (screen.get_height() / 2) - 100,200,200)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.draw.rect(screen,(139,69,19), cookie_pos, border_radius=200)
    pygame.mouse.get_pressed(num_buttons=3)
    if event.type == pygame.MOUSEBUTTONDOWN:
        print ("bob")
        mouse_pos = event.pos
        if cookie_pos.collidepoint(mouse_pos):
            print ("click")
            cookies += 1


    text_surface = font.render(f"score:{cookies}", True, (0, 0, 0))
    screen.blit(text_surface, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


try:
    with open(filename, 'wb') as file:
        pickle.dump(cookies,file, protocol=pickle.HIGHEST_PROTOCOL)
except (OSError, pickle.PickleError) as e:
    print ('fout')