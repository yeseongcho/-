from cs1robots import *
create_world(avenues = 8, streets = 8 )
# beepers 스펠링에 유의
hubo = Robot(beepers=1)
hubo.set_trace("red")
hubo.set_pause(0.2)
hubo.drop_beeper()
hubo.move()
# while안에 if문 구성하는 아이디어에 익숙해지자! 중요하다!
while not hubo.on_beeper() : 
    if hubo.front_is_clear():
        hubo.move()
    else :
        hubo.turn_left()
hubo.turn_left()    
