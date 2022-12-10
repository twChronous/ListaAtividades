def maravilhosos(num: int) :
    if num != 1 and num % 2 != 0: 
        number_state = 3 * num + 1
        print(number_state)
        maravilhosos(number_state)
    elif num != 1 and num % 2 == 0 :
        number_state = num // 2
        print(number_state)
        maravilhosos(number_state)
    

input_number = int(input())
maravilhosos(input_number)
