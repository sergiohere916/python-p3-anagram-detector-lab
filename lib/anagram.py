# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list):
        return [word for word in list if sorted(word.upper()) == sorted(self.word.upper())]

Listen = Anagram("listen")
print(Listen.match(["enlists", "google", "fatty", "inlets"]))
