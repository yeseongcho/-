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
        if line.startswith('*END*THE SMALL PRINT') :
            break

    line = file.read()    
    word = line.strip(string.punctuation + string.whitespace)
    word1 = word.lower()
    word2 = word1.split()

    
    
    for voca in word2 :
        if voca in dic :
            dic[voca] += 1
            
            
        
    
    
    
    file.close()
    return dic

def make_list(dicts) :
    list1 = []
    for element in dicts :
        list1.append((element, dicts[element]))
    return list1

def sorting(s_final_l) :

    s_final_l.sort(key = lambda item : item[1], reverse= True)

    return s_final_l    
    

dictionary = make_dictionary()
final_dict = emma(dictionary)
final_dict1 = make_list(final_dict)
final_dict2 = sorting(final_dict1)
for i in range(20) :
    print(final_dict2[i])


