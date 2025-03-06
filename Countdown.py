import time as t
try:
    time: int = int(input("Enter time (s):"))
    for i in range(time):
        seconds: int = time
        hours: int = seconds//3600
        seconds = seconds - (hours*3600)
        minutes: int = seconds//60
        seconds = seconds - (minutes*60)
        print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}", end = "\r")
        time = time - 1
        t.sleep(1)
    print("00:00:00")
    print("Time Up!!")
except ValueError:
    print("Wrong input!!")
