def build_a_dict():
    file = open("mid_term1.txt", "r")
    dict_subjects = dict()
    for line in file:
        line = line.strip().split(",")
        line[1] = int(line[1])
        dict_subjects[line[0]] = line[1]

    file.close()
    print(dict_subjects)
    return dict_subjects

 

def read_a_subject(sub_dict):
    while True :
        query = input("Enter a course: ")
        if query == "quit":
            return "quit"
        if query in sub_dict:
            return query
        print(query, "?  Not in the dictionary!")

                                     

def show_subjects(subject_dict, query):
    if query in subject_dict:
        print (query, subject_dict[query])
    else:
        print (query, "not in the dictionary")

 

def main():
    dict_of_subjects = build_a_dict()
    while True :
        subject = read_a_subject(dict_of_subjects)
        if subject == "quit":
            break
        else:
            show_subjects(dict_of_subjects, subject)

           

main()
