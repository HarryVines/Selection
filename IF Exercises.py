#Harry Vines
#selection improvement exercise
#29-09-14

months=False
while months==False:
            month = int(input("Please enter a month as a number between 1-12: "))
            year = int(input("please enter the year: "))
            if month == 1:
                print("The month you entered is January")
                months=True
            if month == 2:
                months=True
                print("The month you entered is February")
            if month == 3:
                months=True
                print("The month you entered is March")
            if month == 4:
                months=True
                print("The month you entered is April")
            if month == 5:
                months=True
                print("The month you entered is May")
            if month == 6:
                months=True
                print("The month you entered is June")
            if month == 7:
                months=True
                print("The month you entered is July")
            if month == 8:
                months=True
                print("The month you entered is August")
            if month == 9:
                months=True
                print("The month you entered is September")
            if month == 10:
                months=True
                print("The month you entered is October")
            if month == 11:
                months=True
                print("The month you entered is November")
            if month == 12:
                months=True
                print("The month you entered is December")
            if month > 12:
                print("invalid month")
            if month < 1:
                print("invalid month")

            if year/4 and year%4==0:
                print("The year is a leap year")
            else:
                print("The Year is not a leap year")

