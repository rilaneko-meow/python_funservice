import random

class Parrot:
    def __init__ (self, phrase):
        self.phrases = [phrase]
    def say(self,n=1):
        for _ in range(n):
            random_phrase = random.choice(self.phrases)
            print(random_phrase, end=' ')
        print()
    def learn(self, new_phrase):
        self.phrases.append(new_phrase)

p = Parrot('Гав!')
p.say()
p.learn('Мяу!')
p.say()
p.say(3)
