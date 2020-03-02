import threading
import time


def threadCb(count):
    time.sleep(1)
    print(count)


# 1234 or 1243
print(1)
threading.Thread(target=threadCb, kwargs={'count': 3}).start()
threading.Thread(target=threadCb, kwargs={'count': 4}).start()
print(2)
