"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 Player 4명이 임의로 카드를 뽑아 그 카드 목록을 print해주는 함수입니다.
"""


 
import random
import time


# 카드 생성
class Card :
    # Card class variable
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self, suit=0, rank=1) :
        # Deck에서 카드 리스트를 만들기 위해 사용되어지는 Card의 method
        self.rank = rank # 이들은 parameter로 제공
        self.suit = suit 
    # random으로 뽑은 카드의 리스트를 'A of B' 형태로 return하구 이를 보여주기 위한 __str__구성
    def __str__(self) :
        rank_name = Card.rank_names[self.rank] # rank_names리스트 안에 있는 element불러옴
        suit_name = Card.suit_names[self.suit] # suit_names리스트 안에 있는 element불러옴
        return "%s of %s" % (rank_name, suit_name)
    # 카드의 대소 설정
    def __lt__(self, other) :
        if self.suit < other.suit :
            return True
        if self.suit > other.suit :
            return False
        if self.rank < other.rank :
            return True
        return False
    
# 덱 구성
class Deck :
    def __init__(self) :
        self.cards = [] # 덱에 있는 모든 카드 리스트
        for suit in range(4) :
            for rank in range(1, 14) :
                card = Card(suit, rank) # 에이스클로버부터~스페이드킹까지 모든 52개의 카드를 덱에 추가
                self.cards.append(card)
                
    # 모든 카드 리스트를 \n으로 구분된 string으로 구성하여 그에 맞게 print해주는 __str__구성
    def __str__(self) :
        res = [] 
        for card in self.cards :
            res.append(str(card)) # string형태의 card데이터 삽입. 하나의 element를 print하고 한 행씩 넘겨간다. (\n 때문에)
        return "\n".join(res)
    # 끝에 있는 카드 하나를 뽑는 속성
    def pop_card(self) : 
        return self.cards.pop()
    # 카드를 다시 덱에 넣는 속성
    def add_card(self, card) :
        self.cards.append(card)
    # 카드를 섞는 속성
    def shuffle(self) :
        random.shuffle(self.cards)
    # 한 사람이 주어진 카드의 수만큼 카드를 뽑아가는 속성 (hand로 옮기는 것)
    def move(self, hand, num) :
        for i in range(num) :
            hand.add_card(self.pop_card()) 
    # 다수의 사람이 주어진 카드의 수만큼 카드를 뽑아가는 속성
    def deal_hands(self, num_hands, num_cards) :  # num_hands가 사람의 수가 되고 num_cards가 카드의 수가 된다.
        hands = [] # hands라는 빈 리스트 설정
        for i in range(num_hands) :
            hand = Hand()
            self.move(hand, num_cards)
            hands.append(hand)
            
        return hands
    # 게임 화면에 카드들을 표시하기 위함
    

class Hand(Deck) :
    def __init__(self, label=" ") :
        self.cards = []
        self.label = label
    def print_table(self) :
        print(self.label)


        
def main() :
    deck = Deck()
    deck.shuffle()
    # 4명의 player가 5장씩 카드를 걷어감
    hands = deck.deal_hands(4, 5)
    
    
    # 뽑은 카드들의 이름들을 산출
    for hand in hands :
        print("\n")
        print(hand)

main()

