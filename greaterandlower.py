numero = int(input())

numbers = list()
for x in range(numero):
    numbers.append(int(input()))

print(f"Menor: {min(numbers)}")
print(f"Maior: {max(numbers)}")