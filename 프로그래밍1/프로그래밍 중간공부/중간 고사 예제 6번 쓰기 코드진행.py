"""
file = open("./mid_term1.txt", "w")
for i in range(6) :
    subject = input("Enter your subject:")
    file.write(subject + "\n")

file.close()
"""

def create_a_dict() :
    file = open("./mid_term1.txt", "r")
    dict_courses = dict()
    for line in file :
        line = line.strip().split(",")
        line[1] = int(line[1])
        dict_courses[line[0]] = line[1]
    file.close()
    print(dict_courses)
    return dict_courses

def read_a_course(dictionary) :
    while True :
        query = input("Enter a courses :")
        if query == "quit" :
            return "quit"
        elif query in dictionary :
            return query
        print(query, "? Not in the dictionary!")

def show_courses(trans_dict, query) :
    if query in trans_dict :
        print(query, trans_dict[query])
    else :
        print(query, "not in the dictionary")

def main() :
    dict_of_courses = create_a_dict()
    while True :
        course = read_a_course(dict_of_courses)
        if course == "quit" :
            break
        else :
           show_courses(dict_of_courses, course)
main()
