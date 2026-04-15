#!/usr/bin/env python3

import time
import pygame

pygame.init()

print("""
Type in the amount of seconds you want your timer to go on for!
""")

timer = int(input())

noise = pygame.mixer.Sound('extremely-loud-correct-buzzer.mp3')

while True:
	timer = timer - 0.1
	time.sleep(0.1)
	if timer <= 0:
		break
print("timer done!")
noise.play()
time.sleep(2.5)
