def piscininha(x,y,widht,height,a,b):
    if x + widht > a and y + height > b > y:
        print("Dando um tchibum")
    elif (x + widht < a or a < x ) or (y+ height < b or b < y):
        print("Tomando um solzinho")
    else:
        print("pe")