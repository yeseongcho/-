"""
file = open("./mid_term2.txt", "w")
for i in range(5) :
    name = input("Enter your name and score : ")
    file.write(name + "\n")

file.close()
"""

def function() :
    list_students = []
    file = open("./mid_term2.txt", "r")
    for line in file :
        line = line.rstrip()
        record = line.split(",")
        record[1] = int(record[1])
        record[2] = int(record[2])
        student = tuple(record)
        list_students.append(student)
    file.close()
    return list_students

def function2(student_records) :
    student_records.append(("Carrol Johnson", 80, 98))
    student_records.sort(key = lambda item : (item[2], item[1]), reverse = True )
    return student_records

def display_list(list_of_items) :
    for item in list_of_items :
        student, math, science = item
        print("%-15s %3d %3d" % (student, math, science))

def main() :
    list1 = function()
    list2 =function2(list1)
    display_list(list2)

main()
