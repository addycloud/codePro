#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import psutil
from pprint import pprint


def get_device_info():
    print("核心数", psutil.cpu_count())
    print("物理核心", psutil.cpu_count(logical=False))
    print(psutil.cpu_times())
    print(psutil.cpu_times_percent())
    print("频率", psutil.cpu_freq())
    print("", psutil.virtual_memory())
    print("交换内存", psutil.swap_memory())
    pprint(psutil.disk_partitions())
    print(psutil.disk_usage("C:\\"))
    pprint(psutil.disk_io_counters())
    pprint(psutil.disk_io_counters())
    pprint(psutil.disk_io_counters(perdisk=True))
    pprint(psutil.net_io_counters())
    pprint(psutil.net_if_addrs())
    pprint(psutil.net_connections())
    # 当前登录用户
    pprint(psutil.users())
    # 系统启动时间
    pprint(psutil.boot_time())
    # 进程pid
    pprint(psutil.pids())
    # 进程信息
    pprint(psutil.pid_exists(0))
    # 进程对象迭代器
    pprint(psutil.process_iter())
    # 获取进程对象
    pprint(psutil.Process(pid=0))
    # 进程所有信息
    p = psutil.Process(pid=148)

    # 进程名称
    print(p.name())  # WeChat.exe

    # 进程的exe路径
    print(p.exe())  # D:\WeChat\WeChat.exe

    # 进程的工作目录
    print(p.cwd())  # D:\WeChat

    # 进程启动的命令行
    print(p.cmdline())  # ['D:\\WeChat\\WeChat.exe']

    # 当前进程id
    print(p.pid)  # 16948

    # 父进程id
    print(p.ppid())  # 11700

    # 父进程
    print(p.parent())  # psutil.Process(pid=11700, name='explorer.exe', started='09:19:06')

    # 子进程列表
    pprint(p.children())

    # 进程状态
    print(p.status())  # running

    # 进程用户名
    print(p.username())  # LAPTOP-264ORES3\satori

    # 进程创建时间,返回时间戳
    print(p.create_time())  # 1561775539.0

    # 进程终端
    # 在windows上无法使用
    try:
        print(p.terminal())
    except Exception as e:
        print(e)  # 'Process' object has no attribute 'terminal'

    # 进程使用的cpu时间
    print(p.cpu_times())  # pcputimes(user=133.3125, system=188.203125, children_user=0.0, children_system=0.0)

    # 进程所使用的的内存
    print(p.memory_info())

    # 进程打开的文件
    pprint(p.open_files())

    # 进程相关的网络连接
    pprint(p.connections())

    # 进程内的线程数量，这个进程开启了多少个线程
    print(p.num_threads())  # 66

    # 这个进程内的所有线程信息
    pprint(p.threads())
    # 进程的环境变量
    pprint(p.environ())

    # 结束进程, 返回 None, 执行之后微信就会被强制关闭, 当然这里就不试了
    # print(p.terminal())
    # 模拟ps命令
    # psutil.test()


if __name__ == '__main__':
    get_device_info()
