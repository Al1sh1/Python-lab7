import os
import pygame
import keyboard
import time

pygame.mixer.init()

playlist = ['music/Rust.mp3', 'music/Seeuagain.mp3']

current_track = 0
is_playing = False


def load_track(index):
    pygame.mixer.music.load(playlist[index])
    print(f"Loaded: {playlist[index]}")


def play():
    global is_playing
    if not is_playing:
        pygame.mixer.music.play()
        is_playing = True
        print("Playing")


def pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
        print("Paused")


def stop():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("Stopped")


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    load_track(current_track)
    play()
    print("Next Track")


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    load_track(current_track)
    play()
    print("Previous Track")


load_track(current_track)


def listen_for_keys():
    while True:
        try:
            if keyboard.is_pressed('space'):
                if is_playing:
                    pause()
                else:
                    play()
                time.sleep(0.2)
            elif keyboard.is_pressed('s'):
                stop()
                time.sleep(0.2)
            elif keyboard.is_pressed('n'):
                next_track()
                time.sleep(0.2)
            elif keyboard.is_pressed('p'):
                previous_track()
                time.sleep(0.2)
        except:
            break


print("Press SPACE to Play/Pause, S to Stop, N for Next, P for Previous")
listen_for_keys()
