import datetime, time

alllist = []
lucklist = []

x = 1
while x <= 60 :
    alllist.append(x)
    x += 1

print("All numbers")
print(alllist)

def sortnumber(time: int):             
    lucky_number = time%60
    if lucky_number != 0:
        return lucky_number
    else:
        return 60            

def timestamp():
    return  int(datetime.datetime.now().strftime("%f"))

while len(lucklist) < 6:          
    time.sleep(.01)
    number = sortnumber(timestamp())
    if number not in lucklist :
        lucklist.append(number)

print("These are your 6 lucky numbers")
sorted_numbers = sorted(lucklist)
print(sorted_numbers)






