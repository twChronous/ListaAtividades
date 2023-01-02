import re
number = int(input())

def test(string):
    i = 0
    splited = re.split('(\d+)', string)
 
    decodified = ""
    while i < len(splited) -1 :
        decodified += splited[i] * int(splited[i + 1])
        i += 2
    print(decodified)

for x in range(number):
    string = input()
    test(string)