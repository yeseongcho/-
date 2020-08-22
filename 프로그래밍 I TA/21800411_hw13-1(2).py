from cs1graphics import*
import random
import time

#main function
def main():
    table=Table() 
    deck=Deck()   
    deck.shuffle()
    #4쌍의 카드 패를 만들어 분배(1패당 5장씩) 
    hands=deck.deal_hands(4,5)   
    for i in range(4):
        #show each label on table: player1, player2,,
        table.show_label(i,hands[i])
        #show each player's 패 on table
        hands[i].show_cards(table)     
        time.sleep(1)
    table.clear()


#create table(background canvas)    
class Table:
    def __init__(self):
        #create canvas
        self.canvas= Canvas(1000,600,"dark green","BlackJack")
        #첫번째 카드 패의 첫번째 위치 
        self.x0=250
        self.y0=80
        self.depth0=50

        self.delta_x=50 #가로방향으로 50씩 카드 위치 바꿈  
        self.delta_d=-5 #depth는 -5씩 빼서 점점 카드가 위로 쌓이는 느낌으로 

        #현재 table이 참조하고 있는 위치 
        self.x=self.x0
        self.y=self.y0
        self.d=self.depth0
        self.images=[]# 카드들의 image object들을 저장하기 위한 리스트 

    #카드를 x,y,d 위치로 보낸다음에 캔버스에 보여줌 
    def display_card(self,card,x,y,d):  #card는 card class의 object
        image= card.image  #card object에 image라는 attribute있음 
        self.images.append(image) #카드를 images 리스트에 등록시킴 
        image.setDepth(d)
        image.moveTo(x,y)  #이미지를 캔버스의 x,y위치로 이동 
        self.canvas.add(image)  #이미지를 캔버스에 추가시키면 캔버스 위에서 보임 
        time.sleep(1)

    #hand를 where 위치에서 show message    
    def show_label(self,where,hand):
        text=Text()
        y=self.y0+where*120
        text.setFontColor("white")
        text.setFontSize(20)
        text.moveTo(100,y)
        self.canvas.add(text)
        text.setMessage(hand.label)

    #increment y by 120    
    def increment_y(self):
        self.y+=120

    #remoce images from canvas
    def clear(self):
        for image in self.images:
            self.canvas.remove(image)
        #initialize table
        self.x=self.x0
        self.y=self.y0
        self.images=[]

#create a cad
class Card:
    suit_names=["clubs", "diamonds", "hearts", "spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self,suit=0,rank=1):
        self.suit = suit 
        self.rank = rank
        rank_name=Card.rank_names[rank]
        suit_name=Card.suit_names[suit]
        #get image
        self.image=Image("./BlackJack/"+suit_name+"_"+rank_name+".png")
    def __str__(self) :
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return "%s of %s" % (rank_name, suit_name)
    def __lt__(self, other) :
        if self.suit < other.suit :
            return True
        if self.suit > other.suit :
            return False
        if self.rank < other.rank :
            return True
        return False
        

#create deck of 52 cards        
class Deck:
    #show cards on the table
    def __init__(self):
        self.cards = []
        #put 52 cards in self.cards
        for suit in range(4): 
            for rank in range(1, 14): 
                card = Card(suit, rank) 
                self.cards.append(card)

    def __str__(self):
        res = []
        #put 52 cards in res
        for card in self.cards: 
            res.append(str(card)) 
        return "\n".join(res)
    
    #remove a card
    def pop_card(self):    
        return self.cards.pop()
    
    #add a card
    def add_card(self, card): 
        self.cards.append(card)
        
    #shuffle cards
    def shuffle(self):   
        random.shuffle(self.cards)

    #num of hands만큼 distribute num of cards 
    def deal_hands(self,num_hands,num_cards):
        hands = []
        for i in range(num_hands): 
            hand = Hand()
            #move num of cards from deck to hand
            self.move(hand, num_cards)
            hands.append(hand)  
        return hands
    
    
    #move num of cards from deck to hand
    def move(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    #show cards on table       
    def show_cards(self,table):
        x=table.x0
        y=table.y
        d=table.depth0
        for card in self.cards:
            table.display_card(card,x,y,d)
            x+=table.delta_x
            d+=table.delta_d
        #move down to next line
        table.increment_y()


#create a 패 for a player
class Hand(Deck):
    def __init__(self, label=" "):
        self.cards = [] 
        self.label = label
        
    #print label
    def print_label(self):
        print (self.label)
        

#call main function
main()
