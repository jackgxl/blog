# consul

## 下载



```shell
wget https://releases.hashicorp.com/consul/1.6.2/consul_1.6.2_linux_amd64.zip
```
## 解压

```shell
tar zxf consul_1.6.2_linux_amd64.zip
mkdir -pv /data/consul/{conf,data,logs}
mv consul_1.6.2_linux_amd64/consul /usr/local/bin
```

## 启动

参数意义：

>consul -h
>Usage: consul [--version] [--help] <command> [<args>]
>
>Available commands are:
>    acl            Interact with Consul's ACLs
>    agent          Runs a Consul agent
>    catalog        Interact with the catalog
>    config         Interact with Consul's Centralized Configurations
>    connect        Interact with Consul Connect
>    debug          Records a debugging archive for operators
>    event          Fire a new event
>    exec           Executes a command on Consul nodes
>    force-leave    Forces a member of the cluster to enter the "left" state
>    info           Provides debugging information for operators.
>    intention      Interact with Connect service intentions
>    join           Tell Consul agent to join cluster
>    keygen         Generates a new encryption key
>    keyring        Manages gossip layer encryption keys
>    kv             Interact with the key-value store
>    leave          Gracefully leaves the Consul cluster and shuts down
>    lock           Execute a command holding a lock
>    login          Login to Consul using an auth method
>    logout         Destroy a Consul token created with login
>    maint          Controls node or service maintenance mode
>    members        Lists the members of a Consul cluster
>    monitor        Stream logs from a Consul agent
>    operator       Provides cluster-level tools for Consul operators
>    reload         Triggers the agent to reload configuration files
>    rtt            Estimates network round trip time between nodes
>    services       Interact with services
>    snapshot       Saves, restores and inspects snapshots of Consul server state
>    tls            Builtin helpers for creating CAs and certificates
>    validate       Validate config files/directories
>    version        Prints the Consul version
>    watch          Watch for changes in Consul


### config

```
{
    "data_dir": "/data/consul",
    "datacenter": "dc1",
    "log_level": "INFO",
    "server": true,
    "bootstrap_expect": 3,
    "bind_addr": "192.168.64.182",
    "client_addr": "0.0.0.0",
    "ui":true
    "log-file": "/data/consul/consul.log"
    "log-rotate-bytes": 102400 
}
```

### 	*server*

```shell
consul agent -server -bootstrap-expect=2 -data-dir=/data/consul/data/ -node=consul-03.artron.net -bind=192.168.22.185 --config-dir=/data/consul/conf/ -client=0.0.0.0 -ui -dns-port=8600 -datacenter=dc1 -rejoin
```

###	*client*

```shell
consul agent --server=false --client=0.0.0.0 --join 192.168.22.185 -pid-file=/data/consul/data/consul.pid -data-dir=/data/consul/data/
```



### 查看集群状态

```
consul operator raft list-peers
```




#### tips:

```
生产环境：server一般启动奇数个，最少3个
```


#### reference

[https://www.cnblogs.com/niejunlei/p/5982911.html](https://www.cnblogs.com/niejunlei/p/5982911.html)

