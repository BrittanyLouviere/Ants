#!/usr/bin/env python3

import random
import os

maxGridSize = 10

class Location:
  x = 0
  y = 0

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "({}, {})".format(self.x, self.y)

  @classmethod
  def random(self):
    return Location(random.randint(0,maxGridSize-1), random.randint(0,maxGridSize-1))

# Used to assign id numbers to new ants
antCount = 0

class Ant:
  id = 0
  location = Location(0,0)

  def __init__(self, location):
    self.location = location
    global antCount
    self.id = antCount
    antCount += 1
  
  def __str__(self) -> str:
    return "Ant #{}: {}".format(self.id, self.location)

  @classmethod
  def random(self):
    return Ant(Location.random())

  def move(self):
    dir = random.randint(1,5)
    if (dir == 1 and self.location.x < maxGridSize-1):
      self.location.x += 1
      return "right"
    elif (dir == 2 and self.location.x > 0):
      self.location.x -= 1
      return "left"
    elif (dir == 3 and self.location.y < maxGridSize-1):
      self.location.y += 1
      return "down"
    elif (dir == 4 and self.location.y > 0):
      self.location.y -= 1
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

def printWorld():
  #sorted = antsArray.sort(key=sortX)
  for y in range(0, maxGridSize):
    row = ""
    for x in range(0, maxGridSize):
      found = " . "
      for ant in antsArray:
        if (ant.location.x == x and ant.location.y == y):
          found = " {} ".format(ant.id)
          break
      row += found
    print(row)



# Main code
userInput = ""
os.system('clear')
newAnts(5)
printWorld()
print()
printAllAnts()
userInput = input("Input: ")

while (userInput != "x" and userInput != "X"):
  if (userInput == "c" or userInput == "C"):
    printAntCount()
    userInput = input("Input: ")
  else:
    moveAllAnts()
    os.system('clear')
    printWorld()
    print()
    printAllAnts()
    userInput = input("Input: ")