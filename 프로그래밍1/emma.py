

f = open("./words.txt", "r")
word_dict = {}
for word in f :
    wrd = word.strip()
    if 5 <= len(wrd) <= 10 :
        word_dict[wrd] = 0
f.close()

file = open("./emma.txt", "r")
# 
for line in file :
    if line.startswith("*END*THE") :
        break
# 가정 : line을 읽는 것이 위에 것의 바통을 받아서 이어진다.
for line in file :
    words = line.split()
    words_check = words.strip(string.punctuation + string.whitespace)
    words_check = words_check.lower()
    for voca in words_check :
        if 5<= len(voca) <= 10 :
            if voca in word_dict :
                word_dict[voca] += 1 # 가정 : 이 voca를 그대로의 key값으로 갖는다.
f.close()

for element in word_dict :
    list1 = []
    list1.append((element, word_dict[element])
                 


print(list1[0])





