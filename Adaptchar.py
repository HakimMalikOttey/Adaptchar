import os, sys
import pygame
from chatterbot import ChatBot
from pygame.locals import *
screen = pygame.display.set_mode((400,300))
background = pygame.image.load("grass.jpg")
comp1 = pygame.image.load('red.png').convert()
comp2 = pygame.image.load('red.png').convert()
comp3 = pygame.image.load('red.png').convert()
comp4 = pygame.image.load('red.png').convert()
enemy = pygame.image.load('black.jpg').convert()
pygame.init()
done = False
clock = pygame.time.Clock()
while not done:
    comp1 = pygame.transform.scale(comp1, (35, 35))
    comp2 = pygame.transform.scale(comp2, (35, 35))
    comp3 = pygame.transform.scale(comp3, (35, 35))
    comp4 = pygame.transform.scale(comp4, (35, 35))
    enemy = pygame.transform.scale(enemy, (150, 150))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    screen.blit(background,(0,0))
    screen.blit(comp1,(50,50))
    screen.blit(comp2, (50,100))
    screen.blit(comp3, (50, 150))
    screen.blit(comp4, (50, 200))
    screen.blit(enemy, (200,70))
    pygame.display.flip()
    clock.tick(60)