#!/usr/bin/env python3

from tkinter.constants import TRUE
from graphics import update
from graphicsLayer import maxGridSize, win, AntGraphic, math
import random
import os

# Used to assign id numbers to new ants
antCount = 0
antSpeed = 1

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

  def look(self, x, y):
    dy = y - self.y()
    dx = x - self.x()
    tan = math.atan2(dy, dx)
    self.antGraphic.move(self.x(), self.y(), tan)
    
  def moveForward(self):
    dx = antSpeed * math.cos(self.angle())
    dy = antSpeed * math.sin(self.angle())
    x = self.x() + dx
    y = self.y() + dy
    if (0 < x < maxGridSize - 2 and 0 < y < maxGridSize - 2):
      self.antGraphic.move(x, y, self.angle())
    
  def wander(self):
    rand = random.random()
    if (rand < 90/100):
      self.moveForward()
    if (rand < 95/100):
      return "stayed still"
    else:
      self.antGraphic.move(self.x(), self.y(), random.uniform(0, math.pi * 2))

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

def moveAllAnts():
  for ant in antsArray:
    ant.wander()

# Testing mode where a single ant is created and moves forward in whatever direction it's facing.
# The user can click anywhere on the screen and the ant will rotate to face that location.
def testAntRotationAndMovement():
  ant = Ant(maxGridSize/2, maxGridSize/2, 0)
  while (TRUE):
    update(10)
    point = win.checkMouse()
    if (point != None):
      win.plotPixel(point.x, point.y)
      ant.look(point.x, point.y)
    ant.moveForward()

def main():
  newAnts(100)
  while(win.checkKey() != 'x'):
    moveAllAnts()
    update(60)
  win.close()

main()
#testAntRotationAndMovement()