# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/3 8:23
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : multiFoundation.py

# 进程和线程

from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random


def run_proc(name):
    print "子进程 %s(线程ID %s)" % (name, os.getpid())


if __name__ == '__main__':
    print "父进程 %s" % os.getpid()
    for i in range(5):
        print "正在启动创建新进程。。。"
        p = Process(target=run_proc, args=str(i))
        print "新进程即将启动。。。"
        p.start()
        #
        p.join()  # 实现进程间同步

    print "创建进程结束"


# 进程池的方式创建进程

def run_task(name):
    print "Task %s (pid = %s) is running..." % (name, os.getpid())
    time.sleep(random.random() * 3)
    print "Task %s end ." % name


if __name__ == "__main__":
    print "Current process %s." % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print "Waiting for all subprocesses done..."
    p.close()
    p.join()  # 调用join之前必须调用close
    print "All subprocesses done."


# 进程间通信
# 进程间通信是一个很古老的话题，在其他语言中进程通信一般是管道,MQ,Socket,Http等来实现。
# 此处的进程间通信主要的子进程间的通信，不的独立进程间的通信
