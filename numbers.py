count = 0
total = 0
maximum = None
minimum = None

while True:
    num = int(input("enter a number (0 to stop):"))
    if num == 0:
        break
    count+=1
    total+=num

    if maximum is None or num > maximum:
        maximum = num

    if minimum is None or num < minimum:
        minimum = num

print("count=",count)
print("sum=",total)
print("maximum=",maximum)
print("minimum=",minimum)