def age(inputNumber):
    years = inputNumber // 360
    months = (inputNumber - years * 360) // 30
    days = (inputNumber - years * 360 - months*30)
    print(f"{years} ano(s), {months} mes(es) e {days} dia(s)")

userInput = input()
handledUserInput = str(userInput).split(" ")

for inputNumber in handledUserInput:
    age(int(inputNumber))