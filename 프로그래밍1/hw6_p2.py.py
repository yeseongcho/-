"""
Name: 조예성
Student ID : 21600685
Description : 이 함수는 메멘토 게임을 실행하기 위한 프로그램입니다.( main함수부터 읽기를 권장 )
"""


from cs1graphics import *
import random, time
# 게임할 판 설정
canvas = Canvas(550, 480)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Memento Games")

photos = [] # 사진과 파일 이름을 담기 위한 리스트 (추후에 사진을 업로드하기 위해도 사용됨)


cards = [] # 카드의 고유 식별 번호 담기. 같은 쌍이 있으므로 총 12개의 숫자가 한쌍씩 24개가 들어간다.


board = [] # index값으로 cards의 element와 hidden이라는 변수가 들어간다. hidden은 카드의 뒤집어졌는지 아닌지의 여부를 True or False로 반환해주는 변수이다.




# 이 함수는 게임 시작 전 사진의 이름과 파일명, 카드의 고유식별번호, 뒤짚어진 여부를 보여주는 리스트를 만드는 함수
def initialize_cards_and_board() :
    for photo_id in range(12) : 

        if photo_id < 10  : # face'x' 뒤에 x 숫자가 일의 자리인 경우 앞의 0을 붙여줘야하므로 추가로 조건 만듦

            filename = "faces/face0" + str(photo_id) + ".jpg" 

        else :
            filename = "faces/face" + str(photo_id) + ".jpg"

        photos.append(filename) 

        cards.append(photo_id) # 카드의 고유 식별번호를 입력. 같은 카드가 2개이므로 2번 실행

        cards.append(photo_id)


    random.shuffle(cards) # 게임을 다시 실행할 때 사진을 섞기 위해

    for i in range(24) :
        hidden = True
        board.append([cards[i], hidden]) # 카드를 우선 다 뒤짚어 놓는다.




# 이 함수는 게임 시작 전 카드들의 위치를 정해주는 함수이다.
def show_initial_screen() :
    x0 = 50 # 이 x0와 y0는 맨 좌측 상단에 위치하는 직사각형의 처음 중심값이다.
    y0 = 60

    for index in range(24) :

        i = index//6 # 직사각형의 중심이 1번째 행에서 4번째 행까지 위치시키게 하기 위한 식이다. 

        j = index%6 # 직사각형의 중심이 1번째 열에서 6번쨰 열까지 위치시키게 하기 위한 식이다. 

        rect = Rectangle(90, 120)

        rect.moveTo(x0 + 90*j, y0+120*i)

        canvas.add(rect)

        label = Text(str(index)) # index별로 카드에 숫자 삽입

        label.moveTo(x0 + 90*j, y0+120*i) 

        canvas.add(label)


# 식별할 카드의 index번호를 입력받는 함수 지정
def get_a_card(new) :
    while(True) :
        if new == 1 : 
            pos = input("Enter the 1st card number: ")

        else : 
            pos = input("Enter the 2nd card number: ")

        try : # 카드 입력받을 때마다 올바른 입력을 받았는 지 확인하는 try except 함수 이용
            pos = int(pos)
            return(pos)

        except : # 올바르지 않을 경우(즉, 숫자가 아닌 다른 변수를 입력했을 경우)
            print(pos, ": invalid input")


# 입력 받은 숫자가 유효한 숫자인지 판별하는함수 ( 주어진 카드 번호 범위 내의 숫자를 입력했는지, 이미 뒤짚혀진 카드의 번호를 입력했는지 판별)
def is_valid(pos1, pos2) :
    if pos1<0 or pos1>23 : # 숫자를 입력했지만 주어진 index바깥의 숫자를 입력했을 경우 False반환
        return False

    if pos2<0 or pos2>23 :
        return False

    if is_hidden(pos1) and is_hidden(pos2) : # 사용자가 이미 뒤짚은 카드를 골랐는 지 판별하는 함수
        return True

    return False


# 이 함수는 이 카드가 뒤집혀있는지 아닌지 상태를 나타내주는 함수
def is_hidden(pos) :
    photo_id, hidden = board[pos] 
    return hidden 


# 이 함수는 카드들을 직접 뒤짚어 확인하는 프로그램이다.
def check_cards(pos1, pos2, layer) :
    photo_id1, hidden1, = board[pos1] # 첫번째 입력한 숫자의 카드의 식별번호와 뒤짚은 여부를 나타내는 hidden값 unpacking

    photo1 = add_to_layer(pos1, photo_id1, layer) # add_to_layer함수 실행, 즉 카드를 뒤짚음

    photo_id2, hidden2 = board[pos2] 

    photo2 = add_to_layer(pos2, photo_id2, layer)

    time.sleep(3) 

    if photo_id1 == photo_id2 : # 카드의 고유 식별번호가 일치한지 ( 즉 사진이 일치하는지 )
        update_board(pos1) # 일치할 경우 뒤짚은 상태로 둠

        update_board(pos2) 
        return True  

    layer.remove(photo1) # 불일치할 경우 추가했던 사진을 제거

    layer.remove(photo2)

    return False  


# 이 함수는 뒤짚은 결과인 사진을 설정한 layer를 이용해 카드 위에 덧붙여주는 함수이다.
def add_to_layer(pos, photo_id, layer) :
    # 처음 카드위치를 설정했을 때랑 같은 알고리즘
    x0 = 50
    y0 = 60
    i = pos//6
    j = pos%6 
    filename = photos[photo_id] # 입력받은 고유식별번호에 해당하는 사진 이름과 파일명 element를 filename에 저장

    photo = Image(filename) # 이미지 불러옴 

    photo.moveTo(x0 + 90*j, y0+120*i) 

    layer.add(photo) 
    return photo

# 카드를 뒤짚은 상태로 유지하기 위한 함수
def update_board(pos) :
    board[pos][1] = False


# 라운드 뒤에 서수 형식을 표시해주기 위한 함수 구성
def round_suffix(rnd) :
    if rnd == 1 :
        return "st"
    if rnd == 2 :
        return "nd"
    if rnd == 3 :
        return "rd"
    return "th"


def main() :
    # 게임 시작 전 환경 설정

    correct_pairs = 0 # 맞는 순서쌍의 갯수를 의미. 

    round = 0 # 각 라운드의 수를 의미

    layer = Layer() # 이 빈 layer에 나중에 사진을 선택할 때 해당 사진을 덧붙이기 위해 설정, 즉 뒤짚기를 하는 경우를 뜻한다.

    layer.setDepth(40) # 그 사진은 기존에 뒤짚어진 카드보다 더 앞쪽에 위치해야 하므로 깊이 40 설정

    canvas.add(layer) 


    # 카드와 보드 초기화
    initialize_cards_and_board() 


    # 카드와 보드 화면에 띄우기
    show_initial_screen()

    while(correct_pairs < 12) :
        # 식별할 2개의 카드를 입력받는다
        posit1 = get_a_card(1)
        posit2 = get_a_card(2)
        round += 1 # 실행할 라운드 

        if posit1 == posit2 : # 같은 카드를 2번 고른 경우
            print(posit1, posit2, ": You choose the same card! Retry.")

        elif not is_valid(posit1, posit2) : # 유효하지 않은 숫자를 입력했을 경우 
            print(posit1, "or", posit2, "is invalid")

        else : # 유효한 숫자를 입력했을 경우
            if check_cards(posit1, posit2, layer) : # 일치한 경우
                print("Great! You got it") 

                correct_pairs += 1 # 맞는 쌍 한 개수 증가

            else : # 사진이 일치하지 않는 경우
                print("Sorry! Try again.") 
        print("the" + str(round) + round_suffix(round) + "round" + ":", correct_pairs, "correct_pairs") # 라운드를 실시할 때 마다, 몇 라운드 인지와 맞은 쌍의 갯수는 몇개인 지 알려주는 print구문

    print("You are done! Your number of trials are ", round, ".") # correct_pairs가 12개가 될때 게임을 종료하고 최종 시행한 round값 반환

main()
