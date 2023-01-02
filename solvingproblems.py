numero = int(input())

solvingproblems = 0
for x in range(numero):
    problems = input().split()
    if (int(problems[0]) + int(problems[1]) + int(problems[2])) >= 2:
        solvingproblems += 1
print(solvingproblems)