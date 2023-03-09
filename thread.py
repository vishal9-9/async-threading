import threading
from time import sleep


def thread_a():
    print("thread 1")
    sleep(2)
    print("thread <1")

def thread_b():
    print("thread 2")
    sleep(4)
    print("thread <2")

x = threading.Thread(target=thread_a)
y = threading.Thread(target=thread_b)

x.start()
y.start()

# x.join()
# y.join()

print("Executing")
