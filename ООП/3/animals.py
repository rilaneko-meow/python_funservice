from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, age):
        self.__name = name  # Скрытое поле для имени
        self.__age = age    # Скрытое поле для возраста

    # Свойства для чтения скрытых полей (только геттеры)
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def gettingOlder(self):
        """Увеличивает возраст питомца на 1 год."""
        self.__age += 1

    @abstractmethod
    def say(self):
        """Абстрактный метод, должен быть реализован в наследниках."""
        pass

class Mammal(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def run(self):
        """Метод для вывода сообщения о том, что животное побежало."""
        print(f"{self.name} побежал")

class Cat(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def say(self):
        """Реализация метода say для кошки — выводит 'Мяу!'"""
        print(self.name, ": Мяу!")


class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def say(self):
        """Реализация метода say для собаки — выводит 'Гав!'"""
        print(self.name, ": Гав!")

class Reptilia(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def crawl(self):
        """Метод для вывода сообщения о том, что рептилия поползла."""
        print(f"{self.name} пополз...")


class Turtle(Reptilia):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def say(self):
        """Реализация метода say для черепахи — можно оставить пустым или добавить звук."""
        print(self.name, ": Кр-кр...")


class Snake(Reptilia):
    def __init__(self, name, age):
        super().__init__(name, age)  # Вызываем конструктор родительского класса

    def say(self):
        """Реализация метода say для змеи — выводит 'Ш-ш-ш!'"""
        print(self.name, ": Ш-ш-ш!")
