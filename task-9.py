firstname = input('Enter the firstname of the student: ') #this code asks the user to input his/her firstname
lastname = input('Enter the lastname of the student: ')   #this code asks the user to input his/her lasttname
Studentnumber = input('Enter the studentnumber of the student: ')  #this code asks the user to input his/her studentnumber

my_dict = {''' 'Course1': 'Career Success', 'Course code': 1830 
        'Course2': 'Readind and writing', 'Course code': 4566
        'Course3': 'IT infrastructure', 'Course code': 3908
        'Course4': 'Networking Basics', 'Course code': 7855 '''}  #this code gives the list of the courses.
print(my_dict)  #this code print the dictionary
list = []                                                      
Course_list = input("Please enter course code"  +  " list : ") #user needs to give the courses that he/she wants to register for
list.append(Course_list)
list = Course_list.split(",") #this code puts separate the course in the list 
print('List : ',list)   #this code print the list of the courses that are registered       

print("Student Name:",firstname,lastname) #prints the firstname of the user
print("Student Number:",Studentnumber) #prints the lastname of the user
print("Total no. of courses registered:",len(list))
print("---------------------------------------------")
print("Course registration has been confirmed for the following courses")
if list[0] in list:
    print(list[0])
else:
    pass
if list[1] in list:
    print(list[1])
else:
    pass
if list[2] in list:
    print(list[2])
else:
    pass
if list[3] in list:
    print(list[3])
else:
    pass
