# application that take start time and finish time of shift from user(test version
# of app to implement it's logic on swift later)
# def counthours():

# count number of minutes to multiply later by pay
from datetime import datetime

# pay per hour
pay = 23
# pay per minute
pay2 = pay / 60 

pay3 = float(round(pay2, 2)) 

print(" pay per min is {}".format(pay2))
print(" pay per min rounded is {}".format(pay3))

totalminutes = 0


work = True

while work:

    starttime = str(input('Enter start time( hh:mm): , or type end to end program :'))
    if starttime == 'end':
        work = False
        break
    finishtime = str(input('Enter finish time( hh:mm): '))

    try:
        start = datetime.strptime(starttime, "%H:%M")
        finish = datetime.strptime(finishtime, "%H:%M")

    # except:
    #     print("Error")

        # total time worked
        timedifference = finish - start
    except:
        print("Error")
        

    # total minutes worked
    timedifference1 = int(timedifference.total_seconds() / 60)

    print("timedifference in hours {} ".format(timedifference))
    print("timediffernece in minutes is {}".format(timedifference1))

    totalPayHours = pay * timedifference
    totalPayMinutes = float(round(pay2 * timedifference1, 2))

    # print(" payment for total  hours is {}".format(totalPayHours))
    print(" payment for total minutes is {}".format(totalPayMinutes))

