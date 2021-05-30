
# application that take start time and finish time of shift from user(test version
# of app to implement it's logic on swift later)
# def counthours():

from datetime import datetime



# pay per hour
pay = 22
# pay per minute
pay2 = pay / 60

pay3 = float(round(pay2,2))

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

starttime = ''

while starttime != 'end':
    #try:
    

    starttime = str(input('Enter start time( hh:mm): , or type end to end program :'))

    start = datetime.strptime(starttime, "%H:%M")

    finishtime = str(input('Enter finish time( hh:mm): '))

    finish = datetime.strptime(finishtime, "%H:%M")


        # total hours worked
    timedifference = finish - start
    # total minutes worked
    timedifference1 = int(timedifference.total_seconds() / 60)

    print(timedifference)
    print(timedifference1)

        # totalhours = finishHours - startHours

        # total = totalhours * pay

        # total sum of payed minutes
    total = timedifference1 * pay3

    print("time added and for now sum is total " + str(total))
    #except:
    print("Sorry, invalid input")

