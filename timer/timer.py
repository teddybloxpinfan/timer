#!/usr/bin/env python3

import time
import pygame
import os

pygame.init()

print("""
Type in the amount of seconds you want your timer to go on for!
""")

timer = int(input())

noise = pygame.mixer.Sound('extremely-loud-correct-buzzer.mp3')

def clear():
	os.system('clear')

#timer stuff
while True:
	timer = timer - 0.1
	time.sleep(0.1)
	print("you have " + str(timer) + "time left!")
	clear()
	if timer <= 0:
		break

noise.play()
time.sleep(2.5)
