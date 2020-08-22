from cs1robots import *
load_world("worlds/myworld.wld")
hubo = Robot(avenue = 1, street = 1)
hubo.set_pause(0.1)
hubo.set_trace("red")
def turn_right() :
    for i in range(3):
        hubo.turn_left()

def move_east() :
    while hubo.front_is_clear():
        if hubo.on_beeper():
            while hubo.on_beeper():
                hubo.pick_beeper()
        else :
            hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    if not hubo.front_is_clear() :
        hubo.turn_left()
        while hubo.front_is_clear():
            if hubo.on_beeper():
                while hubo.on_beeper():
                    hubo.pick_beeper()
            hubo.move()
   

def move_west() :
    while hubo.front_is_clear():
        if hubo.on_beeper():
            while hubo.on_beeper():
                hubo.pick_beeper()
        else :
            hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    if not hubo.front_is_clear() :
        turn_right()
        while hubo.front_is_clear():
            if hubo.on_beeper():
                while hubo.on_beeper():
                    hubo.pick_beeper()
            hubo.move()
    

while True :
    move_east()
    move_west()
        
