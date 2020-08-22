
fruits_dict = {"Apple": 800, "Grape":1000, "Persimmon":300, "Pear": 1500, "Chestnut":50}

new_tuple = tuple()

new_dict = dict()

new_list = list()

for item in fruits_dict:
    new_tuple = new_tuple + ((fruits_dict[item], item),)
    new_list.append([item, fruits_dict[item]])
    new_dict[fruits_dict[item]] = item

print("number 9")
print (new_tuple)
print('\n')
print("number 10")
print (new_list)
print('\n')
print('number 11')
print (new_dict)
