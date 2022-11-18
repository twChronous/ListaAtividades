def quantosSemestres(m, a, s):
    firstYearAndSemester = str(m)[:4]
    firstYear = int(firstYearAndSemester[:2])
    firstSemester = int(firstYearAndSemester[2:])
    semesters = (int(str(a)[2:]) - firstYear)*2

    if(firstSemester == 0 and s == 1):
        print(semesters + 1)
    elif(firstSemester == 1 and s == 0):
        print(semesters - 1)
    else: 
        print(semesters)
    