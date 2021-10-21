#!/usr/bin/env python3

from graphicsLayer import maxGridSize, win, AntGraphic, math
import random
import os

# Used to assign id numbers to new ants
antCount = 0

class Ant:
  id = 0
  antGraphic = None

  def __init__(self, x, y, angle):
    global antCount
    self.id = antCount
    antCount += 1
    self.antGraphic = AntGraphic(x, y, angle)
  
  def __str__(self) -> str:
    return "Ant #{}: {} ".format(self.id, self.antGraphic)

  def x (self):
    return self.antGraphic.x()

  def y (self):
    return self.antGraphic.y()

  def angle (self):
    return self.antGraphic.getAngle()

  @classmethod
  def random(self):
    return Ant(random.randint(0, maxGridSize-1), random.randint(0, maxGridSize-1), random.uniform(0, math.pi * 2))

  def move(self):
    dir = random.randint(1,5)
    if (dir == 1 and self.x() < maxGridSize-1):
      self.antGraphic.move(self.x() + 1, self.y(), self.angle())
      return "right"
    elif (dir == 2 and self.x() > 0):
      self.antGraphic.move(self.x() - 1, self.y(), self.angle())
      return "left"
    elif (dir == 3 and self.y() < maxGridSize-1):
      self.antGraphic.move(self.x(), self.y() + 1, self.angle())
      return "down"
    elif (dir == 4 and self.y() > 0):
      self.antGraphic.move(self.x(), self.y() - 1, self.angle())
      return "up"
    else:
      return "stayed"

# Array of all ants that exist
antsArray = []

def newAnt():
  ant = Ant.random()
  antsArray.append(ant)
  return ant

def newAnts(number):
  for x in range(number):
    newAnt()

def printAntCount():
  print("Number of Ants:", len(antsArray))

def printAllAnts():
  for ant in antsArray:
    print(ant)

def moveAndPrintAnt(id):
  dir = antsArray[id].move()
  if (dir == "stayed"):
    print("Ant #{} stayed at \t{}".format(id, antsArray[id].location))
  else:
    print("Ant #{} moved {} to \t{}".format(id, dir, antsArray[id].location))

def moveAllAnts():
  for ant in antsArray:
    ant.move()

def main():
  newAnts(10)
  while(win.checkKey() != 'x'):
    moveAllAnts()
    #update(30)
  win.close()

main()
#testRotation()