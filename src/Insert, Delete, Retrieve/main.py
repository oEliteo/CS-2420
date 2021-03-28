import Student
import timeit

def main():
    file0 = open("InsertNames.txt", "r")
    file1 = open("DeleteNames.txt", "r")
    file2 = open("RetrieveNames.txt", "r")
    studentList = []
    start = timeit.default_timer()
    
    for line in file0:
        
        line = line.split(' ')
        student = Student.Student()
        student.setMembers(line[0],line[1],line[2],line[3],line[4].strip())
    
        appendStudent(studentList, student)
        
    end = timeit.default_timer()
    print("The Insertion time elapsed was: " + str(round((end - start), 3)) + " Seconds!\n")
    start = timeit.default_timer()
    print("The Average Age after insertion is:", str(averageAge(studentList)))
    end = timeit.default_timer()
    print("The time elapsed for averaging the ages of the students was:",str(round((end - start), 3)),"Seconds!\n")
    print("The number of students in the list of students before deletion is: " + str(len(studentList)) + "\n")
    
    start = timeit.default_timer()
    for line in file1:
        deleteStudent(studentList, line.strip('\n'))
    end = timeit.default_timer()
    print("The number of students in the list of students after deletion is: " + str(len(studentList)) + "\n")
    print("The time elapsed for deleting the students listed in DeleteStudents.txt was:",str(round((end - start),3)),"Seconds!\n")
    
    start = timeit.default_timer()
    
    age = 0
    total = 0
    amountToSubtract = 0
    count = 0
    for line in file2:
        age = retrieveAverageAge(studentList, line.strip('\n'))
        if age == 0:
            amountToSubtract += 1
        total += int(age)
        count += 1
    
    end = timeit.default_timer()
    print("The average age of the students marked for retrieval is:", str(total / (count - amountToSubtract)))
    print("The time elapsed for the students marked for retrieval was:", str(round((end - start), 3)), "Seconds!\n")
        
    end = timeit.default_timer()
    print("The time elapsed for retrieving the students was: " + str(round((end - start), 3)) + " Seconds!\n")
        
    file0.close()
    file1.close()
    file2.close()
    
def appendStudent(xList, student):
    if not xList:
        xList.append(student)
    else:
        if (checkDuplicate(xList, student)):
            print(student.getFirstName() + " " + student.getLastName() + " Is already in the list of students, and has not been added a second time!")
        else:
            xList.append(student)
            
def checkDuplicate(xList, student):
    flag = False
    for i in range(len(xList)):
        if (xList[i].getSSN() == student.getSSN()):
            flag = True
            break
        else:
            flag = False
    return flag

def averageAge(xList):
    total = 0
    for i in xList:
        total += int(i.getAge())
    return total / len(xList)

def retrieveAverageAge(xList, SSN):
    age = 0
    for i in xList:
        if (i.getSSN() == SSN):
            age = i.getAge()
            break
        
    if (age == 0):
        print("This SSN was marked for retrieval, but was not found in the list:",str(SSN))
    return age        

def deleteStudent(xList, SSN):
    initialLength = len(xList)
    for i in range(len(xList)):
        if (xList[i].getSSN() == SSN):
            xList.pop(i)
            break
    if (initialLength == len(xList)):
        print("This SSN was marked for deletion, but was not found in the list:",str(SSN))

main()