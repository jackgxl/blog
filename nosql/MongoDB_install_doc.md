# MongoDB\_install\_doc

## MongoDB配置优化

* 主机配置

    ```
    CPU主频越高越好
    尽量使用大内存机器，例如128G以上
    磁盘RAID10，SSD更佳
    ```

* 系统配置

    ```
    内核调整：
    echo never > /sys/kernel/mm/transparent_hugepage/enabled
    echo never > /sys/kernel/mm/transparent_hugepage/defrag
    ```
    ```
    用户创建：
        useradd -M -s /sbin/nologin mongo
    用户限制：
        mongo soft nofile 640000
        mongo hard nofile 640000
        mongo soft nproc 320000
        mongo hard nproc 320000
    
    ```

## MongoDB 下载

```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-4.0.5.tgz
```



## mongod配置启动 

* 配置

```
net:
  port: 27019
  bindIp: 0.0.0.0 
  maxIncomingConnections: 5000
  unixDomainSocket:
    enabled: true
    pathPrefix: "/data/mongo27019/tmp"
    filePermissions: 0700



storage:
    engine: wiredTiger
    directoryPerDB: true
    dbPath: /data/mongo27019/var
    journal:
        enabled: true
    wiredTiger:
        engineConfig:
            cacheSizeGB: 2
            directoryForIndexes: true
        collectionConfig:
            blockCompressor: "snappy"
        indexConfig:
              prefixCompression: true


systemLog:
    verbosity: 0
    quiet: true
    traceAllExceptions: false
    destination: file
    logAppend: true
    path: /data/mongo27019/log/mongo27019.log
    logRotate: rename
    

operationProfiling:
  slowOpThresholdMs: 10000

replication:
    oplogSizeMB: 10240
    replSetName: rep1 

processManagement:
    fork: true
    pidFilePath: /data/mongo27019/var/mongo27019.pid
   
```
    
* 文件构成：

```
[root@local-153 data]# tree  mongo27019
mongo27019
├── etc
│   ├── mongo.conf
│   ├── mongo.yaml
│   └── mongo.yaml_bak
├── keyfile
│   └── mongo.key
├── log
│   └── mongo27019.log
├── mongo.sh
├── tmp
│   └── mongodb-27019.sock
└── var
    ├── admin
    │   ├── collection
    │   │   ├── 3-7230440791240647951.wt
    │   │   └── 9-7230440791240647951.wt
    │   └── index
    │       ├── 10-7230440791240647951.wt
    │       └── 4-7230440791240647951.wt
    ├── config
    │   ├── collection
    │   │   ├── 0--178031148169352816.wt
    │   │   └── 7-7230440791240647951.wt
    │   └── index
    │       ├── 1--178031148169352816.wt
    │       ├── 2--178031148169352816.wt
    │       └── 8-7230440791240647951.wt
    ├── diagnostic.data
    │   ├── metrics.2019-03-06T09-34-19Z-00000
    │   ├── metrics.2019-03-06T10-02-37Z-00000
    │   ├── metrics.2019-03-06T10-04-51Z-00000
    │   ├── metrics.2019-03-07T02-57-32Z-00000
    │   ├── metrics.2019-03-07T02-57-54Z-00000
    │   ├── metrics.2019-03-07T05-46-00Z-00000
    │   ├── metrics.2019-03-07T05-46-14Z-00000
    │   ├── metrics.2019-03-07T05-47-38Z-00000
    │   ├── metrics.2019-03-07T05-50-11Z-00000
    │   ├── metrics.2019-03-07T06-25-50Z-00000
    │   ├── metrics.2019-03-07T07-32-58Z-00000
    │   ├── metrics.2019-03-07T08-31-55Z-00000
    │   ├── metrics.2019-03-07T08-38-05Z-00000
    │   ├── metrics.2019-03-08T07-05-15Z-00000
    │   ├── metrics.2019-03-08T07-47-09Z-00000
    │   └── metrics.interim
    ├── journal
    │   ├── WiredTigerLog.0000000015
    │   ├── WiredTigerPreplog.0000000001
    │   └── WiredTigerPreplog.0000000002
    ├── local
    │   ├── collection
    │   │   ├── 0-7230440791240647951.wt
    │   │   ├── 0--7459329023185180427.wt
    │   │   ├── 1-7230440791240647951.wt
    │   │   ├── 2--7459329023185180427.wt
    │   │   ├── 4--7459329023185180427.wt
    │   │   ├── 5-7230440791240647951.wt
    │   │   └── 6--7459329023185180427.wt
    │   └── index
    │       ├── 1--7459329023185180427.wt
    │       ├── 2-7230440791240647951.wt
    │       ├── 3--7459329023185180427.wt
    │       ├── 5--7459329023185180427.wt
    │       ├── 6-7230440791240647951.wt
    │       └── 7--7459329023185180427.wt
    ├── _mdb_catalog.wt
    ├── mongo27019.pid
    ├── mongodb.pid
    ├── mongod.lock
    ├── sizeStorer.wt
    ├── storage.bson
    ├── test
    │   ├── collection
    │   │   └── 0-6909658059796592381.wt
    │   └── index
    │       └── 1-6909658059796592381.wt
    ├── WiredTiger
    ├── WiredTigerLAS.wt
    ├── WiredTiger.lock
    ├── WiredTiger.turtle
    └── WiredTiger.wt

19 directories, 61 files
``` 
    
* 启动

    ```
    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml
    ```
* 关闭
    * 方法1

    
    ```
    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml --shutdown
    ```
    
    * 方法2
    
    ```
    use admin;
    db.shutdownServer();                //普通关闭
    db.shutdownServer({force:true});    //强制关闭 副本集单主时必须使用强制关闭
    ```


**启动关闭mongodb时注意启动用户**

```
用root用户启动的mongodb，普通用户用--shutdown关闭不了，必须登陆mongodb内部关闭。
```

* 查看mongo启动方式和用户

```
[root@local-153 mongo27019]# ps -ef | grep mongo
root      7713  7445  0 11:02 pts/0    00:00:00 su - mongo
mongo     7714  7713  0 11:02 pts/0    00:00:00 -bash
root      8022  7540  0 13:45 pts/2    00:00:00 su - mongo
mongo     8023  8022  0 13:45 pts/2    00:00:00 -bash
mongo     8186  7714  0 13:47 pts/0    00:00:00 tail -f log/mongo27019.log
root      8385     1  0 14:25 ?        00:00:19 /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml
mongo     8448  8023  0 14:26 pts/2    00:00:00 /usr/local/mongodb/bin/mongo 127.0.0.1:27019
root      8519  7564  0 15:21 pts/3    00:00:00 grep --color=auto mongo
```

* 启动脚本

```shell
[root@local-153 mongo27019]# cat mongo.sh 
#!/bin/bash

start(){

    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml
    echo "mongo start~"

}

stop(){
    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml --shutdown
    sleep 3
    echo "mongo stopped!"
}

case "$1" in 
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo $"Usage: $0 {start|stop|restart}"
        exit 1
esac
```

## MongoDB 副本集配置

* 创建其他端口的mongodb实例
    * 复制配置文件，启动脚本
    * 修改端口
    * 启动
     
* 进入27019 端口开启副本集
    
    ```shell
    conf = { _id : "rep1", members : [     {_id :0 ,host : "192.168.64.112:27019"},    {_id :1,host:"192.168.64.113:27019"},{_id :2,host:"192.168.64.101:27019"},]}
    
    rs.initiate(conf)
    ```
     
* 加入新的端口(27020,27018)

    ```
     rs.add("IP:Port")
    ```
* 查看集群状态

    ```
    rs.status();
    rs.conf();
    ```
* 创建keyFile


## mongo_config 配置

```

```


## mongos 配置

```

```


## reference

<a>http://www.mongoing.com/docs/reference/configuration-options.html#storage-options

<a>https://blog.csdn.net/u014686399/article/details/84396240

<a> http://www.lanceyan.com/tech/mongodb_repset2.html
