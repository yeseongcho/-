f = open("files/planets.txt", "r")
list1 = []
for line in f :
    s = line.strip()
    print(s, end=" ")

f.close()
