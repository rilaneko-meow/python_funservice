from animals import *

p = Dog("Шарик", 5)
p.gettingOlder()
print(p.name + ":", p.age, "лет")  # Выведет: Шарик: 6 лет

pets = [Cat("Мурка", 3), p]
for p in pets:
    p.say()  # Выведет: Мяу! \n Гав!
