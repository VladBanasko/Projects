# application that take start time and finish time of shift from user(test version
# of app to implement it's logic on swift later)
# def counthours():

from datetime import datetime

# pay per hour
pay = 23
# pay per minute
pay2 = pay / 60

pay3 = float(round(pay2, 2))

print(pay3)

totalminutes = 0

# startHours = int(input("input time start: "))
# print("you entered " + str(startHours))
# finishHours = int(input("input time finish: "))
# print("you entered " + str(finishHours))
# starttime = str(input('Enter start time(yyyy-mm-dd hh:mm): '))

# start = datetime.strptime(starttime, "%Y-%m-%d %H:%M")

# finishtime = str(input('Enter finish time(yyyy-mm-dd hh:mm): '))

# finish = datetime.strptime(finishtime, "%Y-%m-%d %H:%M")

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
    # finishtime = str(input('Enter finish time( hh:mm): '))

    # finish = datetime.strptime(finishtime, "%H:%M")
    except:
        print("Error")

        # total hours worked
    timedifference = finish - starts
    # total minutes worked
    timedifference1 = int(timedifference.total_seconds() / 60)

    print(timedifference)
    print(timedifference1)

    # need to create formula to correctly calculate total sum
    # total = 22 * hours ( devide total time by 60 , then multiply whole number of hours by 22
    # rest of time , minutes left from working time multiply by payment per minute

    wotkinghours = int(timedifference  / 60) asdf# whole number of hours
    print(wotkinghours)
    minutesworkedleft =   timedifference % 60 # minutes left from working hours
    print(minutesworkedleft)


    print("time added and for now sum is total " + str(total))
