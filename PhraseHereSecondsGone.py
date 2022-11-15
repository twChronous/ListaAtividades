import datetime
import time

userInput = input()
x = time.strptime(userInput,'%H:%M:%S')
seconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
print(f"La se foram {str(seconds).split('.')[0]} segundos que nao voltam mais...")