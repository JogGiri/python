import time

seconds = int(input("enter the seconds : "))


while seconds >= 0:
    mins, sec = divmod(seconds, 60)
    timer_display = "{:02d}:{:02d}".format(mins, sec)
    print(timer_display, end="\r")
    time.sleep(1)
    seconds -= 1

print("Timer expired!")