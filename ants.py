#!/usr/bin/env python3

from graphics import *
import random
import os

maxGridSize = 500

# Used to assign id numbers to new ants
antCount = 0
# window setup
win = GraphWin("Ant Simulation", maxGridSize, maxGridSize)
win.setBackground("light gray")

class Ant:
  id = 0
  circle = None

  def __init__(self, x, y):
    self.circle = Circle(Point(x,y), 3).draw(win)
    self.circle.setFill("red")
    global antCount
    self.id = antCount
    antCount += 1
  
  def __str__(self) -> str:
    return "Ant #{}: {}".format(self.id, self.circle.getCenter())

  @classmethod
  def random(self):
    return Ant(random.randint(0,maxGridSize-1), random.randint(0,maxGridSize-1))

  def move(self):
    dir = random.randint(1,5)
    center = self.circle.getCenter()
    if (dir == 1 and center.getX() < maxGridSize-1):
      self.circle.move(1, 0)
      return "right"
    elif (dir == 2 and center.getX() > 0):
      self.circle.move(-1, 0)
      return "left"
    elif (dir == 3 and center.getY() < maxGridSize-1):
      self.circle.move(0, 1)
      return "down"
    elif (dir == 4 and center.getY() > 0):
      self.circle.move(0, -1)
      return "up"
    else:
      return "stayed"

# Array of all ants that exist
antsArray = []

def newAnt():
  antsArray.append(Ant.random())

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
  win.close()

main()