class Parrot:
    def __init__ (self, phrase):
        self.phrase = phrase
    def say(self):
        print(self.phrase)
    def newText(self, new_phrase):
        self.phrase = new_phrase

p = Parrot('Гав!')
p.say()
p.newText('Мяу!')
p.say()
    
