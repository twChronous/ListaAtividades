userInput = input()

handledUserInput = str(userInput).split(" ")
base = handledUserInput[0]
power = handledUserInput[1]

print(pow(float(base), float(power)))