f = open("./words.txt", "r")
# 알파벳 순으로 되어있는지 판별하는 함수
def is_abcderian(wrd) :
    arrange = [] 
    word_in_list = list(wrd) #입력받은 wrd를 리스트로 변환
    for i in range(len(wrd)) :
        arrange.append(wrd[i])
    arrange.sort() # arrange라는 리스트에 사전순으로 되어 있게 정리
    
    if arrange == word_in_list : # 이 정리한 값이 기존 wrd와 일치하면(equivalent하면) true값 반환
        return True
    else :
        return False


def main() :
    count = 0
    for word in f :
        wrd = word.strip()
        if is_abcderian(wrd) :
            print(wrd)
            count += 1
    print("no.of count: ", count)

main()
f.close()
