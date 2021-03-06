#! /usr/bin/python3
# -*- coding:utf-8 -*-


import threading
import time

count = 0


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp


threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(f'Final count: {count}')
