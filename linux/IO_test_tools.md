# 磁盘速度测试工具

[TOC]

## Linux tools

```shell
nethogs:按进程查案流量占用
iptraf：按连接/端口查看流量
ifstat：按设备查看流量
ethtool：诊断工具
tcpdump：抓包工具
pstack :    gdb调试
ss：连接查看工具
其他：dstat  slurm  nload  bmon nc
sar -n DEV 1 4
sar -n tcp,etcp 1
load -u K

监控总体带宽使用――nload、bmon、slurm、bwm-ng、cbm、speedometer和netload
监控总体带宽使用（批量式输出）――vnstat、ifstat、dstat和collectl
每个套接字连接的带宽使用――iftop、iptraf、tcptrack、pktstat、netwatch和trafshow
每个进程的带宽使用――nethogs
```

## fio

```shell

```

## CPU 绑定

```
taskset  绑定cpu 

taskset -p -c 10  1220 //把1220 绑定到第10号cpu上
```

## lshw

```shell
yum install lshw -y
```
## mpstat

## 