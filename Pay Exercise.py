#Harry Vines
#06-10-2014
#Selection Development exercise 3


work_hours = int(input("Please enter the amount of hours you worked this week: "))
if work_hours >= 0 and work_hours <=60:
    hourly_pay = float(input("Please enter your hourly pay (£): "))
    pay = work_hours*hourly_pay
    extra = hourly_pay*1.5
    overall_extra = (work_hours-40)*extra
    pay_extra = (40*hourly_pay)+overall_extra
    if work_hours > 40:
        print("Your gross pay is : {0}".format(pay_extra))
    else:
        print("Your gross pay is: {0}".format(pay))
else:
    print("Invalid Work Hours")
