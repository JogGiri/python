import time
from plyer import notification
#for mac users plyer can be replaced by pync.notify

if __name__ == "__main__" :
    def reminder():
        notification.notify(title ="BR",ticker ='Hi', message = "HS PTAB 20!", timeout =1)

while True:
    reminder()
    time.sleep(1200)


