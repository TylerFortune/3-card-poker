#playing card
import random

# <--CLASS DEFINITIONS-->
class Card:    
    def __init__(self,s,v):
        
        if (s=="spades"):
            self.suit="\u2660"
        elif (s=="hearts"):
            self.suit="\u2661"
        elif (s=="diamonds"):
            self.suit="\u2662"
        elif (s=="clubs"):
            self.suit="\u2663"
        
        self.value = v
      
            
            
    def __gt__(self, other):
        #other must be another object of Card type
        if(self.value == 1): #Ace 
            myValue = 14
        else:
            myValue = self.value
            
        if(other.value == 1): #Ace
            otherValue = 14
        else:
            otherValue = other.value
            
       
        #if values are the same compairs suit type
        if(myValue == otherValue):
            if (self.suit == "spades"):
                me = 4
            elif (self.suit == "hearts"):
                me = 3
            elif (self.suit == "diamonds"):
                me = 2
            else:
                me = 1
            
            if (other.suit == "spades"):
                you = 4
            elif (other.suit == "hearts"):
                you = 3
            elif (other.suit == "diamonds"):
                you = 2
            else:
                you = 1
            
            
            if (me > you):
                return True
            else:
                return False
            
            #return me > you                                    
        
        else:
            return myValue > otherValue
    

          
    def display(self):
        if(self.value ==1):
            s = "A"
        elif(self.value ==11):
            s = "J"
        elif(self.value ==12):
            s = "Q"
        elif(self.value ==13):
            s = "K"
        else:
            s = self.suit
        print("[", s , self.value,"]",sep='')
        
class Deck:
    def __init__(self):
        self.cards = [None] *52
        
        for i in range(0, 13, 1):
            self.cards[i] = Card("spades", i+1)
        for i in range(13, 26, 1):
            self.cards[i] = Card("hearts", i-12)
        for i in range(26, 39, 1):
            self.cards[i] = Card("clubs", i-25)
        for i in range(39, 52, 1):
            self.cards[i] = Card("diamonds", i-38)
       
        #set the "top" of the deck
        self.top = 0
        
    def displayDeck(self):
        
        print("-----------------------------")
        for i in range(self.top):
            if(i == self.top):
                print("------TOP--------")
            self.cards[i].display()
        print("-----------------------------")

    def shuffle(self):
        #self.cards is an array of Card objects
        for i in range(100):
            idx1 = random.randint(0,51)
            idx2 = random.randint(0,51)
            
            temp = self.cards[idx1]
            self.cards[idx1] = self.cards[idx2]
            self.cards[idx2] = temp
            
            #resets "top"
            self.top = 0
            
    def dealCard(self):
        #sets top to next card in deck 
        #returns previous card
        self.top = self.top +1
        return self.cards[self.top-1]
    

class Player:    
    def __init__(self, money, name):
        self.name = name
        self.wallet = money
        self.cards = [None] * 3 
        self.num_cards = 0
    def showHand(self):
        print("--------", self.name, "-------:", self.wallet)
        
        for i in range(self.num_cards):
            self.cards[i].display()
        print("---------------")
    
    def getCard(self, card):
        self.cards[self.num_cards] = card
        self.num_cards = self.num_cards+1
        
    # def score(self):
    #     if(self.cards[0] == self.cards[1] and self.cards[1] == self.cards[2]):
    #         pts = 1000
    #     elif(self.cards[])
    # def __gt__(self,other):
    #     if()
        
# <--FUNCTION DEFINITIONS-->
        
# <--MAIN FUNCTION-->
def main():
    deck = Deck()
    deck.shuffle()
    
    player1 = Player("Tyler", 10000)
    
    player2 = Player("computer", 100)
    
# <-- MAIN PROGRAM -->
main()




    

    






