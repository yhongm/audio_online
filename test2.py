import os
import sched
import time


def worker(msg, stime):
    print("time:" + str(time.time()) + ",msg:" + msg + ",stime:" + str(stime))


def test2():
    pass


def test():
    s = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)
    s1 = str(time.time())
    s.enter(1, 1, worker, ('hello1', time.time()))
    s.enter(10, 1, worker, ('hello10', time.time()))
    s.enter(15, 1, worker, ('test15', time.time()))
    s.run()


if __name__ == "__main__":
    print("starttime:" + str(time.time()))
    test()
