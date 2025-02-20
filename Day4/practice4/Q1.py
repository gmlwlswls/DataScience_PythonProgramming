"""
Q1. Cartesian Plane
Write two classes `Point` and `Line`.
- `Line` has `slope` method that returns the slope of the line
- `Line` has `length` method that returns the length of the line

"""


# 1.
from math import sqrt

class Point :
  def __init__(self, X , y ) -> None :
    self.X = X
    self.y = y
  
class Line :
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2
    
  def slope(self) :
    return (self.point2.y - self.point1.y) / (self.point2.X - self.point1.X)

  def length(self) :
    return sqrt((self.point2.y - self.point1.y) ** 2 + (self.point2.X - self.point1.X) ** 2)
  
line= Line(Point(1,1), Point(3,2))
print('Slope :', line.slope(),'/Expected : 0.5')
print('Length :', line.length(),'/Expected : 2.23606797759979')
    