fruits = {"Apple" : 800, "Grape" : 1000, "Persimmon" : 300, "Pear" : 1000, "Chestnut" : 50}
tuple1 = tuple()
dict1 = dict()
list1 = list()
for item in fruits :
    tuple1 = tuple1 + ((fruits[item], item), )
    list1.append([item, fruits[item]])
    dict1[fruits[item]] = item
print(tuple1)
print(list1)
print(dict1)
