largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        ## write your code here
        num = int(num)

        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        ## write your code here
        print("Invalid number")
        continue

print("Maximum", largest)
print("Minimun", smallest)
## write another print statement here
