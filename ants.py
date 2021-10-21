#!/usr/bin/env python3

from graphics import *
import random
import math
import os

maxGridSize = 500

# Used to assign id numbers to new ants
antCount = 0
# window setup
win = GraphWin("Ant Simulation", maxGridSize, maxGridSize, autoflush=False)
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
    update(30)
  win.close()

#main()

def rotate (point: Point, center: Point, angle: float) -> Point:
  s = math.sin(angle)
  c = math.cos(angle)
  px = point.x - center.x
  py = point.y - center.y
  nx = px * c - py * s
  ny = px * s + py * c
  return Point(nx + center.x, ny + center.y)

def getPolygon (center: Point, angle: float) -> Polygon:
  size = 6
  hs = 6/2
  x = center.x
  y = center.y

  head = Point(x + size, y)
  p1 = Point(x + hs, y - hs)
  p2 = Point(x - hs, y - hs)
  p3 = Point(x - hs, y + hs)
  p4 = Point(x + hs, y + hs)

  return Polygon( #rotation
    rotate(head, center, angle),
    rotate(p1, center, angle),
    rotate(p2, center, angle),
    rotate(p3, center, angle),
    rotate(p4, center, angle)
  )

angles = [
  0,
  math.pi / 6,
  math.pi / 4,
  math.pi / 3,
  math.pi / 2,
  math.pi * 2/3,
  math.pi * 3/4,
  math.pi * 5/6,
  math.pi,
  math.pi * 7/6,
  math.pi * 5/4,
  math.pi * 4/3,
  math.pi * 3/2,
  math.pi * 5/3,
  math.pi * 7/4,
  math.pi * 11/6
]
center = Point(50, 50)
a = 0

while(True): 
  ant = getPolygon(center, angles[a])
  ant.setFill("red")
  ant.draw(win)
  a += 1
  a = a % len(angles)
  win.getKey()
  ant.undraw()

