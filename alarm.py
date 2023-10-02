import pygame

pygame.mixer.init()

def p_play():

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    pygame.time.delay(100)


def p_stop():

    pygame.mixer.music.stop()  # Stop the song
    pygame.quit()
