#retrieve 6 numbers from 1 - 60
import datetime, time

alllist = []
lucklist = []

x = 1
while x <= 60 :
    alllist.append(x)
    x += 1

print("All numbers")
print(alllist)

def sortnumber(time):             
    return time%60             

def timestamp():
    return  int(datetime.datetime.now().strftime("%f"))

x = 0
while len(lucklist) < 6:          
    time.sleep(.01)
    number = sortnumber(timestamp())
    if number not in lucklist :
        lucklist.append(number)

print("These are your 6 lucky numbers")
sorted_numbers = sorted(lucklist)
print(sorted_numbers)






