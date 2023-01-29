
### 修改数据存储目录

修改启动systemd脚本

```shell
# CentOS6 
# 因为Ubuntu默认开启了selinux机制 
OPTIONS=--graph="/data/docker" --selinux-enabled -H fd:// 
# CentOS7 
# 修改docker.service文件，使用-g参数指定存储位置 
$ vi /usr/lib/systemd/system/docker.service 
ExecStart=/usr/bin/dockerd --graph /new-path/docker 

systemctl daemon-reload
systemctl restart docker

# Ubuntu 
# 因为Ubuntu默认没开启selinux机制 OPTIONS=--graph="/data/docker" -H fd://
```


修改配置文件

```shell
vim /etc/docker/daemon.json

{

  "registry-mirrors" : [

    "[http://ovfftd6p.mirror.aliyuncs.com](http://ovfftd6p.mirror.aliyuncs.com/)",

    "[http://registry.docker-cn.com](http://registry.docker-cn.com/)",

    "[http://docker.mirrors.ustc.edu.cn](http://docker.mirrors.ustc.edu.cn/)",

    "[http://hub-mirror.c.163.com](http://hub-mirror.c.163.com/)"

  ],

  "insecure-registries" : [

    "[registry.docker-cn.com](http://registry.docker-cn.com/)",

    "[docker.mirrors.ustc.edu.cn](http://docker.mirrors.ustc.edu.cn/)"

  ],

  "debug" : true,
  "graph": "/new-path/docker",
  "experimental" : true

}
```