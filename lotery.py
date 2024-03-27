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
    
x = 0
while x <= 6:
    timestamp = int(datetime.datetime.now().strftime("%f"))        
#    print(timestamp)
    time.sleep(.1)
    number = sortnumber(timestamp)
    lucklist.append(number)
    x += 1
print("These are your 6 lucky numbers")
print(lucklist)





