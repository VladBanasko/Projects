# application that take start time and finish time of shift from user(test version
# of app to implement it's logic on swift later)
# def counthours():

from datetime import datetime

# pay per hour
pay = 22
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
    finishtime = str(input('Enter finish time( hh:mm): '))

    try:
        start = datetime.strptime(starttime, "%H:%M")
        finish = datetime.strptime(finishtime, "%H:%M")
    # finishtime = str(input('Enter finish time( hh:mm): '))

    # finish = datetime.strptime(finishtime, "%H:%M")
    except:
        print("Error")

        # total hours worked
    timedifference = finish - start
    # total minutes worked
    timedifference1 = int(timedifference.total_seconds() / 60)

    print(timedifference)
    print(timedifference1)

    # need to create formula to correctly calculate total sum
    # total =

    print("time added and for now sum is total " + str(total))
