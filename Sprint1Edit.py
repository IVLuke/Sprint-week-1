# Employee work trip claims processing for NL Chocolate Company
# Authors: Nathan Greene & Luke Jones
# Date Submitted:

import math
import matplotlib.pyplot as plt
import datetime

# Functions

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
    x_axis = XList
    y_axis = YList

    plt.title("Total Sales for Each Month")
    plt.scatter(x_axis, y_axis, color='darkred', marker='x',)

    plt.plot(x_axis, y_axis)

    plt.xlabel("Time (Months)")
    plt.ylabel("Sale Totals (Dollars)")

    plt.grid(True)
    plt.show()
    
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
        print()
        NumInputs = 1
        XList = []
        YList = []
        while NumInputs <= 12:
            Month = str(NumInputs)
            Month = datetime.datetime.strptime(Month, "%m")
            FullMonth = Month.strftime("%B")
            MedMonth = Month.strftime("%b")
            try:
                MonthlyTotal = float(input(f"Enter the total monthly sales for {FullMonth}: "))
            except:
                print("Error - Must enter a number value")
                continue
            NumInputs += 1
            XList.append(MedMonth)
            YList.append(MonthlyTotal)
        GraphingMonthClaim()
        print()
        AnyKey = input("Press any key to continue")
        print()
    elif Choice == 5:
        QuitProgram()
        break
