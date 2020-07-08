# redis6 安装

## 下载

```
wget https://github.com/antirez/redis/archive/6.0.4.tar.gz
```

## 编译安装

centos7 需要升级gcc

```
$ sudo yum install centos-release-scl
$ sudo yum install devtoolset-7
$ scl enable devtoolset-7 bash
```

生效环境

```
[ ~]$ source /opt/rh/devtoolset-7/enable 
[ ~]$ gcc --version
gcc (GCC) 7.3.1 20180303 (Red Hat 7.3.1-5)
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

编译安装

```
make
make test
make PREFIX=/usr/local/redis604 install
```


## 配置启动

```
/usr/local/redis604/bin/redis-server /data/redis6040/etc/redis.conf 
```


连接

```
[ redis6040]# /usr/local/redis604/bin/redis-cli -h 127.0.0.1 -p 6040
127.0.0.1:6040> info
NOAUTH Authentication required.
127.0.0.1:6040> AUTH 123
OK
127.0.0.1:6040> info
# Server
redis_version:6.0.4
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:37d560e9a2d2a9c
redis_mode:standalone
os:Linux 3.10.0-957.27.2.el7.x86_64 x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:7.3.1
process_id:29371
run_id:36bae8958b463b5ada15e28cd1a1f87fa0a078de
tcp_port:6040
pubsub_channels:0
```



## reference

[https://github.com/antirez/redis/issues/7177](https://github.com/antirez/redis/issues/7177)

[https://www.jianshu.com/p/76fb9b6a781b](https://www.jianshu.com/p/76fb9b6a781b)