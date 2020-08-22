class Stock:
    #def __init__(self):
    stock_list = {}    

    def load_file(self,stock_file):
        file = open(stock_file,'r')
        for line in file:
            item = Item(line)
            '''
            line = line.strip()
            item = line.split(',')
            item[1] = int(item[1])
            item[2] = int(item[2])
            '''
            self.stock_list[item.name] = (item.price,item.quantity)
        file.close()
        return self.stock_list

    def store_file(self):
        file = open('stock.txt','w')
        for name in self.stock_list:
            line = self.stock_list[name]
            item = (name,str(line[0]),str(line[1]))
            item=','.join(item)+'\n'
            file.write(item)
        file.close()

    def print_stock(self):
        print('\n',' '*20+'STOCK REPORT')
        print('Name        price  quantity      amount')
        for name in self.stock_list:
            item= self.stock_list[name]
            print('%-10s  %5d   %5d       %8d'%(name, item[0], item[1], item[0]*item[1]))

    def find_stock(self,name):
        if name in self.stock_list:

            return name
        return None

    def current_stock(self,name):
        return self.stock_list[name]
        
    def update_stock(self,name,quant):
        item = self.stock_list[name]
        self.stock_list[name] -= self.stock_list[name]-quant


class Item(Stock):
    def __init__(self,line):
        line = line.strip()
        item = line.split(',')
        item[1] = int(item[1])
        item[2] = int(item[2])
        self.name = item[0]
        self.price = item[1]
        self.quantity = item[2]

    #이거 언제씀?
    def display(self):
        print('%-10s  %5d   %5d       %8d'%(self.name,self.price,self.quantity,self.price*self.quantity))

#Transaction여기가 sell에 들어가야 될 것 같은데..
##막힘 
#Stock에 이름 object 없대.. name이 stock에서 시작 되는 것 같음데 
class Transaction():
    def __init__(self,stock_list,stock,quantity):
        name = take_name(stock_list)
        #팔고 남은 재고의 양 
        self.quantity = stock.update_stock(name,quantity)
        #판 아이템의 이름 
        self.name = stock.find_stock(name)
        #판 아이템의 가격
        self.unitprice = stock.stock_list[name][1]

    def __str__(self):
        return '%-10s  %5d   %5d       %8d'%(stock.name,self.unitprice,self.quantity,self.unitprice*self.quantity)

    #판매 했을 때  
    def display(self):
              print('item =',self.name,'; price=',self.unitprice,'; quantity=', self.quantity,'; amount =',self.unitprice*self.quantity)

########지금 여기서 막힘 
def sell_item(stock_list,sales_hist):
    name = take_name(stock_list)
    if name == None:
        return
    quantity = take_quant(stock_list,name)
    if quantity == 0:
        return
    current_stock = stock_list[name]
    transaction = Transaction(stock_list,stock,quantity)
    transaction.display()
    sales_hist.append((name,transaction.unitprice,transaction.quantity))
    

def take_name(stock_list):
    stock = Stock() 
    #stock_list= stock.load_file('stock.txt')
    while True:
        name = input('What you want to buy? >>>')
        r_name = stock.find_stock(name)
        #print(r_name)
        if r_name == name:
            return name
        print('Sorry, we do not have a stock for' + name+ '.')
        res = input('Do you want to buy other item? (y/n)>>>')
        while True:
            if res =='n':
                return None
            elif res == 'y':
                break
            else:
                res = input(res + '? Please type in (y/n)>>>')
                
def take_quant(stock_list,name):
    while True:
        try:
            qty = input ('How many? >>>')
            qty = int(qty)
            stock = Stock()
            stock_list= stock.load_file('stock.txt')
            item = stock.current_stock(name)
            if qty <= 0:
                print(str(qty) + '?Please type in a positive number.')
            elif qty <=item[1]:
                return qty
            elif item[1] <qty:
                if item[1]==0:
                    print('Sorry, we do not have any stock.')
                    return 0
                else:
                    print('Sorry, we have only %5d items.'%item[1])
                    res = input('Would you buy? (y/n)>>>')
                    while True:
                        if res == 'y':
                            return item[1]
                        if res == 'n':
                            return 0
                        res = input(res + '? Type in (y/n). >>>')
        except:
            print(qty + '? Please type in a number.')



def print_sales(sales_hist):
    print(' '*20 + 'SALES REPORT')
    print('Name     price   quantity       amount')
    for item in sales_hist:
        print('%-10s  %5d   %5d       %8d'%(item[0],item[1],item[2],item[1]*item[2]))

def show_menu():
    print('\n','What would you like to do?')
    print(' S: Sell an item')
    print(' P: Print stock')
    print(' R: Report sales')
    print(' E: Exit')
    return input ("Enter your choice (S, P, R, or E)>>>")

def input_error(message):
    print(message+ '?' + 'I beg your pardon.')

                    
                    
def main():
    stock= Stock()
    stock_list= stock.load_file('stock.txt')
    print(stock_list)
    sales_hist = []
    while True:
        s = show_menu()
        if s =='E':
            break
        elif s =='S':
            sell_item(stock_list,sales_hist)
        elif s =='P':
            stock.print_stock(7)
        elif s =='R':
            print_sales(sales_hist)
        else:
            input_error(s)
    stock.store_file()

main()
