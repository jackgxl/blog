# MariaDB\_Spider\_Installation\_Using

# Installation

* 下载MariaDB

```
wget https://downloads.mariadb.com/MariaDB/mariadb-10.3.10/mariadb-10.3.10-linux-glibc_214-x86_64.tar.gz
```

* 解压安装包安装spider插件

```shell
tar zxf mariadb-10.3.10-linux-x86_64.tar.gz -C /usr/local
cd /usr/local
ln -sv mariadb-10.3.10-linux-x86_64 mysql
mkdir -pv /data/mysqldata/
配置my.cnf
cd /usr/local/mysql
./scripts/mysql_install_db --defaults-file=/path/to/my.cnf --user=mysql

cd /usr/local/mysql/share

MariaDB [(none)]> source ./install_spider.sql
```
```
Spider 插件安装验证

MariaDB [mysql]> show tables like '%spider%';
+------------------------------------+
| Tables_in_mysql (%spider%)         |
+------------------------------------+
| spider_link_failed_log             |
| spider_link_mon_servers            |
| spider_table_crd                   |
| spider_table_position_for_recovery |
| spider_table_sts                   |
| spider_tables                      |
| spider_xa                          |
| spider_xa_failed_log               |
| spider_xa_member                   |
+------------------------------------+
9 rows in set (0.001 sec)
```

# Spride 配置



# 

# References

[https://mariadb.com/kb/en/library/spider-storage-engine-overview/](https://mariadb.com/kb/en/library/spider-storage-engine-overview/)

[https://www.jianshu.com/p/b96a8c90689a](https://www.jianshu.com/p/b96a8c90689a)

[https://zhuanlan.zhihu.com/p/47418626?utm_source=qq&utm_medium=social&utm_oi=72613187551232]()

[https://www.centos.bz/2017/12/mariadb-galera-cluster%E9%9B%86%E7%BE%A4%E4%BC%98%E7%BC%BA%E7%82%B9/](https://www.centos.bz/2017/12/mariadb-galera-cluster%E9%9B%86%E7%BE%A4%E4%BC%98%E7%BC%BA%E7%82%B9/)