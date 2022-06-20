
# Constant
DAILY_RATE = 85.00
MILE_RATE = 0.17
# Input Values
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
        kmTrav = str(kmTrav)
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
        ClaimType = Claimtype.upper()
        if ClaimType == "S" or ClaimType == "E":
            ClaimType = ClaimType
        else:
            continue
    break


# Calculations
PerDiemAmt = Days * DAILY_RATE

'''
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
'''

