from cs1graphics import *
import random, time

canvas = Canvas(550,480)
canvas.setBackgroundColor('light blue')
canvas.setTitle('Memento Games')

photos = []
cards=[]
board=[]

def main():
    correct_pairs = 0
    round = 0

    layer = Layer()
    layer.setDepth(40)
    canvas.add(layer)

    initialize_cards_and_board()
    show_initial_screen()

    while(correct_pairs<12):
        posit1 = get_a_card(1)
        posit2 = get_a_card(2)
        if posit1 == posit2:
            print(posit1,posit2,':You choose the same card! Retry.')
        elif is_valid(posit1,posit2):
            if check_cards(posit1,posit2,layer):
                  print('Great! You got it.')
                  correct_pairs += 1
            else:
                  print('Sorry! Try again.')
        else :
            print(posit1,'or',posit2,'is invaild.')
        round += 1
        print('the' + str(round) + round_suffix(round) + 'round' + ':',correct_pairs, 'correct pairs')
    print('You are done! Your number of trials is ',round,'.')

def initialize_cards_and_board():
    for photo_id in range(12):
        if photo_id<10:
          filename = 'faces/face0' + str(photo_id) + '.jpg'
        else:
          filename = 'faces/face' + str(photo_id) + '.jpg'
        photos.append(filename)
        cards.append(photo_id)
        cards.append(photo_id)
    random.shuffle(cards)
    for i in range(24):
        hidden = True
        board.append([cards[i],hidden])

def show_initial_screen():
    x0 = 50
    y0 = 60
    for index in range(24):
        i = index // 6
        j = index % 6
        rect = Rectangle(90,120)
        rect.moveTo(x0 + 90*j, y0+120*i)
        canvas.add(rect)
        label = Text(str(index))
        label.moveTo(x0 + 10 + 90*j, y0 + 120 * i)
        canvas.add(label)

def get_a_card(new):
    while(True):
        if new == 1:
            pos = input('Enter the 1st card number: ')
        else :
            pos = input('Enter the 2nd card number: ')
        try:
            pos = int(pos)
            return pos
        except:
            print(pos,': invaild input')

def is_valid(pos1,pos2):
    if pos1 < 0 or pos1 > 23 :
        return False
    if pos2<0 or pos2 > 23:
        return False
    if is_hidden(pos1) and is_hidden(pos2):
        return True
    return False

def is_hidden(pos):
    photo_id, hidden = board[pos]
    return hidden

def check_cards(pos1,pos2,layer):
    photo_id1, hidden1 = board[pos1]
    photo1 = add_to_layer(pos1, photo_id1, layer)
    photo_id2, hidden2 = board[pos2]
    photo2 = add_to_layer(pos2,photo_id2, layer)
    time.sleep(3)
    if photo_id1 == photo_id2:
        update_board(pos1)
        update_board(pos2)
        return True
    layer.remove(photo1)
    layer.remove(photo2)
    return False

def add_to_layer(pos, photo_id,layer):
    x0 = 50
    y0 = 60
    i = pos // 6
    j = pos % 6
    filename = photos[photo_id]
    photo=Image(filename)
    photo.moveTo(x0 + 90*j, y0+120*i)
    layer.add(photo)
    return photo

def update_board(pos):
    board[pos][1] = False

def round_suffix(rnd):
    if rnd == 1:
        return'st'
    if rnd == 2:
        return 'nd'
    if rnd == 3:
        return 'rd'
    return 'th'

          
main()       
