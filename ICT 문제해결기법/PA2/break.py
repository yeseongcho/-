num = [1, 2, 3, 4]
g = 5
for i in range(len(num)) :
    while(g > num[i]) :
        print(num[i])
        g = g-1
        if g == 3 :
            break
    print("##")

## break는 자신을 감싸고 있는 한 반복문만 빠져나온다!!
