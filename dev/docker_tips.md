# docker tips

## error
问题

```
oot@5b5ba67010b8:/# apt-get install vim
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package vim
root@5b5ba67010b8:/# ping www.baidu.com
bash: ping: command not found
root@5b5ba67010b8:/# apt-get intall ping
E: Invalid operation intall
root@5b5ba67010b8:/# apt-get install ping
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ping
root@5b5ba67010b8:/# exit
exit
```

解决

```
$ docker attach 3aeb41c338a2
root@3aeb41c338a2:/# apt-get update
```

docker 批量停止容器
```
docker stop $(docker ps -a -q)
```

  

docker 批量删除容器

```
docker rm $(docker ps -a -q)
```

批量更新image

```
for i in `docker images |awk '{print $1}'|grep -v 'REPOSITORY'`;do docker pull $i:latest;done
```

删除none镜像

```
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
docker images | grep none | awk '{print $3}' | xargs docker rmi
```

删除所有镜像
```
docker rmi $(docker images -q -a)
```

查看数据目录

```shell
docker info | grep Dir
```


镜像大小

```
docker system df
```


docker 镜像打包上传到hub流程

```
docker pull nginx

docker run --name webserver2 -d -p 81:80 nginx

docker exec -it webserver2 bash

docker commit --author "gxl" --message "test" webserver2 nginx:v1

docker login //输入账号密码

docker tag nginx:v1 docker.artron.net/gao/nginx:v1

docker push docker.artron.net/gao/nginx:v1

docker rmi docker.artron.net/gao/nginx:v3
```

参考：

[https://blog.csdn.net/lafengwnagzi/article/details/77984616](https://blog.csdn.net/lafengwnagzi/article/details/77984616)

[https://blog.csdn.net/achilles12345/article/details/47122963](https://blog.csdn.net/achilles12345/article/details/47122963)