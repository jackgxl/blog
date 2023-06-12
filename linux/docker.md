# docker


* 文件上传指令格式：

```shell
docker cp  本地路径文件  ID全称:容器路径
```

* 文件下载指令格式：

```shell
docker cp ID全称:容器文件路径 本地路径
```

**启动

```shell
docker run --name=ubuntu_rocksdb --net=host -d -ti -v /home/gaoxueliang/:/home/gaoxueliang ubuntu /bin/bash
```