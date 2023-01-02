number = int(input())

finalNumber = 0

for x in range(number):
    operation = input().replace("x", "")

    if operation == "++":
        finalNumber += 1
    elif operation == "--":
        finalNumber -= 1
        
print(finalNumber)