

# 环境

```
[root@localhost docker_data]# cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 

yum -y update：升级所有包同时也升级软件和系统内核
yum -y upgrade：只升级所有包，不升级软件和系统内核

卸载残余文件清理
yum remove docker docker-common docker-selinux docker-engine

```


# 配置yum源

```
epel源请自行下载
rpm -ivh epel-release-latest-7.noarch.rpm 
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo （中央仓库）

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo （阿里仓库）
```

# 安装

yum安装docker-ce

```
查看可用版本有哪些
yum list docker-ce --showduplicates | sort -r

安装
sudo yum install docker-ce
sudo systemctl start docker
sudo systemctl enable docker
```

yum资源中没有docker-ce或者docker不是最新版

```
yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

```
yum provides */docker-ce

[root@local-153 ~]# yum search docker-ce

Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: mirrors.tuna.tsinghua.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
========================================================================= N/S matched: docker-ce =========================================================================
docker-ce.x86_64 : The open-source application container engine
docker-ce-cli.x86_64 : The open-source application container engine
docker-ce-selinux.noarch : SELinux Policies for the open-source application container engine

```

## yum install docker-ce 

```[root@local-153 ~]# yum install docker-ce.x86_64 docker-ce-cli.x86_64 
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: mirrors.tuna.tsinghua.edu.cn
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.huaweicloud.com
Resolving Dependencies
--> Running transaction check
---> Package docker-ce.x86_64 3:18.09.3-3.el7 will be installed
--> Processing Dependency: containerd.io >= 1.2.2-3 for package: 3:docker-ce-18.09.3-3.el7.x86_64
---> Package docker-ce-cli.x86_64 1:18.09.3-3.el7 will be installed
--> Running transaction check
---> Package containerd.io.x86_64 0:1.2.4-3.1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================
 Package                                  Arch                              Version                                     Repository                                   Size
==========================================================================================================================================================================
Installing:
 docker-ce                                x86_64                            3:18.09.3-3.el7                             docker-ce-stable                             19 M
 docker-ce-cli                            x86_64                            1:18.09.3-3.el7                             docker-ce-stable                             14 M
Installing for dependencies:
 containerd.io                            x86_64                            1.2.4-3.1.el7                               docker-ce-stable                             22 M

Transaction Summary
==========================================================================================================================================================================
Install  2 Packages (+1 Dependent package)

Total download size: 55 M
Installed size: 236 M
Is this ok [y/d/N]: y
Downloading packages:
containerd.io-1.2.4-3.1.el7.x8 FAILED                                                                                                   ]   59 B/s | 2.6 MB 259:10:55 ETA 
https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.4-3.1.el7.x86_64.rpm: [Errno 12] Timeout on https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.4-3.1.el7.x86_64.rpm: (28, 'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds')
Trying other mirror.
docker-ce-18.09.3-3.el7.x86_64 FAILED                                          
https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-18.09.3-3.el7.x86_64.rpm: [Errno 12] Timeout on https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-18.09.3-3.el7.x86_64.rpm: (28, 'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds')
Trying other mirror.
docker-ce-cli-18.09.3-3.el7.x8 FAILED                                          =-                                                       ]   19 B/s | 5.1 MB 752:47:07 ETA 
https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-cli-18.09.3-3.el7.x86_64.rpm: [Errno 12] Timeout on https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-cli-18.09.3-3.el7.x86_64.rpm: (28, 'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds')
Trying other mirror.
containerd.io-1.2.4-3.1.el7.x8 FAILED                                          =-                                                       ]   15 B/s | 5.2 MB 980:54:42 ETA 
https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.4-3.1.el7.x86_64.rpm: [Errno 12] Timeout on https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.4-3.1.el7.x86_64.rpm: (28, 'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds')
Trying other mirror.
warning: /var/cache/yum/x86_64/7/docker-ce-stable/packages/docker-ce-18.09.3-3.el7.x86_64.rpm: Header V4 RSA/SHA512 Signature, key ID 621e9f35: NOKEY 18 MB  00:00:29 ETA 
Public key for docker-ce-18.09.3-3.el7.x86_64.rpm is not installed
(1/3): docker-ce-18.09.3-3.el7.x86_64.rpm                                                                                                          |  19 MB  00:00:17     
(2/3): docker-ce-cli-18.09.3-3.el7.x86_64.rpm                                                                                                      |  14 MB  00:00:08     
(3/3): containerd.io-1.2.4-3.1.el7.x86_64.rpm                                                                                                      |  22 MB  00:00:14     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                     152 kB/s |  55 MB  00:06:09     
Retrieving key from https://download.docker.com/linux/centos/gpg
Importing GPG key 0x621E9F35:
 Userid     : "Docker Release (CE rpm) <docker@docker.com>"
 Fingerprint: 060a 61c5 1b55 8a7f 742b 77aa c52f eb6b 621e 9f35
 From       : https://download.docker.com/linux/centos/gpg
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : 1:docker-ce-cli-18.09.3-3.el7.x86_64                                                                                                                   1/3 
  Installing : containerd.io-1.2.4-3.1.el7.x86_64                                                                                                                     2/3 
  Installing : 3:docker-ce-18.09.3-3.el7.x86_64                                                                                                                       3/3 
  Verifying  : 3:docker-ce-18.09.3-3.el7.x86_64                                                                                                                       1/3 
  Verifying  : containerd.io-1.2.4-3.1.el7.x86_64                                                                                                                     2/3 
  Verifying  : 1:docker-ce-cli-18.09.3-3.el7.x86_64                                                                                                                   3/3 

Installed:
  docker-ce.x86_64 3:18.09.3-3.el7                                                  docker-ce-cli.x86_64 1:18.09.3-3.el7                                                 

Dependency Installed:
  containerd.io.x86_64 0:1.2.4-3.1.el7                                                                                                                                    

Complete!
```


查看docker状态，启动docker服务，docker启动加入服务

```
[root@local-153 ~]# system status docker
-bash: system: command not found
[root@local-153 ~]# systemctl status docker 
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: https://docs.docker.com
[root@local-153 ~]# systemctl start docker
[root@local-153 ~]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
[root@local-153 ~]# docker version
Client:
 Version:           18.09.3
 API version:       1.39
 Go version:        go1.10.8
 Git commit:        774a1f4
 Built:             Thu Feb 28 06:33:21 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.3
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.8
  Git commit:       774a1f4
  Built:            Thu Feb 28 06:02:24 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```

# 参考资料

[https://www.cnblogs.com/qgc1995/p/9553572.html](https://www.cnblogs.com/qgc1995/p/9553572.html)

[https://www.cnblogs.com/yufeng218/p/8370670.html](https://www.cnblogs.com/yufeng218/p/8370670.html)

