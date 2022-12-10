def ritmoMedio(h,m,s, d):
    secondsToMinutes = s / 60
    hoursToMinutes = h * 60
    totalMinutes =  m + secondsToMinutes +hoursToMinutes 

    rest = (totalMinutes / d) * 60
    print(rest)
    minutes, seconds = divmod(rest, 60)
    minutes = str(minutes).split('.')[0]
    seconds = str(seconds).split('.')[0]
    print(f"{minutes.zfill(2)}:{seconds.zfill(2)} min/km")

ritmoMedio(0,22,50,5.5)
ritmoMedio(1,1,25,22.3)