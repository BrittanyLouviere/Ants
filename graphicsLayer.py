from graphics import *
import math
import random

# window setup
maxGridSize = 500
win = GraphWin("Ant Simulation", maxGridSize, maxGridSize, autoflush=False)
win.setBackground("light gray")

class AntGraphic:
  center = Point(0, 0)
  angle = 0.0
  polygon = Polygon()
  color = color_rgb(0, 0, 0)

  def __init__(self, x: int, y: int, angle: float) -> None:
    self.center = Point(x, y)
    self.angle = angle
    rand_color = random.choices(range(256), k=3)
    self.color = color_rgb(rand_color[0], rand_color[1], rand_color[2])
    self.polygon = getPolygon(self.center, self.angle, self.color)
    self.polygon.draw(win)

  def __str__(self) -> str:
    return "[center: {}, angle: {}]".format(self.center, self.angle)
  
  def move(self, x, y, angle):
    self.center = Point(x, y)
    self.angle = angle
    self.polygon.undraw()
    self.polygon = getPolygon(Point(x, y), angle, self.color)
    self.polygon.draw(win)
  
  def x (self):
    return self.center.x
  
  def y (self):
    return self.center.y
  
  def getAngle (self):
    return self.angle

def rotate (point: Point, center: Point, angle: float) -> Point:
  s = math.sin(angle)
  c = math.cos(angle)
  dx = point.x - center.x
  dy = point.y - center.y
  nx = dx * c - dy * s
  ny = dx * s + dy * c
  return Point(nx + center.x, ny + center.y)

def getPolygon (center: Point, angle: float, color) -> Polygon:
  size = 6
  hs = 6/2
  x = center.x
  y = center.y

  head = Point(x + size, y)
  p1 = Point(x + hs, y - hs)
  p2 = Point(x - hs, y - hs)
  p3 = Point(x - hs, y + hs)
  p4 = Point(x + hs, y + hs)

  ant =  Polygon( #rotation
    rotate(head, center, angle),
    rotate(p1, center, angle),
    rotate(p2, center, angle),
    rotate(p3, center, angle),
    rotate(p4, center, angle)
  )
  ant.setFill(color)
  return ant
