numero = int(input())

number = 1
def teste(number):
    print("{number} {elefante} muita gente..."
        .format(
            number = number + x,
            elefante = "elefantes incomodam" if number + x > 1 else "elefante incomoda"
        )
    )
    print("{number} elefantes{anoy} incomodam muito mais... "
        .format(
            number = number + x + 1,  
            anoy = (number + x) * " incomodam,"
        )
    )

for x in range(numero):
   teste(number)