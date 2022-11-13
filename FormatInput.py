firstUserInput = input("Digite um caractere alfanumerico (a-Z,0-9):\n")
secondUserInput = input("Digite um caractere alfanumerico novamente (a-Z,0-9):\n")
thirdUserInput = input("Digite um caractere alfanumerico novamente (a-Z,0-9):\n")

print(f"{firstUserInput}{secondUserInput}{thirdUserInput}\n")
print(f"{firstUserInput} \n{2*secondUserInput}\n")
print(f"{thirdUserInput} {thirdUserInput} {thirdUserInput}\n")
print(f"X == {firstUserInput}, Y == {secondUserInput}, Z == {thirdUserInput}\n")
print(f"X != {secondUserInput}, Y != {firstUserInput}, Z == {thirdUserInput}")