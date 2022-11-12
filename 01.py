import os

userInput = input("Digite um caractere alfanumerico (a-Z,0-9):\n")

os.system('cls' if os.name == 'nt' else 'clear')
print("{userInput}\n{userInput}{userInput}\n{userInput} {userInput}\n2{userInput}\n[{userInput}]\n".format(
    userInput = userInput
))