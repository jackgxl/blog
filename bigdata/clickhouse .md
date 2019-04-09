# clickhouse_installation

**clickhouse CentOS7.6 rpm安装**

## 准备工作

检查是否支持SSE4.2

```shell

grep -q sse4_2 /proc/cpuinfo && echo "SSE 4.2 supported" || echo "SSE 4.2 not supported"

```

安装依赖包

```shell
yum install -y git clang libicu-devel readline-devel mysql-devel openssl-devel unixODBC_devel bzip2 gcc gcc-c++ make
```



* 下载RPM包
    
    [https://packagecloud.io/Altinity/clickhouse](https://packagecloud.io/Altinity/clickhouse)

```
[root@local-182 backup]# ls -al clickhouse-*
-rw-r--r-- 1 root root     6368 Apr  7 10:49 clickhouse-client-19.4.3.11-1.el7.x86_64.rpm
-rw-r--r-- 1 root root 26746084 Apr  7 11:20 clickhouse-common-static-19.4.3.11-1.el7.x86_64.rpm
-rw-r--r-- 1 root root  8743352 Apr  7 10:51 clickhouse-server-19.4.3.11-1.el7.x86_64.rpm
-rw-r--r-- 1 root root     9760 Apr  7 10:48 clickhouse-server-common-19.4.3.11-1.el7.x86_64.rpm
-rw-r--r-- 1 root root  1122768 Apr  7 10:47 clickhouse-test-19.4.3.11-1.el7.x86_64.rpm
```

* 安装

```
yum install clickhouse-*
```

* 验证

```
[root@local-182 ~]# clickhouse
Use one of the following commands:
clickhouse local [args] 
clickhouse client [args] 
clickhouse benchmark [args] 
clickhouse server [args] 
clickhouse performance-test [args] 
clickhouse extract-from-config [args] 
clickhouse compressor [args] 
clickhouse format [args] 
clickhouse copier [args] 
clickhouse obfuscator [args] 
[root@local-182 ~]# clickhouse server -h
usage: 
clickhouse [OPTION] [-- [ARG]...]
positional arguments can be used to rewrite config.xml properties, for 
example, --http_port=8010

-h, --help                        show help and exit
-V, --version                     show version and exit
--daemon                          Run application as a daemon.
--umask=mask                      Set the daemon's umask (octal, e.g. 027).
--pidfile=path                    Write the process ID of the application to 
                                  given file.
-C<file>, --config-file=<file>    load configuration from a given file
-L<file>, --log-file=<file>       use given log file
-E<file>, --errorlog-file=<file>  use given log file for errors only
-P<file>, --pid-file=<file>       use given pidfile
[root@local-182 ~]# 
```


## 修改配置文件




## 启动并验证







