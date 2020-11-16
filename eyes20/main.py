import time
from win10toast import ToastNotifier


def start():
    userInput = input("Start? (y/n)")
    if userInput == "y":
        timer()
    else:
        exit()


def showNotification():
    n.show_toast("EYES20", "Take A Quick 20 Scecond Break!", duration=20)


def timer():
    print("executing")
    time.sleep(1200)
    showNotification()
    repeat()


def repeat():
    userInput = input("Repeat? (y/n)")
    if userInput == "y":
        timer()
    else:
        exit()


if __name__ == "__main__":
    n = ToastNotifier()
    start()
