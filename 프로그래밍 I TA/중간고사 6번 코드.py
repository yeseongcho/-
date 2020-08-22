def tuple_to_dict(trans_tup) :
    score_dict = dict()
    for item in trans_tup :
        if item[1] not in score_dict :
            score_dict[item[1]] = [item[0]]
        else :
            score_dict[item[1]].append(item[0])
    return score_dict

def show_dict(score_dic) :
     for score in score_dic :
         print(score, end = " ")
         for i in range(len(score_dic[score])) :
             print(score_dic[score][i], end = " ")
         print(" ")

def main():
    trans_tuple = (["Korean", 90], ["English", 85],["Math.", 90], ["Science", 85],["History", 90], ["Economics", 95])    
    score_dic = tuple_to_dict(trans_tuple)
    print(score_dic)
    print("###")

    show_dict(score_dic)
    print (90, score_dic[90])

    subjects = score_dic.pop(85)
    print(subjects)

    MaxSoFar = -1
    for score in score_dic:
        MaxSoFar = max(MaxSoFar, score)

    print(score_dic[MaxSoFar])

 

main()
    
