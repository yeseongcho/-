def conversion_to_dict(transcript) :
    invrs_dict = dict()
    for subject in transcript :
        if subject[1] not in invrs_dict :
            invrs_dict[subject[1]] = [subject[0]]
        else :
            invrs_dict[subject[1]].append(subject[0])
    return invrs_dict

def display_dict(dictionary) :
    for score in dictionary :
        print(score, end = " ") # - 1
        for i in range(len(dictionary[score])) :
            print(dictionary[score][i], end = " ")
        #print("\n") - 이 경우 end로 끝나고 한칸 띄고 또 한칸 띄어 # - 1실행
        print(" ") # 이 경우 end = " "로 끝나는 걸 막아줌
        #아예 안쓴 경우 - 이 경우 end = " "가 지속되므로 이어 써준다.
def main() :
    
    trans_list = (["Korean", 90], ["English", 85], ["Math.", 90], ["Science", 85], ["History", 90], ["Economics", 95])
    inverted_dict = conversion_to_dict(trans_list)
    display_dict(inverted_dict)
    print(90, inverted_dict[90])
    courses = inverted_dict.pop(85)
    print(courses)
    MaxSoFar = -1
    for score in inverted_dict :
        MaxSoFar = max(MaxSoFar, score)
    print(inverted_dict[MaxSoFar])     
                       
main()       
