# ES

### 下载

下载地址

```shell
https://www.elastic.co/cn/downloads/elasticsearch
```

### 安装

环境依赖 java8

解压

```
tar zxf elasticsearch-7.3.0-linux-x86_64.tar.gz
```

创建数据、日志目录

```shell
mkdir /data/es/{log,data} -pv
```

### 修改配置文件

```
cd elasticsearch-7.3.0

vim elasticsearch.yml //配置文件

cluster.name: //集群名称
node.name: //集群节点名称
path.data //数据目录
path.logs //日志目录
network.host:  //网络
http.port:     //端口
discovery.seed_hosts //集群成员
```

### 启动

创建启动用户

```
useradd esuser

chown -R esuser:esuser elasticsearch-7.3.0
chown -R esuser:esuser es
```

启动

```
sudo -u esuser /home/elasticsearch-7.3.0/bin/elasticsearch -d
```


验证 

```
curl 'http://127.0.0.1:9200/?pretty'
{
  "name" : "node-1",
  "cluster_name" : "my-application",
  "cluster_uuid" : "3belA_qjTfSdB_lrv-hWEg",
  "version" : {
    "number" : "7.3.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "de777fa",
    "build_date" : "2019-07-24T18:30:11.767338Z",
    "build_snapshot" : false,
    "lucene_version" : "8.1.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```