import threading

import time


def worker():
    count = 0

    while True:
        if (count >= 5):
            # raise RuntimeError()
          break
        time.sleep(1)
        print("I'm working")
        count += 1


t = threading.Thread(target=worker, name='worker')  # 线程对象.

t.start()  # 启动.

print("==End==")