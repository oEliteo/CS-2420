import Student
import SSN
import timeit
from UUC import *


def main():
#___________________________________________________________________________________________
    #insertion
    seperator = "_________________________________________________________________________"
    print(seperator,'\n' + "Insertion:")
    file0 = open("InsertNames.txt", "r")
    file1 = open("DeleteNames.txt", "r")
    file2 = open("RetrieveNames.txt", "r")
    studentList = UUC()
    start = timeit.default_timer()
    
    for line in file0:
        line = line.split(' ')
        student = Student.Student()
        student.setMembers(line[0],line[1],line[2],line[3],line[4].strip())
        
        if(not studentList.insert(student)):
            print("Duplicate detected:", student.getFirstName(), student.getLastName())
                
    end = timeit.default_timer()
    print("Items:",studentList.size())
    print("Insertion time: " + str(end-start) + "s" + "\n" + seperator) 
#___________________________________________________________________________________________
    #Average-Initially
    print(seperator,'\n' + "Initial Average Age:")
    start = timeit.default_timer()
    totalAge = [0]
    studentList.traverse(average, totalAge)
    print("Average Age:",str(totalAge[0] / studentList.size()))
    end = timeit.default_timer()
    print("Time Elapsed:",str(end - start) + 's')
    print("\n" + seperator)
#___________________________________________________________________________________________
    print(seperator,'\n'+"Deletion:")
    start = timeit.default_timer()
    print("Items before:", studentList.size())
    for line in file1:
        ssn = SSN.SSN(line.strip('\n'))
        if(not studentList.delete(ssn)):
            print("SSN not found:", ssn.getSSN())
    end = timeit.default_timer()
    print("Items after:",studentList.size())
    print("Deletion time:", str(end-start) + 's' + '\n' + seperator)
#___________________________________________________________________________________________
    #Average-Range
    print(seperator,'\n'+"Retreive:")
    start = timeit.default_timer()
    totalAge = [0]
    count = 0
    for line in file2:
        ssn = SSN.SSN(line.strip('\n'))
        if(studentList.exists(ssn)):
            count += 1
            found_student = studentList.retrieve(ssn)
            totalAge[0] += int(found_student.getAge())
        else:
            print("SSN not found:", ssn.getSSN())
    end = timeit.default_timer()
    print("Average Age:",str(totalAge[0] / count))
    print("Retrieval time:",str(end-start) + 's' + '\n' + seperator)
    
    
def average(student, data):
    data[0] += int(student.getAge())
    
main()