class Parrot:
    def __init__ (self, phrase):
        self.phrase = phrase
    def say(self,n=1):
        for _ in range(n):
            print(self.phrase, end=' ')
        print()
    def newText(self, new_phrase):
        self.phrase = new_phrase

p = Parrot('Гав!')
p.say()
p.newText('Мяу!')
p.say(3)
