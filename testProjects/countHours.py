# application that take start time and finish time of shift from user(test version
# of app to implement it's logic on swift later)
#def counthours():

from datetime import datetime
#pay per hour
pay = 22
#pay per minute
pay2 = pay /60

totalhours = 0

#startHours = int(input("input time start: "))
#print("you entered " + str(startHours))
#finishHours = int(input("input time finish: "))
#print("you entered " + str(finishHours))


#starttime = str(input('Enter start time(yyyy-mm-dd hh:mm): '))

#start = datetime.strptime(starttime, "%Y-%m-%d %H:%M")

#finishtime = str(input('Enter finish time(yyyy-mm-dd hh:mm): '))

#finish = datetime.strptime(finishtime, "%Y-%m-%d %H:%M")

starttime = str(input('Enter start time( hh:mm): '))

start = datetime.strptime(starttime, "%H:%M")

finishtime = str(input('Enter finish time( hh:mm): '))

finish = datetime.strptime(finishtime, "%H:%M")

timedifference = finish - start

print(timedifference)

#totalhours = finishHours - startHours

#total = totalhours * pay
total = timedifference * pay

print(total)

print("time added and for now sum is " + str(total))

