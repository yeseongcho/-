"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 사용자로부터 입력받은 2~4명의 플레이어 사이에서 블랙잭 게임을 진행하는 프로그램입니다.
"""
import random, time, sys
from cs1graphics import *
suit_name = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_name = {"2": 2, "3": 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}
canvas = Canvas(1000, 600, "dark green", 'Black Jack')
# 판 구성
class Table :
    def __init__(self) :
        # 초기 딜러와 플레이어들의 카드를 구성
        self.x0 = 300
        self.depth0 = 50
        self.delta_x = 50
        self.delta_d = -5
        self.y0 = 80
        # 승부를 알려주는 메세지 구성
        self.message = Text()
        self.message.setFontColor('red')
        self.message.setFontSize(20)
        self.message.moveTo(canvas.getWidth()/2 - 50, canvas.getHeight()-80)
        canvas.add(self.message)
        # 질문 메세지 구성
        self.question = Text()
        self.question.setFontColor('white')
        self.question.setFontSize(20)
        self.question.moveTo(canvas.getWidth()/2 - 50, canvas.getHeight() - 40)
        canvas.add(self.question)
        self.PLAYERS = self.set_game() # 사용자의 수 설정
        self.hands = []
        for i in range(self.PLAYERS) :
            if i == self.PLAYERS - 1 :
                label = "Dealer"
                y = self.y0
            else :
                label = "Player %1d" % (i+1)
                y = self.y0 + (i+1)*120
            hand = Hand(label, self.x0, y, self.depth0, self.delta_x, self.delta_d)
            self.hands.append(hand)
    def get_no_of_players(self) :
        return self.PLAYERS
    # 사용자의 수를 입력받음
    def set_game(self) :
        self.question.setMessage("How many persons?")
        while True :
            event = canvas.wait() # GUI활용
            if event == None :
                sys.exit(1) 
            response = event.getDescription() # 어떠한 입력값을 받았는지 확인
            if response == "keyboard"  : # 키보드의 입력값인 경우
                key = event.getKey()
                if "1" < key < "5" : # 정상입력
                    self.question.setMessage("number of players: "+ key)
                    key = int(key)
                    return key
                else : #키보드 값의 비정상값 입력
                    self.question.setMessage(key + "? Type in a number" + "between 2 and 4, inclusively")

    # 새로운 플레이어와 게임을 하는 경우
    def start_new(self, prompt) : 
        self.question.setMessage(prompt + "(y/n)") 
        while True :
            event = canvas.wait()
            if event == None :
                sys.exit(1)
            response = event.getDescription()
            if response == "keyboard" :
                key = event.getKey()
                if key == "y": # y가 입력될 경우 True를 반환해 Table()를 다시 실행함으로 새로운 판 구성
                    self.question.setMessage(" ")
                    return True 
                if key == "n" : # n의 경우 판 종료
                    self.question.setMessage(" ")
                    return False
            self.question.setMessage(response + ".Type in (y/n)") #키보드 이외의 값 입력시 다시 입력 요구

     # 한 게임이 끝난 후 게임을 다시 실시할 것인지를 묻는 경우           
    def ask_response(self, prompt) :
        self.question.setMessage(prompt)
        while True :
            event = canvas.wait()
            if event == None :
                sys.exit(1)
            response = event.getDescription()
            if response == "keyboard" :
                key = event.getKey()
                self.question.setMessage(" ")
                if key == "y": # 게임을 다시 실행하고 싶은 경우
                    return True
                if key == "n": # 게임을 다시 실행하고 싶지 않은 경우
                    return False
                else :
                    self.question.setMessage(key+ "? I beg your pardon.") # 키보드로 그 이외의 값들을 입력하는 경우
            else :
                self.question.setMessage("An unexpected event") # 키보드 이외의 값들을 입력하는 경우
    # 카드들의 이미지를 불러옴
    def display_card(self, card, hand, flag = False) :
        if card.hidden_state() : # 딜러의 첫번째 숨겨진 카드의 경우
            image = card.get_image(True)
        else : # 다른 나머지 카드들의 경우
            image = card.get_image()
        d, x0, x, y = hand.get_data() # 카드들의 위치 데이터를 가지고옴
        if flag : # 딜러의 첫번째 숨겨진 카드를 공개하는 경우
            back_image = card.get_back_image() 
            canvas.remove(back_image)
            image.moveTo(x0, y)
        else : # 나머지 카드들의 위치 조정해 보여주는 경우
            image.moveTo(x, y)
            hand.update_data() # 깊이랑 x위치 변화값 부여
        image.setDepth(d) # 변화 조정한 걸 깊이로 설정
        canvas.add(image)
        time.sleep(1)
    # 딜러의 히든 카드를 공개하는 경우
    def open_hcard(self, dealer) :
        hand = self.hands[dealer] 
        card = hand.get_card(0) # 맨 첫번째 popping한 카드
        card.update_state(False) # 뒤짚었으니 False로 변환
        self.display_card(card, hand ,True) # 뒤짚었을 때 카드 위치 조정
        return card
    # 히든 카드를 제외한 다른 카드들을 보여주는 경우
    def show_card(self, card, who) :
        hand = self.hands[who]
        image = self.display_card(card, hand)
        return hand.get_score()
    # 승패를 보여주는 함수
    def show_message(self, text) :
        self.message.setMessage(text)
        time.sleep(3)
        self.message.setMessage(" ")#메세지 산출 이후 제거
    # 사람들의 리스트
    def get_hand(self, who) :
        return self.hands[who]
    # 카드들의 위치값, hidden값, 점수 전부 초기화
    def clear(self) :
        for hand in self.hands :
            hand.clear()
    # label값도 초기
    def clear_label(self) :
        for hand in self.hands :
            hand.erase_label()
    # 플레이어들 수중에 있는 카드들의 점수를 계산
    def hand_value(self, who) :
        return self.hands[who].get_score()
    # 경기 종료하는 경우
    def close(self) :
        canvas.close()

# 카드 구성
class Card :
    def __init__(self, suit="Clubs", rank = "2") :
        self.rank = rank
        self.suit = suit
        self.value = rank_name[rank] # 카드의 점수값
        self.image = Image("./BlackJack/" + suit + "_" + rank + ".png") 
        self.back_image = Image("./BlackJack/" + "Back.png")
        self.hidden = False # 히든카드의 여부
    # 카드가 어떤 것인지 print할때
    def __str__(self) :
        article = "a"
        if self.rank in ("8", "Ace") :
            article = "an "
        return article + self.rank + " of" + self.suit
    # 히든 카드일 때 히든 카드의 back image반환하고 그렇지 않은 경우는 해당 카드의 image반환
    def get_image(self, hidden = False) :
        if hidden :
            return self.back_image
        return self.image
    
    def get_back_image(self) :
        return self.back_image
    # 뒤집혀진 경우를 나타내는 함수
    def hidden_state(self) :
        return self.hidden
    # 카드가 역전하는 경우 상태를 바꾸기 위한 함수
    def update_state(self, hidden):
        self.hidden = hidden
# 덱 구성
class Deck :
    def __init__(self) :
        # 덱 설정
        self.cards = []
        for suit in suit_name :
            for rank in rank_name :
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self) :
        random.shuffle(self.cards)
        return(self)
    # 덱에 있는 카드들을 일부 수중으로 옮겨놓음
    def move_card(self, hand, hidden = False) :
        card = self.cards.pop()
        hand.add_card(card, hidden) 
        return card
    # 카드를 한 장 가져감 
    def get_card(self, index) :
        return self.cards[index]

# 수중에 있는 카드 
class Hand(Deck) :
    def __init__(self, label, x0, y, depth0, delta_x, delta_d) :
        # 수중에 있는 카드를 보여주기위한 위치 변수 설정
        self.x0 = x0
        self.depth0 = depth0
        self.label = label
        self.delta_x = delta_x
        self.delta_d = delta_d
        # player들의 이름 보여주는 텍스트 구성
        self.text_label = Text()
        self.text_label.setFontColor("white")
        self.text_label.setFontSize(20)
        self.text_label.moveTo(100, y)
        self.text_label.setMessage(self.label)
        canvas.add(self.text_label)
        # 수중에 있는 카드들의 위치값 구성
        self.cards = []
        self.x  = self.x0
        self.y = y
        self.depth = self.depth0
        self.score = 0
        # 플레이어들의 점수를 보여주기 위한 텍스트 구성
        self.text_score = Text()
        self.text_score.setFontColor('white')
        self.text_score.setFontSize(20)
        self.text_score.moveTo(canvas.getWidth()-100, y)
        self.text_score.setMessage(" ")
        canvas.add(self.text_score)
    # 카드를 수중으로 가지고 올 때
    def add_card(self, card, hidden) :
        self.score += card.value # 플레이어의 해당 카드의 점수 획득
        if hidden : # 딜러의 히든카드 경우
            card.update_state(hidden) 
        self.cards.append(card)
    # 카드를 보여줄때 위치값들을 조정
    def update_data(self) :
        self.x += self.delta_x
        self.depth += self.delta_d
    # 축적된 점수를 보여주는 함수
    def show_score(self) :
        tscore = "%3d" % self.score
        self.text_score.setMessage(tscore)
        return self.score
    # 게임 이후 수중에 있던 카드의 이미지나, 위치값, 점수값 들을 초기화기 위함
    def clear(self) :
        self.x = self.x0
        self.depth = self.depth0
        self.score = 0
        self.label = " "
        self.text_score.setMessage(" ")
        for card in self.cards :
            image = card.get_image(card.hidden_state())
            canvas.remove(image)
        self.cards = []
    # label를 지움
    def erase_label(self) :
        self.label = " "
        self.text_label.setMessage(" ")
    # 카드들의 위치를 display하기 위한 위치 데이터 확보
    def get_data(self) :
        return self.depth, self.x0, self.x, self.y
    # label데이터 확보
    def get_label(self) :
        return self.label
    # 점수 데이터 확보
    def get_score(self) :
        return self.score

# 초기 플레이어 별로 2장의 카드를 공시하는 경우
def first_two_cards(deck, table) :
    for j in range(2) : # 2장의 카드를 가져오기 위해
        for i in range(table.get_no_of_players()) : # 플레이어 별로 카드를 가져오기 위해
            hand = table.get_hand(i)
            if j == 0 and i == table.get_no_of_players() - 1 : # 딜러의 히든 카드를 가져오는 경우
                card = deck.move_card(hand, True)
            else :
                card = deck.move_card(hand)
            table.show_card(card, i) # 초기 2장의 카드를 모두 보여준다.

# 사용자의 차례
def players_turn(deck, table) :
    all_lost = True # True일 경우 플레이어의 패배라 table초기화, False의 경우 딜러의 차례로 넘어감을 나타내주는 지표
    player_max = 0 # 3명의 플레이어의 점수중 가장 큰 것을 환산하는 변수
    for i in range(table.get_no_of_players()-1) :
        hand = table.get_hand(i) #초기 수중의 있는 카드들의 점수
        tscore = hand.show_score() # 테이블에 공시
        while tscore < 21: # 점수가 21이하인 경우 플레이어는 계속 게임을 실행할 지 말지를 선택
            msg = "Player %1d, " % (i+1) + "Would you like to have another card?(y/n)"
            if not table.ask_response(msg) : # 더 이상 카드를 뽑지 않는 경우
                break
            # 추가로 카드를 뽑은 경우
            card = deck.move_card(hand)
            table.show_card(card, i)
            tscore = hand.show_score()
        # 플레이어의 카드 점수가 21을 넘긴 경우 - 패배한 경우
        if tscore > 21:
            msg = "Player %1d," % (i+1) + "you went over 21! You Lost!"
            table.show_message(msg)
        else : 
            all_lost  = False # 21을 넘지 않고 플레이어가 카드를 더 이상뽑지 않았을 때 딜러의 차례로 넘김
            player_max = max(player_max, tscore) # 3명의 플레이어 중 가장 큰 점수를취함
        time.sleep(1)
    return all_lost, player_max 
    
# all_lost가 False인 딜러의 차례
def dealers_turn(deck, player_max, table) :
    table.open_hcard(table.get_no_of_players() - 1) # 히든 카드 공개
    hand = table.get_hand(table.get_no_of_players() - 1)
    tscore = hand.show_score() # 점수 공시
    # 17보다 크거나 플레이어 최대점수보다 크면 카드를 그만 뽑는다. 그 전까지는 계속 뽑는다.
    while tscore < 17 and tscore <= player_max :
        card = deck.move_card(hand)
        tscore = table.show_card(card, table.get_no_of_players() - 1)
        tscore = hand.show_score()

# 승패를 최종 판별해주는 함수
def conclude_the_game(table) :
    dealer_hand = table.get_hand(table.get_no_of_players() - 1) # 딜러 수중에 있는 카드 
    dealer_val = dealer_hand.get_score() # 딜러의 최종 점수 계산
    for i in range(table.get_no_of_players() - 1) :
        hand = table.get_hand(i)
        player_val = hand.get_score() # 플레이어 한명 당 점수 계싼
        if player_val > 21 :
            msg = "you went over 21! You Lost!"
        elif dealer_val > 21 :
            msg = "the dealer went over 21! You won!"
        elif dealer_val < player_val :
            msg = "you Won!"
        elif dealer_val > player_val :
            msg = "You Lost!"
        else :
            msg = "You had a tie!"
        msg = "Player%1d, " % (i+1) + msg
        table.show_message(msg) # 승패 결과 공시
        time.sleep(1)
        msg = " " # 점수 표시 제거
        table.show_message(msg)
    table.clear()
# 블랙잭 게임 실행
def blackjack(table) :
    deck = Deck()
    deck.shuffle()
    first_two_cards(deck, table) # 첫번째 2개의 카드 공시
    all_lost, player_max = players_turn(deck, table) # 플레이어 차례
    if all_lost : # 플레이어의 카드가 21이 넘는 경우
        table.clear()
        return
    dealers_turn(deck,player_max, table) # 딜러의 차례
    conclude_the_game(table) # 승패 판별

def game_loop() :
    table = Table()
    while True :
        blackjack(table)
        if not table.ask_response("Play another round? (y/n)") :
            table.clear_label() # 똑같은 플레이어들과 판을 벌이는 경우
            if table.start_new("Play with new persons?") : # 다른 player와 플레이를 원하는 경우
                table = Table() # 다시 새롭게 판을 구성한다.
            else :
                break
        
    
    time.sleep(3)
    table.close()

game_loop()
                
