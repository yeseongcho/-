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
        print(score, end = " ")
        for i in range(len(dictionary[score]) :
            print(dictionary[score][i]. end = " ")
        print(" ") # 마지막 for문을 실행해주고 빠져나올때 문장이 end로 끝나게되면 다시 다음 반복문을 실시할때 end=" "이므로 라인을 붙여서 실행하게 된다. 이를 막아주기 위해 이 행을 실행!

def main() :
    trans_list = (["Korean", 90], ["English", 85], ["Math.", 90], ["Science", 85], ["History", 90], ["Economics", 95])
    inverted_dict = conversion_to_dict(trans_list)
    display_dict(inverted_dict)
    print(90, inverted_dict[90])
    courses = inverted_dict.pop[85]
    print(courses)
    MaxSoFar = -1
    for score in inverted_dict :
        MaxSoFar = max(MaxSoFar, score)
    print(inverted_dict[MaxSoFar]

main()
                       
                    
