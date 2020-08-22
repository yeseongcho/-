"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 삼각함수를 시계방향으로 90도 꺾은 그래프를 불연속적인 점으로 나타내는 프로그램입니다.
"""

# 단, 이 함수를 읽을 때는 맨 아래쪽인 main함수부터 순차적으로 읽는 것을 권장!!



import math

def plot_graph(no_of_symbols) :
    if no_of_symbols < 40 : # 이 경우 main함수의 rad가 pie에서 2pie로 변하는 구간을 의미.(line 33과 동일 ) 최종그림에서는 x축 밑부분을 의미한다.
        if no_of_symbols == 0 : # 특별히 0의 경우는 rad가 3/2pie값을 가지며(val = -1인 경우)  이 경우는 "#"이 그림상 가장 좌쪽에 찍히게 된다.  
            bar = "#" + " " * 38 +"I" 

        else : # 그렇지 않는 경우는 x축 기준 아래쪽의 그림을 나타내기 위함. (no_of_symbol은 0에서 40까지 변화한다.)
            bar = " "*(no_of_symbols-1) + "#" + " "*(39-no_of_symbols) + "I"

    elif no_of_symbols == 40 : # val이 0일때, 즉 rad가 0, pie, 2pie일때인데 pie일때의 경우는 compute_and_plot에서 계산하였으므로( 이 경우는 radian이 pie일때인데 그 경우는 이미 47번재 줄의 else에 의해 고려하지 않음)  0, 2pie일때의 경우를 고려
        bar = " "*39 + "#" # 이 경우는 y축 위에 #하나만 체크해준다.

    else : # 이 경우는 main 함수의 rad가 0에서 pie까지 변하는 구간.(line 36과 동일) 최종그림상에서는 x축 기준 위쪽을 의미.
        bar = " "*39 + "I" + " " *(no_of_symbols - 41) + "#"

    print(bar)

def count_no_of_symbols(angle) : # 여기 angle은 compute_and_plot함수의 radian값을 agrument로 갖음

    val = math.sin(angle) #val은, 즉 main함수에서 rad가 변함에 따라 갖는 sin값임.

    if val < 0 : # sin값이 0보다 작은 구간은 rad가 pie에서 2pie로 변하는 구간을 의미.
        no_of_symbols = int((val*40)-0.5) + 40 # 여기서 no_of_symbol은 0에서 40까지의 값을 가짐(단, 여기서 40인 val이 0일때므로 제외)

    else : # 이 경우는 sin값이 0보다 큰 구간, 즉 rad가 0에서 pie까지 변하는 구간을 의미
        no_of_symbols = int((val*40)+0.5) + 40 # no_of_symbol은 40에서 81까지 변함(여기서는 40을 포함,val이 0인 것을 포함하므로)

    return no_of_symbols 

def compute_and_plot(radian) : #rad를 radian이란 parameter로 갖음

    if radian == math.pi : # 즉 rad값이 pie인 경우, 이 경우는 최종 그림 상 x축을 그려주는 경우를 의미
        print("-"*39 + "#" + "-"*40) # x축을 그려주고 40번째에 "#"을 넣어준다.

    else :
        num_of_symbols = count_no_of_symbols(radian) # rad가 파이를 갖는 경우를 제외하고는 그 값들을 count_no_of_symbol이란 함수에 넣어주어 결과값을 num_of_symbol로 산출

        plot_graph(num_of_symbols) # num_of_symbol값을 plot_graph에 넣어줌.

def main() :
    for i in range(41) :

        rad = (2*math.pi/40)*i # 0~2파이까지 총 20등분을 해서 불연속적인 값 rad를 갖는다. (1pie/20 ~ 40pie/20 )

        compute_and_plot(rad) # compute_and_plot 함수의 argument로 취한다.


main()
