# This is intended to get pygame running in my CLI environment
# Following tutorial at nerdparadise.com: PyGame Tutorial

import pygame
import os

imageLibrary = {}


# if the image has already been loaded, this will return that image
#   if it has not been loaded, this will load it and return it
def getImage(path):
  global imageLibrary
  image = imageLibrary.get(path)
  if image == None:
    canonicalizedPath = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalizedPath)
    imageLibrary[path] = image

  # scales image 
  image = pygame.transform.scale(image, (100, 100))

  return image
# end getImage

pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False
isBlue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      isBlue = not isBlue
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: y -= 3
  if pressed[pygame.K_DOWN]: y += 3
  if pressed[pygame.K_LEFT]: x -= 3
  if pressed[pygame.K_RIGHT]: x += 3
  if pressed[pygame.K_q]: done = True # quits when Q is pressed

  screen.fill((0, 0, 0))
  if isBlue: color = (0, 128, 255)
  else: color = (255, 100, 0)
  pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

  screen.blit(getImage('assets/ball.png'), (20, 20))

  pygame.display.flip()
  clock.tick(60)

