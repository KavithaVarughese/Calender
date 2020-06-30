# Program to display calendar of the given month and year

# importing calendar module
import calendar

#to get today's date
import datetime as date

#to get argiments
import sys

#getting the numner of dats present in a month
def monthdays(month, year):
    days = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    #taking care of leap year condition for feb
    if month not in days:
        if year%4 == 0:
            return 29
        else:
            return 28

    return days.get(month)
    

#Defining weekdays as numbers
weeks = {0:'Mo', 1:'Tu', 2:'We', 3:'Th', 4:'Fr', 5:'Sa',6:'Su',}

#DEfining months
months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

#get the required month
def getMonth(month,year):
    NumberOFDays = monthdays(month, year)

    n,m = 6,7

    ls = [[0 for i in range(m)] for j in range(n)]

    CurrentDay = 1

    #setting month layout
    DayOfMonth = date.date(year, month, CurrentDay).weekday()

    for i in range(n):
        for j in range(m):
            DayOfMonth = date.date(year, month, CurrentDay).weekday()
            if (i == 0 and j < DayOfMonth):
                continue
            ls[i][DayOfMonth] = CurrentDay
            CurrentDay = CurrentDay + 1
            if CurrentDay > NumberOFDays :
                break

        if CurrentDay > NumberOFDays:
            break

    return ls

def printMonth(month, year, arr, todayDate):
    print("\n\n    {}  {}  ".format(months.get(month), year))

    for i in range(7):
        print("{}".format(weeks[i]),end=" ")
    print(" ")

    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print("{:3}".format(" "),end='')
            else:
                if arr[i][j] == todayDate:
                    print(' ', end='')
                    print('\x1b[1;37;40m{:2d}\x1b[0m'.format(arr[i][j]), end='')
                else:
                    print('{:3d}'.format(arr[i][j]),end='')
        print(' ')

def help():
    print("This program will print the month of the calendar in calendar format according to today's date")
    print("This program also has an extra feature, it will show the future or past month based on you command line argument")
    print("Please note that you can enter any integer between -12 and +12, all other values are not accepted")
    print("The current date of the month is highlighted for every scenario")
    print("")
    return 0


#get today's date
today = date.date.today()
year = today.year
month = today.month
day = today.day

paramLen = len(sys.argv)

if paramLen == 1:
    lsFinal = getMonth(month, year)
    printMonth(month,year,lsFinal,day)
elif paramLen == 2:
    arg1 = sys.argv[1]
    input = 0

    try:
        input = int(arg1)
        if(abs(int(arg1)) <= 12):
            newMonth = month + int(arg1)
            help()
            if newMonth == 0:
                
                lsFinal = getMonth(newMonth,year)
                printMonth(newMonth,year,lsFinal,day)
            elif newMonth<0:
                year = year - 1
                newMonth = newMonth + 12

                lsFinal = getMonth(newMonth,year)
                printMonth(newMonth,year,lsFinal,day)
            else:
                if newMonth > 12:
                    year = year + 1
                    newMonth = newMonth - 12

                    lsFinal = getMonth(newMonth,year)
                    printMonth(newMonth,year,lsFinal,day)
                else:
                    lsFinal = getMonth(newMonth,year)
                    printMonth(newMonth,year,lsFinal,day)
        else:
            help()
    except ValueError:
        help()

else:
    help()