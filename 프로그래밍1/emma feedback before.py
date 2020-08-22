

def make_dictionary() :
    f = open("./words.txt", "r")
    word_dict = {}
    for word in f :
        wrd = word.strip()
        if 5 <= len(wrd) <= 10 :
            word_dict[wrd] = 0 
    
    f.close()
    return word_dict


def emma(dic) :
    import string
    file = open("./emma.txt", "r")
    
    for line in file :
        if line.startswith("END*THE SMALL PRINT!") :
            break
        for word in line.split() :
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            for voca in word :
                if voca in dic :
                    dic[voca] += 1
    
    
    
    
    
    file.close()
    return dic
    
def make_list(dicts) :
    for element in dicts :
        list1 = []
        list1.append(dicts[element])

    
    return list1

def main() :
    print("1111")
    word_dict = make_dictionary()
    print("1111")
    make_dict = emma(word_dict)
    print("1111")
    final_list = make_list(make_dict)
    print("1111")
    for i in final_list :
        print(i)
        print("1111")

main()



# 왜 element가 1개만 생길까? for line in file 이건 line별로 문장을 읽는 것이 아닌가?
# sorting?
# 설명부분을 제한 반복문 이후에 이어서 하는지? 일단 전제로 코딩을 해보자
