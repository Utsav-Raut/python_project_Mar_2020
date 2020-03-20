import sys
def enter_name():
    name = input("Please enter a name: ")
    print(name)

def choose_relation():
    print("Choose a relation from the following: ")
    print("1. SON")
    print("2. DAUGHTER")
    print("3. HUSBAND")
    print("4. WIFE")
    print("5. BROTHER")
    print("6. SISTER")
    relation = input()
    if relation == "1":
        print("Son")
    elif relation == "2":
        print("Daughter")
    elif relation == "3":
        print("Husband")
    elif relation == "4":
        print("Wife")
    elif relation == "5":
        print("Bro")
    elif relation == "6":
        print("Sister")

def choose_band():
    print("Is the person member of any band?")
    band_option = input("Yes/No? ")
    if band_option.upper() == "NO":
        print("OK")
    elif band_option.upper() == "YES":
        print("Band Member")
        band_name = input("Enter the band name : ")
        print(band_name)
    else:
        print("Invalid choice.")

def main():
    head = "Silpa"
    flag = True
    while flag == True:
        print("If you wish to enter new details, press 1")
        print("If u wish to edit existing members, press 2")
        print("If you wish to quit, press 3")
        continue_entering = input()
        if continue_entering == "1":
            enter_name()
            choose_relation()
            choose_band()
        elif continue_entering == "2":
            print("This feature is being built, please try after a few days")
            sys.exit()
        elif continue_entering == "3":
            flag = False
        
    print("Thank You for using our application")

main()
