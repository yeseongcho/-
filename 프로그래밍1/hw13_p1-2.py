"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 Player 4명이 임의로 카드를 뽑아 그 카드를 table에서 보여주는 프로그램입니다.
"""


from cs1graphics import * 
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
        rank_name = Card.rank_names[self.rank] # 이미지 파일 이름을 불러오기 위한 변수 설정
        suit_name = Card.suit_names[self.suit]
        self.image = Image("./BlackJack/"+ suit_name +"_"+rank_name +".png") # 이미지 불러옴
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
        for i in range(num_hands) : # 플레이어마다 다른 label 삽입
            if i == 0 :
                hand = Hand("player1")
                self.move(hand, num_cards) # for i in range(num_hands)안에 또 다른 반복문 for i in range(num_cards)가 있어서 한 사람당 주어진 카드의 개수만큼 뽑아가는 반복문을 실행하기 위함
                hands.append(hand) # 뽑을때마다 hands리스트에 추가한다.
            elif i == 1 :
                hand = Hand("player2")
                self.move(hand, num_cards)
                hands.append(hand)
            elif i == 2 :
                hand = Hand("player3")
                self.move(hand, num_cards)
                hands.append(hand)
            else :
                hand = Hand("player4")
                self.move(hand, num_cards)
                hands.append(hand)
            
        return hands
    # 게임 화면에 카드들을 표시하기 위함
    def show_cards(self, table) :
        x = table.x0 # x의 초기값
        y = table.y # y는 increment_y에 의해 누적되는 값
        d = table.depth0  # d의 초기값
        for card in self.cards : # 여기의 self.cards는 hands[i](한 player)이고, card(수중에 있는 카드들, 5장이 된다.)는 그 안에 있는 카드들을 의미한다.
            table.display_card(card, x, y, d) # 카드를 보여줌
            x += table.delta_x # 카드 하나를 보여주고 x값 증가(+50)
            d += table.delta_d # 카드 하나를 보여주고 d값 감소(-5)
        table.increment_y() # 한 player의 것이 끝나고 나면 다음 행으로 넘어가기 위한 y값 증가(+120)
    

class Hand(Deck) :
    def __init__(self, label=" ") :
        self.cards = []
        self.label = label
    def print_table(self) :
        print(self.label)
# 판을 구성
class Table:
    def __init__(self) :
        self.canvas = Canvas(1000, 600, "dark green", "BlackJack")
        # 맨 처음 카드가 위치하게 되는 x,y좌표와 그 깊이 설정
        self.x0 = 250
        self.y0 = 80
        self.depth0 = 50
        # 카드 한장씩 추가될때마다 변화하는 x위치와 깊이 설정
        self.delta_x = 50
        self.delta_d = -5
       
        
        self.x = self.x0
        self.y = self.y0
        self.d = self.depth0
        self.images=[] # 나중에 다 지우기 위한 리스트 구성
    # 수중에 있는 5장의 카드를 보여주는 함수
    def display_card(self, card, x, y, d) :
        image = card.image # 이미지를 불러오고
        self.images.append(image) # self.images라는 빈 리스트에 저장
        image.setDepth(d) # 입력 받은 깊이 값을 설정하여
        image.moveTo(x, y) # 입력 받은 좌표에 위치시킨다.
        self.canvas.add(image)
        time.sleep(1)
    # player의 이름을 보여주는 함수
    def show_label(self, where, hand) :

       

        text = Text()
        
        # player가 변할 때마다 변하는 y값 저장. where는 현재 위치하는 행을 의미
        y = self.y0 + where*120
        
        text.setFontColor("white")
        
        text.setFontSize(20)
        
        text.setDepth(10)
        # 변화하는 y를 적용하여 문구 위치
        text.moveTo(100, y)
        
        self.canvas.add(text)
         
        text.setMessage(hand.label) #-- 도대체 이녀석이 무슨 역할을 하는 건지 모르겠다!!, hand.lable이 왜 필요한 걸까...?
        
    # player가 변할 때마다 y를 증가시켜 주는 함수
    def increment_y(self) :
        self.y += 120

    # table에 있는 모든 카드들을 제거하기 위한 함수 
    def clear(self) :
        for image in self.images :
            self.canvas.remove(image)
        # 지우고 난 뒤 모든 값들 초기화
        self.x = self.x0
        self.y = self.y0
        self.images = []
    
        


        
def main() :
    table = Table()
    deck = Deck()
    deck.shuffle()
    # 4명의 player가 5장씩 카드를 걷어감
    hands = deck.deal_hands(4, 5)
    # 4명의 player들이 가져간 카드를 보여주는 반복문
    for i in range(4) :
        table.show_label(i, hands[i]) # player문구
        hands[i].show_cards(table) # 카드를 보여줌
        time.sleep(1)
   
    table.clear() 
    # 뽑은 카드들의 이름들을 산출
    

main()
