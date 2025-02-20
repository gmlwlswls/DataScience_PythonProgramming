# 4. 

class Point :
  def __init__(self, X , y ) -> None :
    self.X = X
    self.y = y
  
  def __str__(self): 
    # 객체를 print()에서 부를때 정의된 문자열이 호출되는 특수 메서드
    return f'({self.X}, {self.y})'
  
  def __add__(self, point) :
    return (self.X + point.X, self.y + point.y)
  
  def __sub__(self, point) :
    return (self.X - point.X, self.y - point.y)
  
  def __mul__(self, point) :
    return (self.X * point.X, self.y * point.y)
  
  def __truediv__(self, point) :
    return (float(self.X//point.X), float(self.y//point.y))
  
  def __neg__(self) :
    return (float(-self.X), float(-self.y))
  
  def __gt__(self, point) :
    if self.X > point.X and self.y > point.y :
      return True 
  
  def __lt__(self, point) :
    if self.X < point.X or self.y < point.y :
      return True
    
  def __call__(self) :
    return self.X + self.y

P1, P2= Point(3,4), Point(1,2)
print(P1)
print("P1:",P1, 'Expected: (3,4)') # print할때 __str__ 출력
# P1 = P1 + P2
# print(P1) # +로 reeturn되었으므로 출력o
# print("P1 = P1 + P2, P1:", P1, '/ Expected: (4,6)')

# P1 = P1 - P2
# print("P1 = P1 - P2, P1 :", P2, '/ Expected: (3,4)')

# P1 = P1 * P2
# print('P1 = P1 * P2, P1 :', P1, '/ Expected: (3,8)')

P1 = P1 / P2
print('P1 = P1 / P2, P1:', P1, '/ Expected: (3.0, 2.0)')

# P1 = -P1
# print('P1 = -P1, P1:', P1, '/ Expected: (-3.0, -4.0)')

# print('P1 > P2:', P1>P2, '/ Expected: False')
# print('P1 < P2:', P1 < P2, '/ Expected: True')
# print('P2():', P2(), '/ Expected: 3')

# 클래스를 정의할 때 print() 대신 __str__(self)
# ** __repr__은 잘 모르겠지만
# __repr__(self)는 eval()을 사용하여 객체를 사용할 수 있도록 재정의
# __str__(self)가 정의되어 있지 않으면 default로 __repr(self)가 호출됨됨
