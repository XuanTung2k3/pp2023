import math
import numpy as np

class Base_class():
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def add_info(self):
        pass

class Student(Base_class):
    def __init__(self, id, name, birth, num_stu):
        super().__init__(id, name)
        self.__birth = birth
        self.__num_stu = num_stu
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_birth(self):
        return self.__birth
    def set_birth(self, birth):
        self.__birth = birth
    def get_num_stu(self):
        return self.__num_stu
    def set_num_stu(self, num_stu):
        self.__num_stu = num_stu
    def get_birth(self):
        return self.__birth
    def set_birth(self, birth):
        self.__birth = birth
    def get_num_stu(self):
        return self.__num_stu
    def set_num_stu(self, num_stu):
        self.__num_stu = num_stu
    
    
    def add_info(self):
        __student_info = []
        for i in range(0,self.__num_stu):
            self.__id = input("Enter id of the student {}: ".format(i+1))
            self.__name = input("Enter name of the student {}: ".format(i+1))
            self.__birth = input("Enter date of birth of the student {}: ".format(i+1))
            __student_info.append([self.__id, self.__name, self.__birth])
        return __student_info
        

class Course(Base_class):
    def __init__(self, id, name, num_course, credit):
        super().__init__(id, name)
        self.__num_course = num_course
        self.__credit = credit
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_num_course(self):
        return self.__num_course
    def set_num_course(self, num_course):
        self.__num_course = num_course
    def get_credit(self):
        return self.__credit
    def set_credit(self, credit):
        self.__credit = credit

    def add_info(self):
        __course_info = []
        for i in range(0,self.__num_course):
            self.__id = input("Enter id of the course {}: ".format(i+1))
            self.__name = input("Enter name of the course {}: ".format(i+1))
            self.__credit = input("Enter credit of the course {}: ".format(i+1))
            __course_info.append([self.__id, self.__name, self.__credit])
        return __course_info

class Mark():
    def __init__(self, student_info, course_info):
        self.__student_info = student_info
        self.__course_info = course_info
    def get_student_info(self):
        return self.__student_info
    def set_student_info(self, student_info):
        self.__student_info = student_info
    def get_course_info(self):
        return self.__course_info
    def set_course_info(self, course_info):
        self.__course_info = course_info
    def select_course(self):
        __list_mark_course = [[None for i in range(len(self.__course_info))] for j in range(len(self.__student_info))]
        while True:
            print("Select the course you want to mark: ")
            for i in range(0,len(self.__course_info)):
                print("Course {}: {}".format(i+1, self.__course_info[i][1]))
            select = int(input("Enter the number of the course you want to choose: "))
            if select > len(self.__course_info) or select < 1:
                print("Invalid choice. Please try again.")
            else:  
                print("You have selected course: ", self.__course_info[select-1][1], " (", self.__course_info[select-1][0], ")")          
                for i in range(len(self.__student_info)):
                    mark = float(input("Enter mark of {}: ".format(self.__student_info[i][1])))
                    mark = math.floor(mark*10)/10
                    __list_mark_course[select-1][i] = mark
            print("Enter 0 to stop. Enter other number to continue.")
            if int(input("Enter your choice: ")) == 0:
                break  
        __array_mark_course = np.array(__list_mark_course)
        __array_course_info = np.array(self.__course_info)
        return __list_mark_course, self.__course_info, self.__student_info, __array_mark_course, __array_course_info
    
    def gpa_stu(self, array_mark_course, array_course_info):
        __gpa_stu = np.zeros(len(self.__student_info))
        for i in range(len(self.__student_info)):
            sum_credit = 0
            for j in range(len(self.__course_info)):
                if array_mark_course[j,i] != np.NaN:
                    sum_credit += int(array_course_info[j, 2])
                    __gpa_stu[i] += array_mark_course[j,i]*int(array_course_info[j, 2])
                else:
                    continue
            __gpa_stu[i] = __gpa_stu[i]/sum_credit
        return __gpa_stu
    
    def sort_gpa(self, gpa_stu):
        __sort_gpa = np.sort(gpa_stu)[::-1]
        return __sort_gpa

    
def count_number_student():
    num_stu = int(input("Enter the number of student: "))
    return num_stu

def count_number_course():
    num_course = int(input("Enter the number of course: "))
    return num_course

def main():
    num_stu = count_number_student()
    num_course = count_number_course()
    student = Student(0, "", "", num_stu)
    course = Course(0, "", num_course, 0)
    student_info = student.add_info()
    course_info = course.add_info()
    mark = Mark(student_info, course_info)
    list_mark_course, course_info, student_info, array_mark_course, array_course_info = mark.select_course()
    print("")
    print("")
    print("List of marks of students in each course:")
    for i in range(len(course_info)):
        print("Course: ", course_info[i][1], "(", course_info[i][0], ")", " - Credit: ", course_info[i][2] )
        for j in range(len(student_info)):
            print("     Student: ", student_info[j][1])
            print("     ID: ", student_info[j][0])
            print("     Date of birth: ", student_info[j][2])
            if list_mark_course[i][j] == None:
                print("     Mark: Not marked")
            else:
                print("     Mark: ", list_mark_course[i][j])
            print("")
    print("You want to see the GPA of a specific student or the GPA of all students?")
    print("Enter 0 to see the GPA of a specific student.")
    print("Enter 1 to see the GPA of all students in descending order.")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Enter the ID of the student you want to see the GPA: ")
        id_stu = input("Enter the ID: ")
        for i in range(len(student_info)):
            if student_info[i][0] == id_stu:
                print("The GPA of student {} is: {}".format(student_info[i][1], mark.gpa_stu(array_mark_course, array_course_info)[i]))
                break
    else:
        print("The GPA of all students in descending order: ")
        for i in range(len(mark.sort_gpa(mark.gpa_stu(array_mark_course, array_course_info)))):
            print("Student {}: {}".format(i+1, mark.sort_gpa(mark.gpa_stu(array_mark_course, array_course_info))[i]))

if __name__ == "__main__":
    main()

                
