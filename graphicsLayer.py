from graphics import *
import math

# window setup
maxGridSize = 500
win = GraphWin("Ant Simulation", maxGridSize, maxGridSize, autoflush=False)
win.setBackground("light gray")

class AntGraphic:
  center = Point(0, 0)
  angle = 0.0
  polygon = Polygon()

  def __init__(self, x: int, y: int, angle: float) -> None:
    self.center = Point(x, y)
    self.angle = angle
    self.polygon = getPolygon(self.center, self.angle)
    self.polygon.draw(win)

  def __str__(self) -> str:
    return "[center: {}, angle: {}, polygon: {}]".format(self.center, self.angle, self.polygon)
  
  def move(self, x, y, angle):
    self.polygon.undraw()
    self.polygon = getPolygon(Point(x, y), angle)
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

  ant =  Polygon( #rotation
    rotate(head, center, angle),
    rotate(p1, center, angle),
    rotate(p2, center, angle),
    rotate(p3, center, angle),
    rotate(p4, center, angle)
  )
  ant.setFill("red")
  return ant

def testRotation():
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
    ant.draw(win)
    a += 1
    a = a % len(angles)
    win.getKey()
    ant.undraw()