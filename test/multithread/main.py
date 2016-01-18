# /usr/bin/env python
# encoding:utf8

import threading
import time
from time import sleep


def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


def test(nloop, nsec):
    print "start loop", nloop, ",at :", now()
    sleep(nsec)
    print "loop", nloop, "done,at :", now()


def main():
    print "-" * 33, "starting at : ", now(), "-" * 33
    threadpool = []

    for i in xrange(10):
        th = threading.Thread(target=test, args=(i, 2))
        threadpool.append(th)

    num = 0
    for th in threadpool:
        if num < 5:
            th.start()
        num = num + 1
        # pass

    # for th in threadpool:
        # threading.Thread.join(th)
        # pass

    print "-" * 33, "all Done, at : ", now(), "-" * 33

if __name__ == '__main__':
    main()
