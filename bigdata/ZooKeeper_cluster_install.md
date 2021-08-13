# ZooKeeper 集群安装配置

## 下载安装包

```shell
http://mirror.bit.edu.cn/apache/zookeeper/stable/apache-zookeeper-3.5.5-bin.tar.gz

https://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html

```

```shell
[gaoxueliang@SYQ-101 ~]$ ls
apache-zookeeper-3.5.5-bin.tar.gz  jdk-8u201-linux-x64.tar.gz
```

```
tar zxf jdk-8u201-linux-x64.tar.gz 
tar zxf apache-zookeeper-3.5.5-bin.tar.gz

[gaoxueliang@SYQ-101 ~]$ ls
apache-zookeeper-3.5.5-bin  apache-zookeeper-3.5.5-bin.tar.gz  jdk-8u201-linux-x64.tar.gz  jdk1.8.0_201

mv jdk1.8.0_201 /usr/local/
cd /usr/local/
ln -sv jdk1.8.0_201 java

[gaoxueliang@SYQ-101 ~]$ mv apache-zookeeper-3.5.5-bin zookeeper
[gaoxueliang@SYQ-101 ~]$ mv zookeeper /data/
cd /data/zookeeper/
mkdir data
```

## 修改JAVA环境变量

```
[gaoxueliang@SYQ-101 ~]$ vim /etc/profile.d/java.sh 
#!/bin/bash

export JAVA_HOME=/usr/local/java
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export PATH=$PATH:$JAVA_HOME/bin
```

## 修改ZooKeeper配置文件

```
[gaoxueliang@SYQ-101 ~]$ cat /data/zookeeper/conf/zoo.cfg|grep -v '#'
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/data/zookeeper/data
clientPort=2181
maxClientCnxns=2000
server.0=192.168.101.01:2888:3888
server.1=192.168.101.02:2888:3888
server.2=192.168.101.03:2888:3888
4lw.commands.whitelist=*
```
## 启动

```
三台机器分别 启动JAVA 和ZooKeeper 环境
开启服务
/data/zookeeper/bin/zkServer.sh start 
查看状态
/data/zookeeper/bin/zkServer.sh status
关闭服务
/data/zookeeper/bin/zkServer.sh stop
```

## 监控

**通过zookeeper自带的 four letter words command 获取各种各样的监控指标**
    
```
conf: 输出相关服务配置的详细信息。
cons：列出所有连接到服务器的客户端的完全的连接 /会话的详细信息。包括“接受 / 发送”的包数量、会话 id 、操作延迟、最后的操作执行等等信息。
dump：列出未经处理的会话和临时节点。
envi：输出关于服务环境的详细信息（区别于 conf命令）。
reqs：列出未经处理的请求
ruok：测试服务是否处于正确状态。如果确实如此，那么服务返回“imok ”，否则不做任何相应。
stat：输出关于性能和连接的客户端的列表。
wchs：列出服务器 watch的详细信息。
wchc：通过 session列出服务器 watch的详细信息，它的输出是一个与watch相关的会话的列表。
wchp：通过路径列出服务器 watch的详细信息。它输出一个与 session相关的路径。
mntr：用于监控zookeeper server 健康状态的各种指标
```

```
[gaoxueliang@SYQ-101 ~]$ echo mntr |nc 127.0.0.1 21810
zk_version      3.4.13-2d71af4dbe22557fda74f9a9b4309b15a7487f03, built on 06/29/2018 04:05 GMT
zk_avg_latency  0
zk_max_latency  0
zk_min_latency  0
zk_packets_received     1
zk_packets_sent 0
zk_num_alive_connections        1
zk_outstanding_requests 0
zk_server_state leader
zk_znode_count  11
zk_watch_count  0
zk_ephemerals_count     0
zk_approximate_data_size        1262
zk_open_file_descriptor_count   34
zk_max_file_descriptor_count    65536
zk_fsync_threshold_exceed_count 0
zk_followers    2
zk_synced_followers     2
zk_pending_syncs        0
zk_last_proposal_size   -1
zk_max_proposal_size    -1
zk_min_proposal_size    -1
```


## reference

[https://zookeeper.apache.org/doc/r3.4.12/zookeeperAdmin.html#sc_zkCommands]()

[https://www.cnblogs.com/smail-bao/p/7201091.html]()

[https://www.jianshu.com/p/46fe612b9dda](https://www.jianshu.com/p/46fe612b9dda)
