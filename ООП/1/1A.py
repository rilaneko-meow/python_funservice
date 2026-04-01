class Parrot:
    def __init__ (self, phrase = 'Привет, друзья!'):
        self.phrase = phrase
    def say(self):
        print(self.phrase)

p = Parrot()
p.say()

    
