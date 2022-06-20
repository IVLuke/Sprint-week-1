def EmpTravelClaim():
    return
def FunIntQuestion():
    for List in range(1, 101):
        if List % 5 == 0 and List % 8 == 0:
            List = "FizzBuzz"
        elif List % 5 == 0:
            List = "Fizz"
        elif List % 8 == 0:
            List = "Buzz"
        print(List)
def StringAndDate():
    return
def GraphingMonthClaim():
    return
def QuitProgram():
    print("You have quit the program!")

while True:
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1.Enter an Employee Travel Claim.   ")
    print("2.Fun Interview Question.           ")
    print("3.Cool Stuff with Strings and Dates.")
    print("4.Graph Monthly Claim Totals        ")
    print("5.Quit Program.                     ")
    print()
    while True:
        try:
            Choice = int(input("  Enter choice (1-5):  "))
        except:
            print("  Error -  enter a valid integer between 1-5")
            continue
        else:
            if Choice < 1 or Choice > 5:
                print("  Error -  enter a valid integer between 1-5")
                continue
        break

    if Choice == 1:
        EmpTravelClaim()
        print()
        AnyKey = input("Press any key to continue")
        print()
    elif Choice == 2:
        FunIntQuestion()
        print()
        AnyKey = input("Press any key to continue")
        print()
    elif Choice == 3:
        StringAndDate()
        print()
        AnyKey = input("Press any key to continue")
        print()
    elif Choice == 4:
        GraphingMonthClaim()
        print()
        AnyKey = input("Press any key to continue")
        print()
    elif Choice == 5:
        QuitProgram()
        break

