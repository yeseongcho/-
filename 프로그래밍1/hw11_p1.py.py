"""
Name : 조예성
Studen ID : 21600685
Description : 0/1 Knapsack problem을 해결하는 과정에서 아이템들의 리스트를 깊이에 맞게 실시간으로 보여주고 그 최종 결과값을 산출해주는 프로그램입니다. 메모리를 활용한 경우와 안 한 경우 두 가지 모두 산출하는 프로그램입니다.
"""

# Recursive의 경우
def comp_result(sub_list, avail, count, level) :
    nextitem = sub_list[0] # 가장 앞에 것의 아이템 목록을 가져온다. 
    if nextitem[2] <= avail : # 아이템을 담을지 말 것인지 선택이 가능한 경우
        chosen1, val1, count = bmax_val(sub_list[1:], avail-nextitem[2], count, level) # 깊이 우선 탐색, 선택을 했을 경우를 먼저 탐색한다.
        val1 += nextitem[1] 
        chosen1 = chosen1 + (nextitem,) # tuple of tuple형태 구성
        chosen2, val2, count = bmax_val(sub_list[1:], avail, count, level) # 이후 선택하지 않았을 경우 탐색
        if val1 > val2 : # 아이템을 선택했을 경우와 선택하지 않았을 경우 대비 value가 높은 것 산출
            result = chosen1, val1, count 
        else :
            result = chosen2, val2, count
    else : # weight가 커 아이템을 담을 수 없는 경우
        print(" "*4*(level+1), "No left node") # 다음 아이템을 선택할 수 없음을 표시. 이미 한 단계 깊이가 깊어졌으므로(이 경우 recursive을 통해 level+=1을 할 수 없으므로) level을 한 단계 더 늘려주어야 한다. 
        result = bmax_val(sub_list[1:], avail, count, level) # 계속해서 탐색
    return result
# 현재 어느 부분을 실행하고 있는지 보여주는 함수
def display(list_of_items, weight, level, flag=False) :
    nlist = []
    for item in list_of_items :
        nlist.append(item[0])
    if flag : # flag = True인 경우는 이미, 메모리에 있는 case를 recursive한 경우이다. 
        print(" "*4*level, nlist, weight, "Already solved")
    else : # 메모리에 없는 새로운 case의 경우
        print(" "*4*level, nlist, weight)

# 최종적으로 가장 value가 큰 값을 return하는 함수
def bmax_val(sub_list, avail, count = 0, level = -1) :
    level += 1 #계속해서 bmax_val이 recursive할때마다 즉, 하나씩 깊이가 늘어날때마다 우측으로 한 칸씩 옮겨 적기 위함. display하기 전에 미리 level을 추가해주어야 한다.
    display(sub_list, avail, level, flag=False) # bmax_val이 실행될때마다 리스트를 보여줌. 즉, 현재 어디를 실행하는지를 보여주기 위함
    if sub_list == [] or avail == 0 : # base case
        return (), 0, count # 아이템의 정보와, value, recursive 횟수를 return
    count += 1 # 앞의 base case가 아닌 경우이므로 recursive를 실행하기에 count를 늘려준다.
    result = comp_result(sub_list, avail, count, level) # recursive case
    return result


def bfast_max(sub_list, avail, memo={}, count=0, level = -1) :
    level += 1 # bfast_max가 실행될 때마다 현 아이템 리스트를 우측으로 한 칸씩 옮겨 적기 위함.
    if (len(sub_list), avail) in memo :
        display(sub_list, avail, level, flag=True) # 이미, 메모리에 있는 경우
        return memo[(len(sub_list), avail)] + (count,)
    display(sub_list, avail, level, flag=False) # 현 위치를 보여줌
    if sub_list == [] or avail == 0 : # Base caes
        return (), 0, count
    count += 1 #recursive의 경우 count를 1추가해준다.
    result = fast_result(sub_list, avail, memo, count, level) # recursive case
    memo[(len(sub_list), avail)] = result[0:2] # recursive 실행 결과들을 memory에 저장. 
    return result
# Recursive의 경우
def fast_result(sub_list, avail, memo, count, level) :
    nextitem = sub_list[0] # 가장 앞에 것의 아이템 목록을 가져온다
    if nextitem[2] <= avail : # 아이템을 담을지 말 것인지 선택이 가능한 경우
        chosen1, val1, count = bfast_max(sub_list[1:], avail-nextitem[2], memo, count, level) # 깊이 우선 탐색, 선택을 했을 경우를 먼저 탐색한다.
        chosen1 = chosen1 + (nextitem,) # tuple of tuple형태 구성
        val1 += nextitem[1] 
        chosen2, val2, count = bfast_max(sub_list[1:], avail, memo, count, level) # 이후 선택하지 않았을 경우 탐색
        if val1 > val2 : # 아이템을 선택했을 경우와 선택하지 않았을 경우 대비 value가 높은 것 산출
            result = chosen1, val1, count
        else :
            result = chosen2, val2, count
    else : # weight가 커 아이템을 담을 수 없는 경우
        print(" "*4*(level+1), "No left node") # 다음 아이템을 선택할 수 없음을 표시. 이미 한 단계 깊이가 깊어졌으므로(이 경우 recursive을 통해 level+=1을 할 수 없으므로) level을 한 단계 더 늘려주어야 한다. 
        result = bfast_max(sub_list[1:], avail, memo, count, level) # 계속해서 탐색
    return result


# 기본 제품 list 설정
def create_item_list() :
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    list_of_items = []
    for i in range(len(names)) :
        list_of_items.append((names[i], vals[i], weights[i]))
    
    return list_of_items

def main() :
    items = create_item_list()
    taken, val, count = bmax_val(items, 5) # bmax_val 실행, 최종 value가 높은 선택안이 산출된다.
    print('\n')
    for item in taken : # 최종적으로 선택된 아이템 목록 
        print(item)
    print("Total value of items taken=", val, "count= ", count)

    print('\n')
    taken, val, count = bfast_max(items ,5) # 메모리를 활용하는 경우, bfast_max실행
    print('\n')
    for item in taken : 
        print(item)
    print("Total value of items taken=", val, "count=", count)


main() 
