# ES

### 下载

下载地址

```shell
https://www.elastic.co/cn/downloads/elasticsearch
```

### 安装

环境依赖 java11,自带jdk

解压

```shell
tar zxf elasticsearch-7.7.1-linux-x86_64.tar.gz -C /data
cd /data
mv elasticsearch-7.7.1 es
```

创建数据、日志目录

```shell
mkdir /data/es/{logs,data} -pv
```

### 修改配置文件

```shell
cd es

vim config/elasticsearch.yml //配置文件

cluster.name: //集群名称
node.name: //集群节点名称
path.data //数据目录
path.logs //日志目录
network.host:  //网络
http.port:     //端口
discovery.seed_hosts //集群成员

cat config/elasticsearch.yml |grep -v '#'
cluster.name: my-application
node.name: node-109
path.data: /data/es/data
path.logs: /data/es/logs
network.host: 192.168.64.109
http.port: 19200
discovery.seed_hosts: ["192.168.1.154", "192.168.1.157","192.168.1.109"]
cluster.initial_master_nodes: ["node-154", "node-109"]
```

### 启动

创建启动用户

```bash
useradd es
chown -R es:es es
```

启动

```bash
sudo -u es /data/es/bin/elasticsearch -d
```



每个实例依此安装，启动，集群自动发现

验证 

```json
curl 'http://192.168.64.109:19200/?pretty'
{
  "name" : "node-109",
  "cluster_name" : "my-application",
  "cluster_uuid" : "Lej1uHFsSMWNLotUPwx-jg",
  "version" : {
    "number" : "7.7.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "ad56dce891c901a492bb1ee393f12dfff473a423",
    "build_date" : "2020-05-28T16:30:01.040088Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```



## 监控

### top10 指标

```shell
Cluster Health – Nodes and Shards
Search Performance – Request Latency and
Search Performance – Request Rate
Indexing Performance – Refresh Times
Indexing Performance – Merge Times
Node Health – Memory Usage
Node Health – Disk I/O
Node Health – CPU
JVM Health – Heap Usage and Garbage Collection
JVM health – JVM Pool Size
```



```
_cluster/health
_cluster/health?level=indices
_cluster/health?level=shards
_cluster/health?wait_for_status=green
```



jvm

http://192.168.64.154:19200/_nodes/?pretty

mem

threads

gc

```json
 "jvm": {
                "pid": 70604,
                "version": "11.0.7",
                "vm_name": "Java HotSpot(TM) 64-Bit Server VM",
                "vm_version": "11.0.7+8-LTS",
                "vm_vendor": "Oracle Corporation",
                "bundled_jdk": true,
                "using_bundled_jdk": false,
                "start_time_in_millis": 1592535385707,
                "mem": {
                    "heap_init_in_bytes": 1073741824,
                    "heap_max_in_bytes": 1037959168,
                    "non_heap_init_in_bytes": 7667712,
                    "non_heap_max_in_bytes": 0,
                    "direct_max_in_bytes": 0
                },
                "gc_collectors": [
                    "ParNew",
                    "ConcurrentMarkSweep"
                ],
                "memory_pools": [
                    "CodeHeap 'non-nmethods'",
                    "Metaspace",
                    "CodeHeap 'profiled nmethods'",
                    "Compressed Class Space",
                    "Par Eden Space",
                    "Par Survivor Space",
                    "CodeHeap 'non-profiled nmethods'",
                    "CMS Old Gen"
                ]
 }
```



## reference

[https://www.elastic.co/guide/cn/elasticsearch/guide/current/_cluster_health.html](https://www.elastic.co/guide/cn/elasticsearch/guide/current/_cluster_health.html)

