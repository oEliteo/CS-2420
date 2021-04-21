import Student
import SSN
import timeit
from UUCHash import *


def main():
#___________________________________________________________________________________________
    #insertion
    seperator = "_________________________________________________________________________"
    print(seperator,'\n' + "Insertion:")
    file0 = open("InsertNamesMedium.txt", "r")
    file1 = open("DeleteNamesMedium.txt", "r")
    file2 = open("RetrieveNamesMedium.txt", "r")
    studentList = UUC(300000)
    start = timeit.default_timer()
    duplicates = 0
    for line in file0:
        line = line.split(' ')
        student = Student.Student()
        student.setMembers(line[0],line[1],line[2],line[3],line[4].strip())
        
        if(not studentList.insert(student)):
            duplicates += 1
    
    end = timeit.default_timer()
    t1 = end-start
    print("There were:", str(duplicates), "duplicates in the list of names marked for insertion!")
    print("Items:",studentList.size())
    print("Insertion time: " + str(t1) + "s" + "\n" + seperator) 
#___________________________________________________________________________________________
    #Average-Initially
    print(seperator,'\n' + "Initial Average Age:")
    start = timeit.default_timer()
    totalAge = [0]
    studentList.traverse(average, totalAge)
    print("Average Age:",str(totalAge[0] / studentList.size()))
    end = timeit.default_timer()
    t2 = end - start
    print("Time Elapsed:",str(t2) + 's')
    print(seperator)
#___________________________________________________________________________________________
    #Deletion
    print(seperator,'\n'+"Deletion:")
    start = timeit.default_timer()
    print("Items before:", studentList.size())
    delete_failures = 0
    for line in file1:
        ssn = SSN.SSN(line.strip('\n'))
        if(not studentList.delete(ssn)):
            delete_failures += 1
#             print("SSN not found:", ssn.getSSN())
    end = timeit.default_timer()
    t3 = end - start
    print("There were:", str(delete_failures), "items not found in the list of names marked for deletion!")
    print("Items after:",studentList.size())
    print("Deletion time:", str(t3) + 's' + '\n' + seperator)
#___________________________________________________________________________________________
    #Retrieve
    print(seperator,'\n'+"Retreive:")
    start = timeit.default_timer()
    totalAge = [0]
    count = 0
    retrieve_failures = 0
    for line in file2:
        ssn = SSN.SSN(line.strip('\n'))
        if(studentList.exists(ssn)):
            count += 1
            found_student = studentList.retrieve(ssn)
            totalAge[0] += int(found_student.getAge())
        else:
            retrieve_failures += 1
#             print("SSN not found:", ssn.getSSN())
    end = timeit.default_timer()
    t4 = end - start
    print("There were:", str(retrieve_failures), "items not found in the list of names marked for retrieval!")
    print("Average Age:",str(totalAge[0] / count))
    print("Retrieval time:",str(t4) + 's' + '\n' + seperator)
    total_time = t1 + t2 + t3 + t4
    print('\n' + "Total Time Elapsed:",str(total_time) + 's')
    
def average(student, data):
    data[0] += int(student.getAge())
    
main()