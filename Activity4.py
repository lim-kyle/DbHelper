"""
    <name: Alcarmen, Brandon V.>
    <schedule: MW 9:00-10:30 AM>
    <edpcode: 13953>
	create a file 'student.txt', read, write and update this file
	for the student list
	Create the student list with a menu provided below
	----------- Student List -----------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ------------------------------------
    Enter Option(0..5):
    sample student entry below
    
    student:dict = {
        'idno':'0001',
        'lastname':'alpha',
        'firstname':'bravo',
        'course':'bsit',
        'level':'3',
    }
"""
from os import system
from dbhelper import * #Connector sa dbhelper na database;
def idchecker(ID):
    return ID.isdigit()
    
def Add()->None:
    system("cls")
    print("---------------")
    print(">>ADD student Page<<")
    print("---------------\n")
    
    Check = False
    while True:
        ID = input(">> Enter ID: ")
        if idchecker(ID):
            students = "student.txt"
            

            with open(students, "r") as find:
                for line in find:
                    if str(ID) in line:
                        print()
                        print(">> ID already exist! <<\n")
                        print(">> Returning to Main Menu. <<\n")
                        
                        found = True
                        
                        return ID
                  
            if not Check:   
                stud = open("student.txt","a")
                FName = input (">> Enter First Name: ")
                LName = input (">> Enter Last Name: ")
                Course= input (">> Enter Course/Program: ")
                Level= input (">> Enter Level: ")
                                
                student:dict={
                    'idno: ':ID,
                    'First name: ':FName,
                    'Last name: ':LName,
                    'Course: ':Course,
                    'Level: ':Level
                }
                stud.write(f"{student.get('idno: ')} ,{student.get('First name: ')}, {student.get('Last name: ')}, {student.get('Course: ')}, {student.get('Level: ')}\n")
                break
        else:
            print("\n>> Please input numbers in ID. <<\n")
   
    

def Find()->None:
    system("cls")
	#Change OIL Dri
    print("---------------")
    print(">>Find/Search Page<<")
    print("---------------\n")
    
    found = False
    search = input(">> Enter Search: ")
    
    students = "student.txt"
    with open(students, "r") as find:
        for line in find:
            if search in line:
                print(">> Student Found:",line)
                
                found = True
    if not found:
        print(">> Name doesn't exist. <<")
    
    

def Delete()->None:
    system("cls")
	#Change OIL Dri
    print("---------------")
    print(">>Delete Student Page<<")
    print("---------------\n")
    found = False
    remain = []  
    students = "student.txt"  

    delet = input(">> Enter the student name to delete: ")
    remain = []
    if delet != "":  
        print()
        agree = input(">> Are you really really sure?(Y for yes/ N for no): ")
        if agree == "Y" or agree == 'y':
            with open(students, "r") as find:
                for line in find:
                    if delet in line:
                        print()
                        print(f">> Student Found: {line}")
                        found = True
                    else:
                        remain.append(line)
                if not found:
                    print(">> Student doesn't exist.")
                else:
                    with open(students, "w") as find:
                        find.writelines(remain)
                    print(f">> Student '{delet}' has been deleted.")
                    print()
        else:
            print()
            print(">> Delete Cancel. <<")
            print(">> Returning to Main Menu. <<\n")
    else:
        print()
        print(">> Error <<")
     
def Update()->None:
    system("cls")
	#Change OIl Diri
    print("---------------")
    print(">>Update Page<<")
    print("---------------\n")
    students = "student.txt"
    try:
        ID = input("Enter Student >>IDnumber<<:")
        if idchecker(ID):
            FName = input (">> Enter First Name: ")
            LName = input (">> Enter Last Name: ")
            Course= input (">> Enter Course/Program: ")
            Level= input (">> Enter Level: ") 
            
            with open(students) as check:
                lines=check.readlines()
            if (int(ID)<= len(lines)):
                lines[int(ID)-1] = f"{ID},{FName},{LName},{Course},{Level}\n"
                with open(students,"w") as check:
                    print()
                    check.writelines(lines)
            else:
                print("ID", ID, "Exceed.")
        else:
            print("\n>> Please input numbers in ID. <<\n")
            print(">> Returning to Main Menu. <<\n")
    except ValueError:
        print("\n>> Please input Student's ID number <<\n")
    
    

def add():
	#Add using the dphelper connector
	idno = input("Enter id: ")
	firstname = input("Enter firtname: ")
	lastname = input("Enter lastname: ")
	course = input("Enter course: ")
	level = input("Enter level: ")
	print(addrecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level))
	
def DisplayAll()->None:
	system("cls")
	print("------------------------")
	print(">>Display student Page<<")
	print("------------------------\n")
	sd = getall("student")
	for i in sd:
		print(i)

    
    
def Quit()->None:
    system("cls")
    print("Program Ended...")
	


def displaymenu()->None:
	system("cls")
	MenuOption:tuple=(
	"------- Main Menu -------",
	"1. Add Student",
	"2. Find Student",
	"3. Delete Student",
	"4. Update Student",
	"5. Display All Student",
	"0. Quit/Exit",
	"-------------------------"
	)
	[print(menu) for menu in MenuOption]	
def main()->None:
	
	option:int = -1
	menuitems = {
		1:add,
		2:Find,
		3:Delete,
		4:Update,
		5:DisplayAll,
		0:Quit
	}
	while option != 0:
		displaymenu()
		option=int(input("Enter option (0-5): "))
		menuitems.get(option)()
		input("Press any key to continue...")


if __name__=="__main__":
	main()