import time
from plyer import notification

minutes = int(input("Enter reminder interval (minutes): "))

while True:
    notification.notify(
        title="💧 Drink Water",
        message="Hey! It's time to drink water 💙",
        timeout=5
    )
    time.sleep(minutes * 60)
