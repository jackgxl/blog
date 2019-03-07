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
    用户创建：
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
    
    
* 启动

    ```
    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml
    ```
* 关闭

    ```
    /usr/local/mongodb/bin/mongod -f /data/mongo27019/etc/mongo.yaml --shutdown
    ```
    
    ```
    use admin;
    db.shutdownServer();                //普通关闭
    db.shutdownServer({force:true});    //强制关闭 副本集单主时必须使用强制关闭
    ```


**启动关闭mongodb时注意启动用户**

```
用root用户启动的mongodb，普通用户用--shutdown关闭不了，必须登陆mongodb内部关闭。
```

查看mongo启动方式和用户

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


## MongoDB 副本集配置

* 创建其他端口的mongodb实例
* 进入27019 端口开启副本集
* 加入新的端口(27020)
* 查看集群状态



## mongo_conf 配置

```


```


## mongos 配置

```

```


## reference

<a>http://www.mongoing.com/docs/reference/configuration-options.html#storage-options

<a>https://blog.csdn.net/u014686399/article/details/84396240

<a> http://www.lanceyan.com/tech/mongodb_repset2.html
