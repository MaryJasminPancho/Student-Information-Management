'''
Student information management
'''

import csv
from os import system
from student import Student

filename:str = 'student.csv'
slist:list = []  #local data container, not persistent


#displaymenu
def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*160)
    print("----------------------------------------".center(160))
    print("Student Information Management".center(160))
    print("----------------------------------------".center(160))
    print("1. Add student record         ".center(160))
    print("2. Find student record        ".center(160))
    print("3. Delete student record      ".center(160))
    print("4. Update student record      ".center(160))
    print("5. Display All Student records".center(160))
    print("0. Exit                       ".center(160))
    
#file management modules
def load()->None:
    global slist
    slist.clear()
    try: 
        with open(filename, newline='', mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                s = Student(row[0], row[1], row[2], row[3], row[4])
                slist.append(s)
    except FileNotFoundError:
        print("No existing student record.".center(160))

def updater()->None:
    global slist
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for s in slist:
            writer.writerow([s.getidno(), s.getlastname(), s.getfirstname(), s.getcourse(), s.getlevel()])


#utility modules
def addrecord(student:Student)->bool:
    system('cls')
    load()
    for s in slist:
        if s.getidno() == student.getidno():
            for i in range(1,5):print(" "*160)
            print("Student already exists.".center(160))
            return False
        
    slist.append(student)
    updater()
    for i in range(1,5):print(" "*160)
    print("Student added successfully.".center(160))
    return True


def findrecord(idno:str)->Student:
    system('cls')
    load()
    for s in slist:
        if s.getidno()==idno:
            return s
    return None

def deleterecord(idno:str)->bool:
    system('cls')
    load()
    for s in slist:
        if s.getidno() == idno:
            slist.remove(s)
            updater()
            for i in range(1,3):print(" "*160)
            print("Student deleted successfully.".center(160))
            return True
    print("Student not found.".center(160))
    return False
    
def updaterecord(student:Student)->bool:
    system('cls')
    load()
    for s in slist:
        if s.getidno() == student.getidno():
            s.setlastname(student.getlastname())
            s.setfirstname(student.getfirstname())
            s.setcourse(student.getcourse())
            s.setlevel(student.getlevel())
            updater()
            for i in range(1,3):print(" "*160)
            print("Student updated successfully.".center(160))
            return True
    print("Student not found.".center(160))
    return False

# display all data
def displaylist()->None:
    system('cls')
    load()
    for i in range(1,3):print(" "*160)
    if not slist:
        print("No student records found.".center(160))
        return
    print(f"{'ID No.':<10}{'Firstname':<15}{'Lastname':<15}{'Course':<10}{'Level':<6}".center(160))
    print("--------------------------------------------------------------".center(160))
    for s in slist:
        print(f"{s.getidno():<10}{s.getfirstname():<15}{s.getlastname():<15}{s.getcourse():<10}{s.getlevel():<6}".center(160))

#default entry module
def main()->None:
    option:str = ""
    while option != '0':
        displaymenu()
        for i in range(1,4):print(" "*10)
        print(" "*25, end="")
        option = input(" "*43 + "Enter option [0-5]: ").strip()
        for i in range(1,5):print(" "*25)

        match option:
            case "1": 
                system('cls')
                for i in range(1,5):print(" "*73)
                print("Add Student Record".center(160))
                print("------------------------------".center(160))
                print(" "*67, end="")
                idno = input("ID number : ").strip()
                print(" "*67, end="")
                lastname = input("Lastname  : ").strip()
                print(" "*67, end="")
                firstname = input("Firstname : ").strip()
                print(" "*67, end="")
                course = input("Course    : ").strip()
                print(" "*67, end="")
                level = input("Level     : ").strip()
                student = Student(idno, lastname, firstname, course, level)
                addrecord(student)

            case "2": 
                print(" "*25, end="")
                idno = input(" "*43 + "Enter ID number: ").strip()
                s = findrecord(idno)
                for i in range(1,2):print(" "*160)
                if s:
                    print("Student Info".center(160))
                    print("-------------------------------".center(160))
                    print(" "*67, end="")
                    print(f"ID          : \t{s.getidno()}")
                    print(" "*67, end="")
                    print(f"Lastname    : \t{s.getlastname()}")
                    print(" "*67, end="")
                    print(f"Firstname   : \t{s.getfirstname()}")
                    print(" "*67, end="")
                    print(f"Course      : \t{s.getcourse()}")
                    print(" "*67, end="")
                    print(f"Level       : \t{s.getlevel()}")
                    for i in range(1,2):print(" "*160)
                    print("\n")
                else:
                    for i in range(1,2):print(" "*160)
                    print("Student not found.".center(160))
                
            case "3": 
                print(" "*25, end="")
                idno = input(" "*43 + "Enter ID number: ").strip()
                deleterecord(idno)

            case "4": 
                print(" "*25, end="")
                idno = input(" "*43 + "Enter ID number: ").strip()
                s = findrecord(idno)
                for i in range(1,2):print(" "*160)
                if s:
                    print("Update Student Information".center(160))
                    print("---------------------------------".center(160))
                    print("Leave blank if no changes\n".center(160))
                    print("\n")
                    print(" "*67, end="")
                    lastname = input(f"Enter last name ({s.getlastname()}): ").strip()
                    print(" "*67, end="")
                    firstname = input(f"Enter first name ({s.getfirstname()}): ").strip()
                    print(" "*67, end="")
                    course = input(f"Enter course ({s.getcourse()}): ").strip()
                    print(" "*67, end="")
                    level = input(f"Enter level ({s.getlevel()}): ").strip()

                    if not lastname: lastname = s.getlastname()
                    if not firstname: firstname = s.getfirstname()
                    if not course: course = s.getcourse()
                    if not level: level = s.getlevel()

                    student = Student(idno, lastname, firstname, course, level)
                    updaterecord(student)
                    
                else:
                    for i in range(1,2):print(" "*160)
                    print("Student not found.".center(160))

            case "5": 
                displaylist()
                for i in range(1,2):print(" "*160)
                print("\n")

            case "0": print("Program terminated.".center(160))

            case _:print("Invalid option.".center(160))
        
        input("Press any key to continue...".center(160))
            


#application launcher
if __name__=="__main__":
    main()