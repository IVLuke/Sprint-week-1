def EmpTravelClaim()
def FunIntQuestion()
def StringAndDate()
def GraphingMonthClaim()
def QuitProgram()
    print("You have quit the program!")


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

    if choice == 1:
        EmpTravelClaim()
    elif choice == 2:
        FunIntQuestion()
    elif choice == 3:
        StringAndDate()
    elif choice == 4:
        GraphingMonthClaim()
    elif choice == 5:
        QuitProgram()
    else:
        break


