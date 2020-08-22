from cs1robots import *
load_world("worlds/amazing2.wld")
# beepers 스펠링에 유의
hubo = Robot(beepers=1)
hubo.set_trace("red")
hubo.set_pause(0.2)
hubo.drop_beeper()
hubo.move()
def turn_right():
    for i in range(3):
        hubo.turn_left()
while not hubo.on_beeper() :
    # 여기서 right_is_clear여부를 묻는 걸 먼저 써주어야 하는 게 포인트!
    # 만약 front_is_clear를 먼저 써주었으면 상황은 변하지 않았을것!
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else :
        hubo.turn_left()
hubo.turn_left()    
