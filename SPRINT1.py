# Employee work trip claims processing for NL Chocolate Company
# Authors: Nathan Greene & Luke Jones
# Date Completed: June 21st, 2022

# Imports
import math
import matplotlib.pyplot as plt
import datetime
import random

# Constants
DAILY_RATE = 85.00
MILE_RATE = 0.17
HST_RATE = 0.15


# Functions

def Calc(Value1, Value2):
    # function to subtract Value2 from Value1
    c = Value2 - Value1  # Value1 and Value2 are variables that will be called from the program
    return c  # c is then returned to the program as the result of the equation


def FComma2(DollarValue):
    # Function to format a number into a dollar value (string)
    DollarValueStr = "${:,.2f}".format(DollarValue)  # takes the variable and formats into a dollar

    return DollarValueStr  # Returns the variable (Now formatted to dollars) into the program

def AnyKey():
    # function that calls for an input to end the program
    print()
    Ending = input("Enter any key to continue")
    print()
    return Ending               # Returns the input to continue the program


def EmpTravelClaim():
    # Employee Travel Claim
    # Date Completed: June 18, 2022

    ENDSTATE = "CONTINUE"
    Bonus = 0
    CB1 = "2022-12-15"
    CB1 = datetime.datetime.strptime(CB1, "%Y-%m-%d")
    CB2 = "2022-12-22"
    CB2 = datetime.datetime.strptime(CB2, "%Y-%m-%d")

    # Input values
    while ENDSTATE == "CONTINUE":
        while True:
            try:
                EmpNum = input("Enter your employee # (Must be 5 digits): ")
            except:
                print("Error - employee # must be 5 digits!")
                continue
            else:
                if len(EmpNum) > 5 or len(EmpNum) < 5:
                    print("Error - employee # must be 5 digits!")
                    continue
            break
        EmpFName = input("Enter your first name: ")
        EmpFName = EmpFName.title()
        EmpLName = input("Enter your last name: ")
        EmpLName = EmpLName.title()
        Location = input("Enter the location of the trip: ")
        while True:
            try:
                StartDate = input("Enter a valid start date (YYYY-MM-DD): ")
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            except:
                print("Error - date must be in format (YYYY-MM-DD)")
                continue

            try:
                EndDate = input("Enter a valid end date (No more then 7 days of start date and in format YYYY-MM-DD): ")
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                Days = Calc(StartDate, EndDate)
                Days = Calc(StartDate, EndDate).days
            except:
                print("Error - end date must not exceed 7 days!")
                continue
            else:
                EndDate7 = StartDate + datetime.timedelta(days=7)

                if StartDate > EndDate:
                    print("Error - end date Must be greater than start date")
                    continue
                elif EndDate > EndDate7:
                    print("Error - End date must not exceed 7 days!")
                    continue
            break

        while True:
            try:
                CarOption = input("Enter if used own or rented vehicle (O or R): ")
            except:
                print("Error - Must be O or R!")
                continue
            else:
                CarOption = CarOption.upper()
                if CarOption == "O" or CarOption == "R":
                    CarOption = CarOption
            break

        while CarOption == "O":
            try:
                kmTrav = input("Enter the kilometers traveled (Don't exceed 2000km): ")
            except:
                print("Error - Must mot exceed 2000km!")
                continue
            else:
                kmTrav = int(kmTrav)
                if kmTrav > 2000:
                    print("Error - Must not exceed 2000km!")
                    continue
            break

        while True:
            try:
                ClaimType = input("Enter claim type standard or executive (Use S or E): ")
            except:
                print("Error - Must be S or E!")
                continue
            else:
                ClaimType = ClaimType.upper()
                if ClaimType == "S" or ClaimType == "E":
                    ClaimType = ClaimType
            break

        # Per diem calculations
        PerDiemAmt = Days * DAILY_RATE
        if CarOption == "O":
            MileAmt = MILE_RATE * kmTrav
        else:
            MileAmt = 65.00 * Days

        if Days > 3:
            Bonus += 100
        else:
            Bonus = Bonus

        if kmTrav > 1000 and CarOption == "O":
            Bonus = Bonus + (kmTrav * 0.04)
        else:
            Bonus = Bonus

        if ClaimType == "E":
            Bonus = Bonus + (45.00 * Days)
        else:
            Bonus = Bonus

        if CB1 <= StartDate <= CB2:
            Bonus = Bonus + (50.00 * Days)
        else:
            Bonus = Bonus

        ClaimAmt = PerDiemAmt + MileAmt + Bonus
        Hst = PerDiemAmt * HST_RATE
        ClaimTotal = Hst + ClaimAmt
        StartDate = StartDate.strftime("%Y-%m-%d")
        EndDate = EndDate.strftime("%Y-%m-%d")

        # Printing final outputs
        print()
        print("        Employee Travel Claim         ")
        print("---------------------------------------")
        print()
        print(f"Employee #:      {EmpNum}             ")
        print(f"Employee's name: {EmpFName} {EmpLName}")
        print()
        print(f"Location of travel:  {Location}       ")
        print(f"Start date:          {StartDate}      ")
        print(f"End date:            {EndDate}        ")
        print(f"Number of days:      {Days}           ")
        print()
        print(f"Car Option:          {CarOption}      ")
        print(f"KM travelled:        {kmTrav}         ")
        print()
        print(f"Claim type:          {ClaimType}      ")
        print(f"Per Diem Amount:     {PerDiemAmt}     ")
        print(f"Mileage Amount       {MileAmt}        ")
        print("---------------------------------------")
        print(f"Bonus                {FComma2(Bonus)}")
        print(f"Claim Amount:        {FComma2(ClaimAmt)}")
        print(f"HST:                 {FComma2(Hst)}")
        print(f"Claim Total:         {FComma2(ClaimTotal)}")
        print("---------------------------------------")

        ENDSTATE = input("Would you like to do another sale?(END or CONTINUE): ")
        ENDSTATE = ENDSTATE.upper()


def FunIntQuestion():
    # A Loop that makes every 5th iteration say fizz 8th iteration say buzz and fizzbuzz if both
    for List in range(1, 101):
        if List % 5 == 0 and List % 8 == 0:
            List = "FizzBuzz"
        elif List % 5 == 0:
            List = "Fizz"
        elif List % 8 == 0:
            List = "Buzz"

        # Print statement
        print(List)


def StringAndDate():
    # Random Password Generator
    # Date Completed: June 18, 2022

    # Starting values
    while True:
        EmpFName = "Joe"
        EmpLName = "HassleBerry"
        PhoNum = "7096902791"
        CurDate = datetime.datetime.now()
        CurDate = datetime.datetime.strftime(CurDate, "%Y-%m-%d")
        StartDate = "2022-01-06"

        # RANDOM PASSWORD GEN
        Characters = list(EmpLName + EmpFName + PhoNum + StartDate)

        # Length of password
        length = int(input("Enter password length: "))

        # Shuffling the characters
        random.shuffle(Characters)

        # Picking random characters
        password = []
        for i in range(length):
            password.append(random.choice(Characters))

        # Shuffling
        random.shuffle(password)
        password = "".join(password)
        break

    # printing the list
    print()
    print("--------------------------------------")
    print(f"Random Password Generated: {password}")
    print(f"Date/Time Created:         {CurDate} ")
    print("--------------------------------------")


def GraphingMonthClaim():
    # Graphs out the monthly claims by the input value

    # Variables
    NumInputs = 1
    XList = []
    YList = []

    # Main loop (Including inputs)
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

    # Graphing inputs
    x_axis = XList
    y_axis = YList

    plt.title("Total Sales for Each Month")
    plt.scatter(x_axis, y_axis, color='darkred', marker='x', )

    plt.plot(x_axis, y_axis)

    plt.xlabel("Time (Months)")
    plt.ylabel("Sale Totals (Dollars)")

    plt.grid(True)
    plt.show()


def QuitProgram():
    # prints the quit message for the program
    print("You have quit the program!")


# Loop for the menu
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

    # Input + Verification for the main loop
    while True:
        try:
            Choice = int(input("  Enter choice (1-5):  "))
            print()
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
        AnyKey()
    elif Choice == 2:
        FunIntQuestion()
        AnyKey()
    elif Choice == 3:
        StringAndDate()
        AnyKey()
    elif Choice == 4:
        GraphingMonthClaim()
        AnyKey()
    elif Choice == 5:
        QuitProgram()
        break

