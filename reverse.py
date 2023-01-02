number = input()

if number[:1] == "-":
    print("-" + number[::-1].replace("-", ""))
else:
    print(number[::-1])