# mydumper

# 下载

```
https://launchpad.net/mydumper/+download
wget https://launchpadlibrarian.net/225370879/mydumper-0.9.1.tar.gz
```

# 安装

```
yum install glib2-devel mysql-devel zlib-devel pcre-devel openssl-devel cmake gcc gcc-c++ -y

tar zxf mydumper-0.9.1.tar.gz 

cd mydumper-0.9.1

cmake .
make -j 12
make install
```

```
[root@mgr4 ~]# mydumper --version
mydumper 0.9.1, built against MySQL 5.5.60-MariaDB
[root@mgr4 ~]# myloader --version
myloader 0.9.1, built against MySQL 5.5.60-MariaDB
```

# 备份

* mydumper

    ```
 mydumper -t 12 -h 192.168.11.111-u 'test' -p 'test' -P 3309 -B dbname -o /backup/db
    ```

# 恢复  
  
* myloader


    ```
    myloader -h 192.168.11.100 -u test -p '123456' -P 3308 -d /backup/db -t 12 -B dbname

    ```
