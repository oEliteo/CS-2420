from UUC import *
import Student
def printName(item, uuc):
    print(item)
    
def main():
    uuc  = UUC()
    student = Student.Student()
    student1 = Student.Student()
    student.setMembers("GREGORY", 'DON', '574-28-3634', 'DON.GREGORY@Dixie.edu', 44)
    student1.setMembers("GREGORY", 'DON', '574-28-3634', 'DON.GREGORY@Dixie.edu', 44)
    uuc.insert(student)
    uuc.insert(student1)
    uuc.insert(Student.Student())
    uuc.insert(Student.Student())
    print(uuc.exists(student1))
    print(uuc.exists(student))
    print(uuc.size())
    uuc.traverse(printName, uuc)
    
main()