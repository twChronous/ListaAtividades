hexadecimal = lambda userInput: hex(userInput)

for x in range(5):
    userInput = input()
    print(hexadecimal(int(userInput)))