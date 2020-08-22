"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 Object Oriented Programm을 활용해 가게의 재고와 매출 현황을 나타내는 프로그램입니다.
"""


# 재고 관리
class Stock :
    # 파일을 불러옴
    def __init__(self) :
        file = open("stock.txt", "r")
        stock_dict1 = {}
        for line in file :
            line = line.strip()
            item = line.split(",")
            item[1] = int(item[1])
            item[2] = int(item[2])
            value_list = [] # 가격과 양의 리스트를 따로 추가해줌
            value_list.append(item[1])
            value_list.append(item[2])
            stock_dict1[item[0]] = value_list # 품명의 속성으로 부여
        file.close()
        self.firststock = stock_dict1 # 초기 재고를 설정한다.
        
    # 구매 후 남은 재고를 파일에 저장하기 
    def store_stock(self, stock_dict1, items) : # 구매 후의 재고를 인자로 갖음.
        if items == None :
            return None
        else :
            
            file = open("stock.txt", "w")
            for line in stock_dict1 :
                list1 = [] # line별로 ,로 구분된 string으로 만들기 위한 리스트 생성
                stock_dict1[line][0] = str(stock_dict1[line][0])
                stock_dict1[line][1] = str(stock_dict1[line][1])
                list1.append(line)
                list1.append(stock_dict1[line][0])
                list1.append(stock_dict1[line][1])
                item = ",".join(list1) + "\n" # ,로 구분된 string을 열별로 구성
                file.write(item)
            file.close()
            return stock_dict1

# 물건 판매
class Sell : # 입력받은 items는 [물품이름, 사고자하는 양]으로 구성된 리스트이다.(구매 리스트) ex) [apple, 10]
    def __init__(self, stock_dict1, items, sales_hist) :
        # 물품을 판매한 경우 기존의 재고에서 차감
        self.residual = int(stock_dict1[items[0]][1]) - int(items[1]) 

    # 물품 판매 후 변화한 재고를 반영
    def make_change(self, stock_dict1, items, sales_hist) :
        stock_dict1[items[0]][1] = self.residual
        return stock_dict1

    # 판매 이후 장부에 판매 기록 
    def write(self, stock_dict1, items, sales_hist) :
        sales_hist.append((items[0], stock_dict1[items[0]][0], items[1], int(stock_dict1[items[0]][0])*int(items[1])))
        return sales_hist
   

# 남은 재고를 보여줌
class Print :
    def __init__(self, stock_dict1) :
        self.printing = stock_dict1 # 재고를 속성으로 갖음

    def __str__(self) :
        # 초기 메뉴를 보여줌
        print("\n", " "*20+"STOCK REPORT")
        print("Name          price          quantity         amount")
        # 남은 품목을 보여줌
        for item in self.printing :
            print("%-10s %10d %10d %20d" % (item, int(self.printing[item][0]), int(self.printing[item][1]), int(self.printing[item][0])*int(self.printing[item][1])))
        return " " # __str__의 return값

# 장부 기록을 보여줌
class Report :

    def __init__(self, sales_hist, items1) : # 장부와 구매 리스트를 인자로 갖음
        self.reporting = sales_hist # 장부를 속성으로 갖음
    def __str__(self) :
        print(" "*20 + "SALES REPORT")
        print("Name           price       quantity           amount")
        for item in self.reporting :
            print("%-10s %10d %10d %20d" % (item[0], int(item[1]), int(item[2]), int(item[3])))
        return " "

# 물건을 고름
class Transaction :
    def returns(stock_dict1, items) :
        while True :
            choice = input("What do you want to buy? >>>")
            for item in stock_dict1 : 
                if item == choice : # 재고에 입력받은 물건이 있는 경우
                    items.append(item) # 구매 리스트에 추가
                    return items
            print("Sorry, we do not have a stock for" + " "+ choice+".") # 물품이 없는 경우
            res = input("Do you want to buy other item? (y/n) >>>") 
            if res == "n" :
                return None # 이 경우 구매자가 추가로 물품을 구입하기 원하지 않는 경우 - 다시 메인 화면으로 돌아가기 위한 None값 반환
    
        
# 수량을 정함                
class Buying :
    def buying(stock_dict1, items) :
        if items == None : # 앞서 추가로 물품을 구입하기 원치 않는 경우는 구매 리스트를 None으로 반환해 다시 메인 화면으로 돌아감 
            return None
        while True :
            try :
                quant = int(input("How many?>>>")) # 수량을 입력받음
                
                if quant > int(stock_dict1[items[0]][1]) : # 입력받은 수량이 재고의 량보다 많은 경우
                    
                    print("Sorry, we have only %5d items." % int(stock_dict1[items[0]][1]))
                    
                    while True :
                        res = input("Would you buy? (y/n) >>>") # 남은 재고의 전부를 사기 원하는 지를 묻는 경우
                        if res == "y" :
                            items.append(stock_dict1[items[0]][1])
                            return items
                        
                        elif res == "n" : # 그렇지 않은 경우 역시 메인으로 돌아가기 위한 None값 반환
                            return None
                        else :
                            print(res+"?", "Please, retype in")
                
                items.append(quant) # 수량이 초과되지 않는 경우
                
                return items
            except : # 수가 아닌 다른 값을 입력받았을 때
                print("Type in a number. >>>")
# 메인 화면                
def show_menu() :
    print("\n", "What would you like to do?")
    print("   S: Sell an item")
    print("   P: Print stock")
    print("   R: Report sales")
    print("   E: Exit")
    return input("Enter your choice (S, P, R, or E))>>>")

# 메인 화면에서 올바르지 않은 값을 입력했을 때
def input_error(s) :
    print(s + "?" + "I beg your pardon.")

# 물품을 구매한 뒤 구매한 물품의 정보를 보여줌
class Show :
    def __init__(self, final_stock, items) :
        # 구매 리스트와 재고를 인자로 갖음
        self.item = items
        self.stock = final_stock

    def __str__(self) :
        return "item = %-5s ; price = %-5d ; quantity = %-5d ; amount = %-5d" % (self.item[0], int(self.stock[self.item[0]][0]), int(self.item[1]), int(self.stock[self.item[0]][0])*int(self.item[1]))
    



def main() :
    stock = Stock() # 재고 불러옴
    items = [] # 구매 리스트 생성
    sales_hist = [] # 장부 생성
    
    
    
    
    while True :
    
        s = show_menu()
        
        if s == "E" :
            break
        elif s == "S" :
            # 품목 선택
            items = Transaction.returns(stock.firststock, items)
            # 수량 선택
            items = Buying.buying(stock.firststock, items)
            
            # 구매를 원치 않는 경우
            if items == None :
                print("Show menu again")
                items = [] # None값으로 반환된 items를 초기화 하기 위해
            # 구매하는 경우
            else :
                # 판매
                sell = Sell(stock.firststock, items, sales_hist)
                # 장부 작성
                sales_hist = sell.write(stock.firststock, items, sales_hist)
                # 판매를 통한 재고 수정
                final_stock = stock.store_stock(sell.make_change(stock.firststock, items, sales_hist), items)
                show = Show(final_stock, items)
                items1 = items # 그동안의 구매 기록들을 모아놓기 위해
                if items == None :
                    print("Show menu again")
                    items = [] 
                else :
                    print(show)
                    
                    items = [] # 판매 리스트는 장부 수정이후 최신화
                
                
        elif s == "P" :
            prints = Print(stock.firststock)
            print(prints)
        elif s == "R" :
            items1 = items
            reports = Report(sales_hist, items1)
            
            print(reports)
            
        else :
            input_error(s)

    

main()




    
    
