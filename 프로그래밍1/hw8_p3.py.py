"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 사용자의 요구에 따라 물건을 구매하기 전의 재고와 판매 이후의 재고량을 판매량과 함께 보여주는 프로그램입니다.
"""

# 재고량을 불러옴
def load_stock(filename) :
    file = open(filename, "r")
    stock_list1 = []
    for line in file :
        line = line.strip()
        item = line.split(",")
        item[1] = int(item[1])
        item[2] = int(item[2])
        stock_list1.append(item)
    file.close()
    stock_list1.sort()
    return stock_list1

# 바뀐 재고량을 반영하여 저장
def store_stock(stock_list1) :
    file = open("stock.txt", "w")
    for line in stock_list1 :
        line[1] = str(line[1])
        line[2] = str(line[2])
        item = ",".join(line) + "\n"
        file.write(item)
    file.close()

# 구매하고자하는 물품을 입력받는 함수
def take_name(stock_list1) :
    while True :
        name = input("What do you want to buy? >>>")
        for item in stock_list1 :
            if item[0] == name :
                return item # 구매하고자 하는 물품 return
        print("Sorry, we do not have a stock for " + name + ".")
        res = input("Do you want to buy other item? (y/n) >>>")
        if res == "n" :
            return None # 다른 물품을 구매하길 원치 않는 경우 None return - 이 경우 다시 맨 처음 메뉴로 돌아온다.

# 구매하고자 하는 물품의 수량을 입력받는 함수
def take_quant(item) :
    while True :
        try :
            qty = int(input("How many? >>>"))
            if qty > item[2] : # 재고 이상의 양을 입력했을 경우
                print("Sorry, we have only %5d items." % item[2])
                while True :
                    res = input("Would you buy? (y/n)>>>") # 재고 전부의 양을 구매할 건지를 묻는 경우
                    if res == "y" :
                        return item[2]
                    elif res == "n" :
                        return 0
                    else :
                        print(res + "?", "Please, retype in")
            return qty 
        except :
            print("Type in a number. >>>")


# 물품의 이름과 수량을 입력받는 함수를 호출하고 구매할 여부를 정하는 최종 함수.
def take_input(stock_list1) :
    item = take_name(stock_list1)
    if item != None :
        quant = take_quant(item)
    else :
        quant = 0
    return item, quant

# 사용자가 메뉴창에서 'S'를 입력시 실행되는 함수로서, take_input에서 얻어낸 자료를 바탕으로, 구매 물품의 이름, 가격, 판매량과, 그 매출로 구성된 리스트 구성.
def sell(stock_list1, sales_hist1) :
    item, quant = take_input(stock_list1)
    if item == None or quant == 0 :
        return
    item[2] -= quant # 판매량만큼 재고에서 차감
    amount = item[1]*quant # 가격과 판매량을 곱해 매출 산출
    print("item = ", item[0], "; price = ", item[1], "; quanity = ", quant, "; amount = ", amount)
    sales_hist1.append((item[0], item[1], quant, amount))

# 사용자가 메뉴창에서 'P'를 입력시 실행되는 함수로서, 상품의 정보(가격,이름)와 남은 재고, 그 재고당 판매가를 곲한 액수를 보여줌
def print_stock(stock_list1) :
    print("\n", " "*20 + "STOCK REPORT")
    print("Name         price    quantity               amount")
    for item in stock_list1 :
        print("%-10s    %5d     %5d                %6d" % (item[0], item[1], item[2], item[1]*item[2]))
# 사용자가 메뉴창에서 'R'를 입력시 실행되는 함수로서, 프로그램이 실행되는 동안 얼마만큼 팔았는 지를 보여주는 함수 
def print_sales(sales_hist1) :
    print(" "*20 + "SALES REPORT")
    print("Name         price   quantity        amount")
    for item in sales_hist1 :
        print("%-10s  %5d  %5d    %15d" % (item[0], item[1], item[2], item[3]))
# 초기 메뉴를 보여주는 함수 구성
def show_menu() :
    print("\n", "What would you like to do?")
    print("   S: Sell an item")
    print("   P: Print stock")
    print("   R: Report sales")
    print("   E: Exit")
    return input("Enter your choice (S, P, R, or E))>>>")
# 메뉴창에서 S, P, R, E를 제외한 다른 값을 입력했을 시 오류를 산출하는 함수
def input_error(s) :
    print(s + "?" + "I beg your pardon.")


def main() :
    stock_list = load_stock("stock.txt") # 재고량을 불러옴
    sales_hist = [] # 후에 제품의 매출을 기록하기 위한 리스트
    while True :
        s = show_menu()
        if s == "E" :
            break
        elif s == "S" :
            sell(stock_list, sales_hist)
        elif s == "P" :
            print_stock(stock_list)
        elif s == "R" :
            print_sales(sales_hist)
        else :
            input_error(s)
    store_stock(stock_list) # 재고량 변화 반영

main()
