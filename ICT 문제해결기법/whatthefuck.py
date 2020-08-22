def add(lst2) :
    lst2.append(4)
    return lst2

lst = [1, 2, 3]

lst2 = lst

lst2 = add(lst2)

print(lst)

print(lst2)
