# 3. 

class Pokemon :
  def __init__(self, name, type, hp):
    self.name= name
    self.type= type
    self.hp = hp
  
  def getName(self) :
    return self.name
  
  def getHp(self) :
    return self.hp
  
  def getType(self) :
    return self.type
  
  def decreaseHp(self, amount) :
    self.hp= amount
  
  def cry(self) :
    print(f'{self.getName()} cries')
  
  def attack(self, opponent):
    print(f'{self.name} attacks {opponent.getName()}!')

class Pikachu(Pokemon) :
  def __init__(self):
    self.name= 'Pikachu'
    self.type= 'ELECTRIC'
    self.hp= 100
    self.elecLV= 10
      
  def attack(self, opponent) :
    opponent.hp= opponent.hp - self.elecLV * 0.5
    return opponent.hp
  
  def cry(self) :
    print('Pika Pika!')

class Charmander(Pokemon) :
  def __init__(self):
    self.name= 'Charmander'
    self.type= 'FLAME'
    self.hp= 200
    self.frameLV= 5
    
  def attack(self, opponent) :
    opponent.hp = opponent.hp - self.frameLV * 2

pikachu= Pikachu()
charmander = Charmander()
print("Pikachu's hp:", pikachu.getHp(), '/ Expected: 100')
print("Pikachu's name:", pikachu.getName(), '/ Expected: Pikachu')
print("Pickachu's type:", pikachu.getType(), '/Expected: ELECTRIC' )
pikachu.cry()
print(' / Expected: Pika Pika!')

print("Charmander's hp:", charmander.getHp(), '/ Expected: 200')
pikachu.attack(charmander)
print('Pikachu attacks Charmander')
print("Charmander's hp:", charmander.getHp(), '/Expected: 195.0')

print("Pikachu's hp:", pikachu.getHp(), '/ Expected: 100')
charmander.attack(pikachu)
print('Charmander attacks Pikachu')
print("Pikachu's hp:", pikachu.getHp(), '/ Expected: 90')