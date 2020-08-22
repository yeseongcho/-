from cs1graphics import *
paper = Canvas(500, 400)
event = paper.wait() # 이 녀석을 통해 GUI 구현한다.
ball = Circle(15, event.getMouseLocation()) # 마우스의 위치에 원을 위치시킴
ball.setFillColor('red')
paper.add(ball)
while True :
    event = paper.wait()
    if event.getDescription() != "mouse click" : #만일 마우스클릭이 아닌 다른 값이 사용된다면 프로그램 종료
        
        break
    new_pos = event.getMouseLocation() # 마우스 입력 위치를 받아 원의 위치로 움직이게 한다.
    ball.moveTo(new_pos.getX(), new_pos.getY())
paper.close()
