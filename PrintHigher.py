for x in range(5):
    firstLine = input()
    handledUserInput = str(firstLine).split(" ")
    firstNumber = int(handledUserInput[0])
    secondNumber = int(handledUserInput[1])
    if(firstNumber > secondNumber): print(firstNumber)
    else: print(secondNumber)
