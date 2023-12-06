import time
from plyer import notification
#for mac users plyer can be replaced by pync.notify

if __name__ == "__main__" :
    def reminder():
        notification.notify(title ="Break Notification", message = "Please take a break", timeout =1)

while True:
    reminder()
    time.sleep(1200)


