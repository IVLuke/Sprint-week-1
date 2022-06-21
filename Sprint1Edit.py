def EmpTravelClaim():
# Employee Travell Claim
# Date Completed: June 18, 22

ENDSTATE = "CONTINUE"
# Constant
DAILY_RATE = 85.00
MILE_RATE = 0.17
HST_RATE = 0.15
# Input values
while ENDSTATE == "CONTINUE":
    while True:
        try:
            EmpNum = input("Enter your employee #(Must be 5 digits): ")
        except:
            print("Error - employee # must be 5 digits!")
            continue
        else:
            if len(EmpNum) > 5 or len(EmpNum) < 5:
                print("Error - employee # must be 5 digits!")
                continue
            else:
                break
        break
    EmpFName = input("Enter your first name: ")
    EmpFName = EmpFName.title()
    EmpLName = input("enter your last name: ")
    EmpLName = EmpLName.title()
    Location = input("Enter the location of the trip: ")
    StartDate =  input("Enter a valid start date(Format YYYY-MM-DD): ")
    while True:
        try:
            EndDate = input("Enter a valid end date(No more then 7 days of start date and in format YYYY-MM-DD): ")
        except:
            print("Error - end date must not exceed 7 days!")
            continue
        else:
            ED = float(EndDate[8:10])
            SD = float(StartDate[8:10])
            Days = ED - SD
            if Days > 7:
                print("Error - end date must not exceed 7 days!")
                continue
            else:
                break
        break
    while True:
        try:
            CarOption = input("Enter if used own or rented vehicle(Use O or R): ")
        except:
            print("Error - Must be O or R!")
            continue
        else:
            CarOption = CarOption.upper()
            if CarOption == "O" or CarOption == "R":
                CarOption = CarOption
            else:
                continue
        break
    while CarOption == "O":
        try:
            kmTrav = input("Enter the kilometers traveled(Don't exceed 2000km): ")
        except:
            print("Error - Must mot exceed 2000km!")
            continue
        else:
            kmTrav = int(kmTrav)
            if kmTrav > 2000:
                print("Error - Must not exceed 2000km!")
                continue
            else:
                break
        break
    while True:
        try:
            ClaimType = input("Enter claim type standard or executive(Use S or E): ")
        except:
            print("Error - Must be S or E!")
            continue
        else:
            ClaimType = ClaimType.upper()
            if ClaimType == "S" or ClaimType == "E":
                ClaimType = ClaimType
            else:
                continue
        break


    # Per diem calculations
    PerDiemAmt = Days * DAILY_RATE
    if CarOption == "O":
        MileAmt = MILE_RATE * kmTrav
    else:
        MileAmt = 65.00 * Days

    Bonus = 0
    if Days > 3:
        Bonus = Bonus + 100
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

    SD2 = str(StartDate[5:10])
    if SD2 >= "12-15" and SD2 <= "12-22":
        Bonus = Bonus + (50.00 * Days)
    else:
        Bonus = Bonus

    ClaimAmt = PerDiemAmt + MileAmt + Bonus
    Hst = PerDiemAmt * HST_RATE
    ClaimTotal = Hst + ClaimAmt

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
    print(f"Bonus                 ${Bonus:,.2f}")
    print(f"Claim Amount:         ${ClaimAmt:,.2f}")
    print(f"HST:                  ${Hst:.2f}")
    print(f"Claim Total:          ${ClaimTotal:,2f}")
    print("---------------------------------------")

    ENDSTATE = input("Would you like to do another sale?(END or CONTINUE): ")
    ENDSTATE = ENDSTATE.upper()
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
    return




def StringAndDate():
# Random Password Gen
# Date Completed: June 18, 22

# Import values
import datetime
import random

#Starting values
while True:
    EmpFName = "Joe"
    EmpLName = "HassleBerry"
    PhoNum = "7096902791"
    CurDate = datetime.datetime.now()
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

