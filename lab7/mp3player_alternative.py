import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

music_folder = "C:/Users/AQNIET/Desktop/labs/lab7/music/"
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def toggle_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

button_width, button_height = 120, 50
spacing = 20
start_x = (500 - (4 * button_width + 3 * spacing)) // 2
start_y = 300

buttons = {
    "Prev": pygame.Rect(start_x, start_y, button_width, button_height),
    "Play/Pause": pygame.Rect(start_x + (button_width + spacing), start_y, button_width, button_height),
    "Stop": pygame.Rect(start_x + 2 * (button_width + spacing), start_y, button_width, button_height),
    "Next": pygame.Rect(start_x + 3 * (button_width + spacing), start_y, button_width, button_height)
}

if playlist:
    play_music()

running = True
while running:
    screen.fill((255, 255, 255))
    for text, rect in buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect, border_radius=10)
        label = font.render(text, True, (0, 0, 0))
        text_rect = label.get_rect(center=rect.center)
        screen.blit(label, text_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["Play/Pause"].collidepoint(event.pos):
                toggle_pause()
            elif buttons["Stop"].collidepoint(event.pos):
                stop_music()
            elif buttons["Next"].collidepoint(event.pos):
                next_track()
            elif buttons["Prev"].collidepoint(event.pos):
                prev_track()

pygame.quit()
