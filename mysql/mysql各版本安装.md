#mysql安装文档
**安装前环境配置**：

创建用户：

```
useradd -M -s /sbin/nologin  mysql 
```
配置依赖环境：

```
yum install gcc gcc-c++ cmake  make  autoconf automake ncurses-devel  libaio.x86_64 libaio-devel.x86_64 readline.x86_64 readline-devel.x86_64
```
配置系统环境：
		
	echo vm.swappiness = 0 >>/etc/sysctl.conf
	sysctl -p
	echo deadline> /sys/block/sda/queue/scheduler
	vim /etc/security/limits.conf 
			* soft nofile 65536
			* hard nofile 65536
			* soft nproc 65535
			* hard nproc 65535
##mysql5.1
##msyql5.5
##mysql5.6