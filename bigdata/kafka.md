# kafka

## 下载安装包

```shell
tar zxf kafka_2.11-1.0.0.tgz

```

## 配置Java环境

```shell
[root@local-153 kafka]# java -version
java version "1.8.0_191"
Java(TM) SE Runtime Environment (build 1.8.0_191-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.191-b12, mixed mode)
```

## 配置kafka

* 解压安装包

```shell
mv kafka_2.11-1.0.0 kafka
mv kafka /data/

```

* 修改配置文件

```shell
cd /data/kafka
vim config/zookeeper.properties
```

* 修改下面参数
    * zookeeper
    
        ```shell
        dataDir=/data/kafka/zookeeper
        maxClientCnxns=100
        ```
    
    * kafka
        
        ```
        listeners=PLAINTEXT://192.168.64.153:9092
        log.dirs=/data/kafka/logs/kafka-logs
        ```

## 启动关闭

```shell
[root@local-153 kafka]# cat kafka.sh 
#!/bin/sh

nohup /data/kafka/bin/zookeeper-server-start.sh /data/kafka/config/zookeeper.properties >zoo_1.out 2>&1 &

nohup /data/kafka/bin/kafka-server-start.sh /data/kafka/config/server.properties >kafka.out 2>&1 &
```

## 验证

```
ps -ef|grep 'zookeeper' 
ps -ef |grep 'kafka'
```

