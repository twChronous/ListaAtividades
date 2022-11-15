userInput = input()

handledUserInput = str(userInput).split(" ")

firstNumber = float(handledUserInput[0])
secondNumber = float(handledUserInput[1])
thirdNumber = float(handledUserInput[2])

percent = lambda part: (10 / 100 * part) + part

print(percent(firstNumber) , percent(secondNumber) , percent(thirdNumber))
print(round(percent(firstNumber) + percent(secondNumber) + percent(thirdNumber), 3))