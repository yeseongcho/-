"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 블랙잭 게임을 GUI로 실행하는 프로그램입니다.
"""


from cs1graphics import *
import random, time

RANKS = {"2": 2, "3": 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
# 테이블 내 환경설정
class Table :
    def __init__(self) :
        self.canvas = Canvas(600, 400, 'dark green', 'Black Jack')
        self.x0 = 100 # 카드의 초기 위치
        self.dealer_y = 80 # 딜러 카드의 초기 y위치                                    
        self.player_y = 200 # 플레이어 카드의 초기 y
        self.delta_x = 50 # 카드 한장씩 뽑을때마다 x의 변화량
        self.dealer_x = self.x0 # 딜러의 x의 초기값 삽입
        self.player_x = self.x0 # 플레이어의 x의 초기값 삽입
        self.depth0 = 100 # 초기 깊이값
        self.delta_d = -5 # 카드 한장씩 뽑을 때마다 깊이의 변화량
        self.dealer_d = self.depth0 # 깊이도 초기 값 삽입
        self.player_d = self.depth0
        
        # 딜러와 플레이어의 점수란을 보여주기 위한 text설정   
        self.dealer_s = Text()
        self.dealer_s.setFontColor('white')
        self.dealer_s.setFontSize(10)
        self.dealer_s.moveTo(self.canvas.getWidth() - 100, self.dealer_y)
        self.canvas.add(self.dealer_s)
        
        self.player_s = Text()
        self.player_s.setFontColor('white')
        self.player_s.setFontSize(10)
        self.player_s.moveTo(self.canvas.getWidth() - 100, self.player_y)
        self.canvas.add(self.player_s)
        # 이겼는지 졌는지를 표시하는 구문 설정
        self.message = Text()
        self.message.setFontColor('red')
        self.message.setFontSize(20)
        self.message.moveTo(self.canvas.getWidth()/2 - 50, self.canvas.getHeight() - 80) # 사용자가 임의로 table의 크기를 조정해도 일정한 곳에 위치시키기 위한 설정
        self.canvas.add(self.message)
        # 카드를 뽑을 건지 말건지, 게임을 더 진행할 건지 말건지를 묻는 구문 설정
        self.question = Text()
        self.question.setFontColor('white')
        self.question.setFontSize(20)
        self.question.moveTo(self.canvas.getWidth()/2 - 50, self.canvas.getHeight() - 40)
        self.canvas.add(self.question)
        # 게임을 마칠때마다 새롭게 판을 깔기 위해 
        self.images = []
    # 점수를 보여주는 함수
    def set_score(self, score, dealer = False) :
        text = "%3d" % score
        if dealer :
            self.dealer_s.setMessage("Dealer's score :" + text)
        else :
            self.player_s.setMessage("Your score: " + text)
    # 카드를 보여주는 함수
    def show_card(self, card, dealer = False) :
        if dealer :
            card.display_card(self, self.dealer_x, self.dealer_y, self.dealer_d)
            self.dealer_x += self.delta_x # 카드 한장씩 뽑고 깊이와 위치 변화 조정
            self.dealer_d += self.delta_d
        else :
            card.display_card(self, self.player_x, self.player_y, self.player_d)
            self.player_x += self.delta_x
            self.player_d += self.delta_d
    # 사용자가 더 이상 카드를 뽑지 않을 때 딜러의 hidden카드를 뒤짚기 위한 함수
    def open_hcard(self, hand) :
        card = hand.cards[0] # 딜러의 맨 처음 카드를 가지고 온다
        card.update_state(False) # 뒤짚기
        card.display_card(self, self.x0, self.dealer_y, self.dealer_d) # 해당 함수를 보여주고 해당 함수의 깊이와 x의 위치는 초기값을 부여한다.
        return card
    # 게임을 마치고 테이블을 초기화하기 위한 함수
    def clear(self) :
        self.dealer_x = self.x0 # 모든 x와 깊이를 초기로 설정해준다.
        self.player_x = self.x0
        self.dealer_d = self.depth0
        self.player_d = self.depth0
        self.dealer_s.setMessage("") # socre, 질문 등 메세지들도 공란으로 해준다.
        self.player_s.setMessage("")
        self.message.setMessage(" ")
        self.question.setMessage(" ")
        for image in self.images : # 카드들을 제거하는 반복문 구성
            self.canvas.remove(image)
        self.images = []
    def show_message(self, msg) : # 상황에 맞는 메세지를 산출하기 위한 함수
        self.message.setMessage(msg)
    # 카드를 뽑을지, 게임을 더 진행할지에 대한 대답 산출
    def ask_response(self, prompt) :
        self.question.setMessage(prompt) 
        while True :
            event = self.canvas.wait() # GUI를 사용하기 위한 wait() 
            self.question.setMessage(" ")
            if event == None :
                sys.exit(1) # 프로그램을 종료하는 경우
            response = event.getDescription() # 사용자가 입력하는(키보드, 마우스 등)값을 설정
            if response == "keyboard" : # 키보드 값을 입력받았을 때
                key = event.getKey()
                if key == "y" : # 게임을 계속 실행하는 경우
                    return True
                if key == "n" : # 게임을 종료하는 경우
                    return False
            self.question.setMessage(response+".Type"+"in(y/n)") # 그 외 다른 값들을 입력했을 경우 
    
    def close(self) :
        self.canvas.close()

# 카드 리스트를 만드는 함수
class Card:
    def __init__(self, rank, suit) :
        assert(rank in RANKS and suit in SUITS) # 입력받은 rank와 suit가 RANKS, SUITS 리스트 안에 없으면 error를 내는 기능
        img_path = "./BlackJack/"  
        self.rank = rank 
        self.suit = suit 
        self.value = RANKS[rank] # 후에 카드의 value값들을 더해주기 위해 RANKS의 element반환
        self.image = Image(img_path+suit+"_"+rank+".png") # 이미지를 가지고 오는 method 취함
        self.hidden = False # hidden값은 초기 false 설정

    # 플레이어가 카드를 뽑을 때 어떤 카드를 뽑았는지 산출해주는 구문
    def __str__(self) :
        article = "a"
        if self.rank in ("8", "Ace") :
            article = "an"
        return article +" "+ self.rank +" "+ "of" +" "+ self.suit
    # hidden값을 변환해주는 함수
    def update_state(self, hidden) :
        self.hidden = hidden
    # 카드를 보여주는 함수
    def display_card(self, table, x, y, d) :
        if self.hidden : # 딜러의 첫 번째 카드의 경우, hidden이 True인 경우
            image = Image("./BlackJack/" + "Back.png")
        else :
            image = self.image
        image.setDepth(d) # 깊이는 입력받은 깊이로 하고
        image.moveTo(x, y) # 입력받은 x,y로 카드를 위치시킨다
        table.canvas.add(image)
        table.images.append(image) # 후에 제거하기 위해 table의 images리스트에도 추가해준다.
        time.sleep(1)

# 덱을 구성하는 함수
class Deck :
    # 테이블 내 설정된 SUITS와 RANKS의 카드 리스트를 만듦
    def __init__(self) :
        self.cards = []
        for suit in SUITS :
            for rank in RANKS :
                self.cards.append(Card(rank, suit))
   # 카드를 섞어줌
    def shuffle(self) :
        random.shuffle(self.cards)
        return(self)

    # 사용자나 딜러가 카드를 뽑음
    def draw(self) :
        card = self.cards.pop()
        return card
    # 뽑은 카드를 hand리스트에 저장. 즉 추후에 테이블에 내가 뽑은 카드들을 전부 보여주기 위함
    def move_card(self, hand, dealer = False) :
        card = self.draw() # 카드를 뽑음
        hidden = False
        # 딜러가 맨 처음 카드를 뽑는 경우
        if dealer and len(hand.cards) == 0 :
            hidden = True # 뒤짚은 상태
        hand.add(card, hidden) # hand 리스트에 추가한다.
        return card

# 현재 수중에 있는 카드 
class Hand(Deck) :
    def __init__(self, dealer = False) :
        self.cards = []
        self.dealer = dealer # 딜러 수중에 있는 경우를 구분하기 위해

    def add(self, card, hidden = False) :
        if hidden : # hidden이 True인 경우, 즉 처음 딜러의 카드의 경우
            card.update_state(hidden)
        self.cards.append(card) 
    # 현 수중에 있는 카드들의 value의 합을 계산하는 함수
    def hand_value(self) :
        value = 0
        for card in self.cards :
            value += card.value # 합을 누적시켜 준다.
        return value


# 게임 시작 전에 초기 딜러와 사용자의 카드 두장 씩을 뽑아놓는 경우
def initial_two_cards(deck, player, dealer, table) :
    card = deck.move_card(player) # 플레이어의 카드를 뽑는 경우
    table.show_card(card) # 뽑은 뒤 테이블에 위치시킴
    #print("You were dealt", card) # 어떠한 카드를 뽑았는지 공시
    
    card = deck.move_card(dealer, True) # 딜러가 카드를 뽑는 경우
    table.show_card(card, True)
    #print("Dealer was dealt a hidden card") # 초기 카드는 hidden

    card = deck.move_card(player) # 다음 플레이어의 카드를 뽑는 경우
    table.show_card(card)
    #print("You were dealt", card) 
    table.set_score(player.hand_value()) # 두번째카드를 뽑을 때 score를 table에 공시

    card = deck.move_card(dealer, True) # 딜러의 두 번째 카드를 뽑는 경우
    table.show_card(card, True)
    #print("Dealer was dealt", card)
    #print("Your total iwas", player.hand_value()) # 두번째카드를 뽑을 때 score를 table에 공시

# 초기 2개의 카드 뽑은 이후
def players_turn(deck, player, table) :
    while player.hand_value() < 21 : # 아직 21을 넘지 않아 게임이 진행 가능한 경우
        if not table.ask_response("Would you like another card? (y/n)") : # 카드를 계속 뽑을지 묻는 조건문 -- table.ask_response()로 수정
            break
        # 카드를 계속 뽑는 경우
        card = deck.move_card(player)
        table.show_card(card)
        table.set_score(player.hand_value())
        #print("You were dealt", card)
        #print("Your total was", player.hand_value())
    # 플레이어의 카드 value의 합이 21이 넘어 패배한 경우
    if player.hand_value() > 21:
        #print("You went over 21! You lost!")
        return True # 게임을 종료한다.
    return False # 플레이어가 더 이상 카드를 뽑지 않음.

# 플레이어가 더이상 카드를 뽑지 않는 경우
def dealers_turn(deck, player, dealer, table) :
    table.open_hcard(dealer) # 딜러가 첫 번째 카드를 개봉한다.
    #print("Dealer's hidden card was", card)
    #print("Dealer's total was", dealer.hand_value())
    table.set_score(dealer.hand_value(), True)
    while dealer.hand_value() < 17 and dealer.hand_value() <= player.hand_value() : # 딜러의 카드가 17보다 작고 player보다 value가 작으면 계속해서 카드를 뽑는다.
        card = deck.move_card(dealer, True)
        table.show_card(card, True)
        table.set_score(dealer.hand_value(), True)
        #print("Dealer was dealt", card)
        #print("Dealer's total was", dealer.hand_value())
# 최종 승부 -- 여기에 msg 추가!!
def conclude_the_game(player, dealer, table) :
    player_total = player.hand_value() # 최종 플레이어의 카드 value
    dealer_total = dealer.hand_value() # 최종 딜러의 카드 value
    if player_total > 21 : # 플레이어 패배 경우
        msg = "You went over 21! You lost!"
        
    elif dealer_total > 21 : # 딜러의 패배 경우
        msg = "The dealer went over 21! You win!"
    elif player_total > dealer_total :
        msg = "You win!"
    elif player_total < dealer_total :
        msg = "You lost!"
    else :
        msg = "You have a tie!"
    table.show_message(msg)
    

# 블랙잭 게임 구성
def blackjack(table) :
    deck = Deck()
    deck.shuffle()
    dealer = Hand(True)
    player = Hand()

    initial_two_cards(deck, player, dealer, table)
    already_lost = players_turn(deck, player, table)
    if not already_lost :
        dealers_turn(deck, player, dealer, table)
    conclude_the_game(player, dealer, table)

# 게임실행
def game_loop() :
    print("Welcome to Blackjack!")
    # 게임 실행 전 환경설
    table = Table()
    while True :
        blackjack(table)
        time.sleep(5)
        table.clear()
        if not table.ask_response("Play another round? (y/n)") :
            break
    table.close()
game_loop()
    
