"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 word파일에 있는 길이가 5에서 10사이인 단어 중 가장 많이 emma에 나타난 상위 20개의 단어를 그 수와 함께 출력하는 함수입니다.
"""

# word파일에 있는 길이가 5에서 10사이에 있는 단어들의 사전을 만듦. 갯수는 0
def make_dictionary() :
    f = open("./words.txt", "r")
    word_dict = {}
    for word in f :
        wrd = word.strip()
        if 5 <= len(wrd) <= 10 :
            word_dict[wrd] = 0 
    
    f.close()
    return word_dict

# 문장별로 읽어와 해당 단어와 그 갯수를 읽어오는 함수
def emma(dic) :
    
            
    import string
    file = open("./emma.txt", "r")
    
    for line in file : # 처음 서문 부분은 읽기에서 제외한다.
        if line.startswith('*END*THE SMALL PRINT!') :
            break     
 
    for word in file : # 문장 별로 string을 읽어온다.
        word = word.strip(string.whitespace+string.punctuation) # strip!은 양 끝에 있는 녀석들만 제거한다! 가운데 곳곳에 있는 것은 제거할 수 없다!
        word = word.lower() 
        # 단어들 사이에 붙어있는 특수기호들을 전부 제거한다. (ex) could,와 같은 요소의 경우 ,를 제거해야 could를 읽음
        word = word.replace(',', " ")
        word = word.replace('-', " ")
        word = word.replace('!', " ")
        word = word.replace('?', " ")
        word = word.replace('.', " ")
        word = word.replace(':', " ")
        word = word.replace(';', " ") # string은 기본적으로 immutable하지만 replace라는 method가 있음에 주의!
        word = word.replace('_', " ")
        word = word.replace('*', " ")
        word = word.replace('^', " ")
        word = word.replace('~', " ")
        word = word.replace('"', " ")
        word = word.replace("'", " ")
        word = word.replace("=", " ")
        word = word.replace('(', " ")
        word = word.replace(')', " ")
        word = word.replace('{', " ")
        word = word.replace('}', " ")
        word = word.replace('/', " ")
        # 해당 string을 공백을 기준으로 나눈 리스트로 전한
        word = word.split()
        # 해당 리스트의 element가 입력받은 사전 안에 있을 시 count
        for voca in word :
            if voca in dic :
                dic[voca] += 1

    
    file.close()
    return dic

# 수를 추가한 사전을 tuple element로 구성된 리스트로 전환하는 함수    
def make_list(dicts) :
    list1 = []
    for element in dicts :
        
        list1.append((element, dicts[element]))

    
        
    return list1

# 해당 리스트를 그들의 빈도수가 많은 순으로 sort하는 함수
def sorting(s_final_l) :

    s_final_l.sort(key = lambda item : item[1], reverse = True)

    return s_final_l
    
    




def main() :
    
    word_dict = make_dictionary()
    
    make_dict = emma(word_dict)
    
    semi_final_list = make_list(make_dict)
    
    final_list = sorting(semi_final_list)
    # 해당 단어와 그 빈도수 산출
    for i in range(20) :
        print("%s  %d" % (final_list[i][0], final_list[i][1])) 
        

main()





