import random

class Card:
    
    values = {1:"Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}
    suits = {"C": "Clover", "D": "Diamond", "H": "Heart", "S": "Spade"}
    
    def __init__(self, value, suit):
        self.value = self.values[value]
        self.suit = self.suits[suit]
        
    def __str__(self):
        return self.value + " of " + self.suit + "s"
    
    def getValue(self):
        return self.value
        
    def getSuit(self):
        return self.suit
        
class Deck:

    def __init__(self):
        self.numofcards = 52
        
    
    def ordered(self):
        nonshuffle = []
        for i in range(1, 14):
            for j in "CDHS":
                x = Card(i, j)
                nonshuffle.append((x.value, x.suit))
        return nonshuffle
        
    
    def shuffle(self):
        shuffled = self.ordered()
        random.shuffle(shuffled)
        return shuffled

        
        
