# application that take start time and finish time of shift from user(test version 
# of app to implement it's logic on swift later)
def countHours():



    pay = 22

    totalHours = 0

    startHours = int(input("input time start: "))
    print("you entered " + startHours)
    finishHours = int(input("input time finish: "))
    print("you entered " + finishHours)

    totalHours = finishHours - startHours

    total = totalHours * pay

    print("time added and for now sum is " + total)