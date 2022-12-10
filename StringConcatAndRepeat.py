userInput = input().split(" ")

str1 = userInput[0]
str2 = userInput[1]
a = int(userInput[2])


def concatenar(str1, str2):
    print(str1 + str2)

def repetir(str1, a):
    print((str1)* a)

def ambos(str1, str2, a):
    print((str1 + str2)* a)


concatenar(str1, str2)
repetir(str1, a)
ambos(str1, str2, a)