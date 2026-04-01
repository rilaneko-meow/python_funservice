class Parrot:
    def __init__ (self, phrase):
        self.phrase = phrase
    def say(self):
        print(self.phrase)

p1 = Parrot('Гав!')
p2 = Parrot('Мяу!')
p1.say()
p2.say()

    
