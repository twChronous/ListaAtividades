def area(num1,num2,str1):
    if str1 == "losango":
        equation = num1 * num2 // 2
        print(f"O {str1} tem {equation} de area")
    elif str1 == "retangulo":
        equation = num1 * num2
        print(f"O {str1} tem {equation} de area")
    elif str1 == "triangulo":
        equation = num1 * num2 // 2
        print(f"O {str1} tem {equation} de area")
    elif str1 == "circulo":
        equation = (num1 * num2 )** 2
        print(f"O {str1} tem {equation} de area")