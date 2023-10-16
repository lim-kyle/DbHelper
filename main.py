from api import *

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
def main() -> None:
    menu_option: dict = {
        1: addStudent,
        2: findStudent,
        3: deleteStudent,
        4: updateStudent,
        5: displayAllStudent,
        0: quit
    }
    option: int = -1
    while option != 0:
        system("cls")
        displaymenu()
        #student_updater()
        option = int(input("Enter Option(0..5): "))
        if option < 0 or option > 5:
            print("Invalid Input!")
        else:
            system("cls")
            menu_option.get(option)()
        input("\nPress enter key to continue...")
    
if __name__ == "__main__":
    main()