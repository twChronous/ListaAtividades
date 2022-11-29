def banner(num):
    if num > 0 and (num % 2) == 0:
        print("| | | | | | | | | |")
    elif num > 0 and (num % 2) != 0:
        print("- - - - - - - - - -")
    elif num < 0 and (num % 2) == 0:
        print(". . . . . . . . . .")
    elif num < 0 and (num % 2) != 0:
        print("= = = = = = = = = =")