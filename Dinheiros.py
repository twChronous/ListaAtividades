def dinheiros(liters,val1, val2):
    if 2* val1 <= val2:
        print(val1*liters)
    else:
        print(((liters//2)*val2)+ ((liters%2)*val1))