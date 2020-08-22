fp = open("C:/Users/sec/Desktop/te.txt")

for word in fp :
    word.strip()
    print(word)
    print("###")
    break


for word in fp :
    print(word)
