def quantosJantam(people, fork,knifes, spoons):
    if fork != 0 and knifes != 0 and spoons != 0 and people != 0:
        number = min(fork, knifes) + spoons
        print(min(number, people))
    elif (people == 0 and spoons != 0) or (fork == 0 and spoons != 0):
        print(min(spoons, people))
