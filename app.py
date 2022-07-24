from pyfiglet import Figlet
import os

def clear():
    os.system("cls" if os.name=="nt" else "clear")
    return("   ") 

def again():
    try_again = input("Try again (y/n): ")
    while True:
        if try_again == "y" or try_again == "yes":
            print("yes choosen")
            main()
        elif try_again == "n" or try_again == "no":
            print("no choosen")
            print("Thanks")
            exit()
        else:
            print("Choose (y/n): ")
            again()



def main():
    clear()
    f = Figlet(font="big")
    print(f.renderText("YOUR PROGRAM"))
    print("Which one you will choose")
    print("1. Choice no 1")
    print("2. Choice no 2")
    print("3. Exit")
    choice = input("What do you choose (1/2/3): ")
        
    while True:
        if choice=="1":
            print("1 selected")
            again()
        elif choice=="2":
            print("2 selceted")
            again()
        elif choice=="3":
            print("3 selected")
            exit()
        else:
            print("Wrong selection, please choose (1/2/3): ")
            main()

main()
