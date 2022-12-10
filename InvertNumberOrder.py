def trocarAB(a, b):
    print(b, a)

for x in range(5):
    firstLine = input()
    handledUserInput = str(firstLine).split(" ")
    firstNumber = int(handledUserInput[0])
    secondNumber = int(handledUserInput[1])
    trocarAB(firstNumber, secondNumber)
    