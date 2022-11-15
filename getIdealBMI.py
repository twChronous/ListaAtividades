equationMale = lambda height:  72.7 * float(height) - 58
equationFemale = lambda height: 62.1 * float(height) - 44.7

def peso_ideal(userInput):
    print("%.2f" %equationMale(userInput),  "%.2f" %equationFemale(userInput))

userInput = input()
peso_ideal(userInput)