#!/bin/env python3
# -*- coding:utf-8 -*-

# process and system utilties
# psutil module
# 无需解析代码、跨平台

import psutil

# 获取cpu信息
print(
    psutil.cpu_count(),  # CPU逻辑数量
    psutil.cpu_count(logical=False),  # CPU物理核心
    psutil.cpu_times()
)

# cpu使用频率
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取mem信息
print(
    psutil.virtual_memory(),  # 物理内存信息，单位整数字节
    psutil.swap_memory()  # 交换分区信息
)
# 获取磁盘信息
print(
    psutil.disk_partitions(),  # 磁盘分区信息
    psutil.disk_usage('c:\\'),  # 磁盘使用情况
    psutil.disk_io_counters()  # 磁盘IO
)

# 获取网络信息
print(
    psutil.net_io_counters(),  # 获取网络读写包个数
    psutil.net_if_addrs(),  # 获取网络接口信息
    psutil.net_if_stats(),  # 获取网络接口状态
    psutil.net_connections()  # 获取网络连接信息
)

# 获取进程信息
p = psutil.Process(3376)
print(
    psutil.pids(),  # 所有进程ID
    p.name(),  # 进程名称
    p.exe(),  # 进程exe路径
    p.cwd(),  # 进程工作目录
    p.cmdline(),  # 进程启动命令行
    p.ppid(),  # 父进程ID
    p.children(),  # 子进程列表
    p.status(),  # 进程状态
    p.username(),  # 进程用户名
    p.create_time(),  # 进程创建时间
    p.terminal(),  # 进程终端
    p.cpu_times,  # 进程使用的cpu时间
    p.memory_info,  # 进程使用的内存
    p.open_files(),  # 进程打开的文件
    p.connections(),  # 进程相关网络连接
    p.num_threads(),  # 进程的线程数量
    p.environ(),  # 进程环境变量
    p.terminal()  # 结束进程
)

# 模拟ps command
print(
    psutil.test()
)
