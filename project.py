import sys
def menu():
    print("\n Console-Based Calculator in Python \n")
    print("1. Add two numbers")
    print("2. Substract two numbers")
    print("3. Multiply two numbers")
    print("4. divide two numbers")
    print("5. Exit")

    choice = input("Select an option (1/2/3/4/5) : ")

    if choice == "1":
        add()
    elif choice =="2":
        sub()
    elif choice =="3":
        mul()
    elif choice=="4":
        div()
    elif choice=="5":
        sys.exit("Thank You!")
    else:
        sys.exit("Invalid Option")

def add():
    num1=float(input("Enter the first Number : "))
    num2=float(input("Enter the second number : "))
    print(f"{num1} + {num2} = {num1+num2}")
    menu()

def sub():
    num1=float(input("Enter the first Number : "))
    num2=float(input("Enter the second number : "))
    print(f"{num1} - {num2} = {num1-num2}")
    menu()

def mul():
    num1=float(input("Enter the first Number : "))
    num2=float(input("Enter the second number : "))
    print(f"{num1} * {num2} = {num1*num2}")
    menu()

def div():
    num1=float(input("Enter the first Number : "))
    num2=float(input("Enter the second number : "))
    if num2==0:
        print("Divide by zero Error!")
    else:
        print(f"{num1} / {num2} = {num1/num2}")
    menu()





if __name__ == "__main__":
    menu()