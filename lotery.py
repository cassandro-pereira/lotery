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

def unique_list(numbers):
    return ((len(numbers)) == len(numbers))
    
x = 0
while x < 6:          
#    print(timestamp)
    time.sleep(.01)
    number = sortnumber(timestamp())
    if unique_list(lucklist):
        lucklist.append(number)         
    else:
        lucklist.pop(x)
        time.sleep(.1)
        number = sortnumber(timestamp())
        lucklist.append(number)
    x += 1

print("These are your 6 lucky numbers")
sorted_numbers = sorted(lucklist)
print(sorted_numbers)






