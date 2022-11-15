userInput = input()

handledUserInput = str(userInput).split("/")
day = handledUserInput[0]
month = handledUserInput[1]
year = handledUserInput[2]

print(f"{day}-{month}-{year}")
print(f"{month}-{day}-{year}")
print(f"{year}/{month}/{day}")