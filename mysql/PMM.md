# <center>Percona Monitoring and Management </center>
# <center>(PMM)</center>

[toc]

## 环境配置

```
cat /etc/redhat-release 
CentOS Linux release 7.3.1611 (Core)
```

## docker安装

```
yum install docker -y

systemctl start docker.service
systemctl status docker

```

## PMM安装

* 拉取docker镜像

    ```
    docker pull percona/pmm-server:latest
    [root@localhost data]# docker images;
    REPOSITORY          TAG                 IMAGE ID        CREATED             SIZE
    [root@localhost data]# docker images
    REPOSITORY          TAG                 IMAGE ID        CREATED             SIZE
    [root@localhost data]# docker ps
    CONTAINER ID        IMAGE               COMMAND         
    CREATED             STATUS              PORTS               NAMES
    [root@localhost data]# docker pull percona/pmm-server:latest
    latest: Pulling from percona/pmm-server
    aeb7866da422: Pull complete 
    cc3feb415dc3: Pull complete 
    Digest: sha256:92092866dcfaabd6aac4d2754a4094967ea42864faf2434811232181a9f755dc
    Status: Downloaded newer image for percona/pmm-server:latest
    [root@localhost data]# 
    ```


##  PMM server 创建启动

* 创建
   
```
[root@localhost data]# docker images
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
percona/pmm-server   latest              2ff436aaddc9        5 days ago          1.01GB
[root@localhost data]# docker create \
>    -v /opt/prometheus/data \
>    -v /opt/consul-data \
>    -v /var/lib/mysql \
>    -v /var/lib/grafana \
>    --name pmm-data \
>    percona/pmm-server:latest /bin/true
7c3ad76fe1203463b89065b2cf1bc51953fa621057a4ac8e55487f97a65e720f
```

* 启动
    
```
[root@localhost data]# docker run -d -p 80:80 \
>   --volumes-from pmm-data \
>   --name pmm-server \
>   -e SERVER_USER=test \
>   -e SERVER_PASSWORD=test \
>   --restart always \
>   percona/pmm-server:latest
4f89c180a56e4054ee5e6248731ef2c65de79be0a8863eda467145463d603afe
[root@localhost data]# docker ps
CONTAINER ID        IMAGE                       COMMAND                CREATED             STATUS              PORTS                         NAMES
4f89c180a56e        percona/pmm-server:latest   "/opt/entrypoint.sh"   7 seconds ago       Up 6 seconds        0.0.0.0:80->80/tcp, 443/tcp   pmm-server
[root@localhost data]# 
```

* PMM server 启用Orchestrator

```
        [root@localhost data]# docker ps
CONTAINER ID        IMAGE                       COMMAND                CREATED             STATUS              PORTS                         NAMES
4f89c180a56e        percona/pmm-server:latest   "/opt/entrypoint.sh"   7 seconds ago       Up 6 seconds        0.0.0.0:80->80/tcp, 443/tcp   pmm-server
[root@localhost data]# docker stop 4f89c180a56e
4f89c180a56e
[root@localhost data]# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
[root@localhost data]# 
```
        

```
docker run -d -p 80:80 \
  --volumes-from pmm-data \
  --name pmm-server \
  -e SERVER_USER=$user \
  -e SERVER_PASSWORD=$passwd \
  -e ORCHESTRATOR_ENABLED=true \
  --restart always \
  percona/pmm-server:latest
```


## PMM agent 安装启动

```
yum install -y pmm-client-1.17.0-1.el7.x86_64.rpm 
pmm-admin config --server 192.168.64.101 --server-user $user --server-password $paswd
pmm-admin add mysql --user $user --password $passwd  --socket /path/to/mysql.sock alias_name
```


### PMM agent 关闭

```
pmm-admin stop --all

```

### PMM 删除

```shell
# killall containers
docker_kill(){
    if [ -n "`docker ps -a -q`" ]; then
        docker stop `docker ps -a -q`
    fi
    if [ -n "`docker ps -a -q`" ]; then
        docker rm `docker ps -a -q`
    fi
}

```



## references

[https://segmentfault.com/a/1190000012030650](https://segmentfault.com/a/1190000012030650)

