# Docker_Installation

# 环境

```
[root@localhost docker_data]# cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 
```

# 配置yum源

```
epel源请自行下载
rpm -ivh epel-release-latest-7.noarch.rpm 
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

# 安装

```
yum list docker-ce --showduplicates | sort -r
sudo yum install docker-ce
sudo systemctl start docker
sudo systemctl enable docker
```
# 参考资料

[https://www.cnblogs.com/yufeng218/p/8370670.html](https://www.cnblogs.com/yufeng218/p/8370670.html)