# 服务器监控



## CPU负载监控

​	top
​	
​	 perf top -e cpu-clock
​	 

## 磁盘空间监控

df/du

## 磁盘IO速率监控

 iotop

    
## 内存监控

​	top/free

## 进程/线程/打开文件监控

​	top/ps/lsof
​	
​	lsof -i `pid of mysql`

## 网络端口打开以及状态监控

​	netstat/ss
​	
​	ss -ltn
​	
​	netstat -s |egrep "listen|LISTEN"
​	
​	mpstat 
​	
​	sar -n DEV 1 3

## 网络流量/带宽监控

​	iftop

## 用户活动监控

​	psacct/acct

