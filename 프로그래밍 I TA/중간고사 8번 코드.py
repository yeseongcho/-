
def show_list(list_of_items):
    for item in list_of_items:
        student, math, science = item
        print ("%-15s %3d %3d" % (student, math, science))

 

def append_and_sort(items_list):
    items_list.append(("Carrol Johnson", 80, 98))
    items_list.sort(key = lambda record: (record[2],record[1]), reverse = True)
    return items_list

 

def build_a_list():
    list_of_items = []
    file = open("mid_term2.txt", "r")
    for item in file:
        item = item.rstrip()
        item = item.split(",")
        item[1] = int(item[1])
        item[2] = int(item[2])
        item = tuple(item)
        list_of_items.append(item)

    file.close()

    return list_of_items

   

def main():
    list_a = build_a_list()
    print(list_a)
    list_b = append_and_sort(list_a)
    print(list_b)
    show_list(list_b)

 

main()
