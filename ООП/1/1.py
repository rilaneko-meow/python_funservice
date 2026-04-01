'''
Начальные значения полей можно задавать прямо при создании объекта.
Для этого нужно изменить конструктор, добавив два параметра – начальные
значения длины и ширины дороги:
'''
class TRoad: 
  def __init__ ( self, length0, width0 ):   # конструктор 
    if length0 > 0: 
      self.length = length0 
    else: 
      self.length = 0 
    if width0 > 0:   
      self.width = width0 
    else: 
      self.width = 0
'''
В этом конструкторе проверяется правильность переданных параметров,
чтобы по ошибке длина и ширина дороги не оказались отрицательными.
Теперь создавать объект будет проще:
'''
#road = TRoad ( 60, 3 ) 

class TCar:
  def __init__ ( self, road0, p0, v0 ): 
    self.road = road0
    self.P = p0
    self.V = v0
    self.X = 0

  def move ( self ):
    self.X += self.V 
    if self.X > self.road.length:
      self.X = 0         

# Основная программа
road = TRoad( 65, 3 )
car = TCar( road, 1, 10 ) 
car.move()
print ( "После 1 шага:" )
print ( car.X ) 
for i in range(10):
  car.move()
  print ( car.X ) 

N = 3
cars = []
for i in range(N):
  cars.append ( TCar(road, i+1, 2*(i+1)) )
for k in range(100):  # 100 шагов
  for i in range(N):  # для каждой машины
    cars[i].move()
print ( "После 100 шагов:" )
for i in range(N):
  print ( cars[i].X )
