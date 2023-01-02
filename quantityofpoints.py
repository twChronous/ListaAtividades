numero = input()

numbers = list()
i = 0

numbers = numero.split()
numbers = [int(i) for i in numbers]

print(f"{min(numbers)} {numbers.index(min(numbers))}")
print(f"{max(numbers)} {numbers.index(max(numbers))}")
print(numero)
