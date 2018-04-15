import cards

class Players:

    def __init__(self):
        try:
            self.numofPlayers = int(input("How many players are there? "))
        except ValueError:
            print("Please enter a valid number!")
        while self.numofPlayers < 2:
            self.numofPlayers = int(input("You need at least 2 players!: "))
        self.names = []
        for i in range(self.numofPlayers):
            x = input("Player %d name (Please input unique names): "  % (i+1))
            self.names.append(x)
    
    def playervalues(self):
        playerdict = {}
        for names in self.names:
            playerdict[names] = 0
        return playerdict

class GameSetup:
    
    def __init__(self):
        SDeck = cards.Deck()
        self.RandDeck = SDeck.shuffle()
    
    def cardassign(self):
        two = [self.RandDeck.pop(), self.RandDeck.pop()]
        return two
        
    def hit(self):
        one = self.RandDeck.pop()
        return one
    
def main():

    inv_values = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    
    p = Players()
    playerdict = p.playervalues()
    numofP = p.numofPlayers
    names = p.names
    
    g = GameSetup()
    
    
    for n in names:
        assign = g.cardassign()
        playerdict[n] = inv_values[assign[0][0]] + inv_values[assign[1][0]]
        print(n, ",this is the hand dealt to you: ", assign)
    print("\nThe sum of your hands: ", playerdict)

    for n in names:
        hitchoice = "y"
        print("\nIt is your turn, ", n)
        while playerdict[n] < 21 and hitchoice == 'y':
            print("\nYour hand: ", playerdict[n])
            hitchoice = input("hit? (y/n): ")
            while hitchoice != 'y' and hitchoice != 'n':
                hitchoice = input("You need to enter a 'y' or 'n'!: ")
            if hitchoice == 'y':
                h = g.hit()
                playerdict[n] += inv_values[h[0]]
            elif hitchoice == 'n':
                print("Your final hand: ", playerdict[n])
        if playerdict[n] > 21:
            print("Your hand: ", playerdict[n], "\nBust!")
        elif playerdict[n] == 21:
            print("Blackjack!")
    
    winnerscore = 0
    busts = []
    losers = []
    winner = []
    sortNames = sorted(playerdict, key = playerdict.__getitem__, reverse = True)
    sortValues = sorted(playerdict.values(), reverse = True)
    gameoutcomedict = {k:v for (k,v) in zip(sortNames,sortValues)}
    
    for n in sortNames:
        if gameoutcomedict[n] > winnerscore and gameoutcomedict[n] <= 21:
            winnerscore = gameoutcomedict[n]
            winner = [n]
        elif gameoutcomedict[n] == winnerscore:
            winner.append(n)
        elif gameoutcomedict[n] > 21:
            busts.append(n)
        else:
            losers.append(n)
    
        
    if len(winner) == 1:
        print("\nThe winner is,", winner[0], "!")
        print("Loser(s): ", ', '.join(losers))
        print("Bust(s): ", ', '.join(busts))
    else:
        print("\nThe game resulted with no direct winners!:")
        print("Tied: ", ', '.join(winner))
        print("Loser(s): ", ', '.join(losers))
        print("Bust(s): ", ', '.join(busts))
            
   
main()
    

    


