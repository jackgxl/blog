# MHA_configuration

## MHA结构

|IP地址|角色|端口|
|:--:|:--:|:--:|
|192.168.64.182|Master_node|5641|
|192.168.64.101|Slave_node|5641|
|192.168.64.157|Slave_node|5641|
|192.168.64.160|MHA_Master||


## SSH 互信


每台HOST上都要执行

```shell
ssh-keygen -t RSA
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.182'
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.157'
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.101'
```

mha需要调用mysqlbinlog命令，编译安装的MySQl需要做软连接

```
ln -sv /data/mysql5641/bin/mysqlbinlog /usr/local/bin/mysqlbinlog
```


## 配置MHA_Manage


**ssh check**

```
[root@localhost masterha]# masterha_check_ssh --conf=app1.cnf 
Fri Sep 14 14:47:10 2018 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.
Fri Sep 14 14:47:10 2018 - [info] Reading application default configuration from app1.cnf..
Fri Sep 14 14:47:10 2018 - [info] Reading server configuration from app1.cnf..
Fri Sep 14 14:47:10 2018 - [info] Starting SSH connection tests..
Fri Sep 14 14:47:11 2018 - [debug] 
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.157(192.168.64.157:22)..
Fri Sep 14 14:47:10 2018 - [debug]   ok.
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.101(192.168.64.101:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug] 
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.182(192.168.64.182:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.101(192.168.64.101:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:12 2018 - [debug] 
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.182(192.168.64.182:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.157(192.168.64.157:22)..
Fri Sep 14 14:47:12 2018 - [debug]   ok.
Fri Sep 14 14:47:12 2018 - [info] All SSH connection tests passed successfully.
```

**slave check**

```

```


##

