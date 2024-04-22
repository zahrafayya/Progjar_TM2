import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName) - 10s) %(message)s', )

class MyThread(threading.Thread):
    def __init__(self, num):
        # perlu di-init karena dia akan menempelkan parameter num di self
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        logging.debug('running')

for i in range(5):
    t = MyThread(i)
    t.start()