# MySQL8.0-new-feature

## 优化器

anti join

hash join

**函数索引**

reference

* [函数索引](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)

* [函数索引参考](https://www.cnblogs.com/lynn919/p/10875081.html)

CTE

* [with](https://dev.mysql.com/doc/refman/8.0/en/with.html)

windows function

[不可见索引](https://dev.mysql.com/doc/refman/8.0/en/invisible-indexes.html)

[倒序索引](https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html)

直方图

新增Multi-valued indexes

新增 Index skip scan


## 管理

新增备份锁 backup lock，避免FTWRL
快速加列
原子DDL
admin连接
在线修改undo数量
支持参数修改持久化，set persist

## 复制

json 增强
InnoDB ReplicaSet
MGR offline mode

## 插件

clone plugin
MySQL Shell

## 安全

认证插件默认为 caching_sha2_password
支持role
支持resource group
支持表空间加密

## 开发
默认字符集 utf8mb4，支持表情

## InnoDB

支持自增ID持久化
新增skip lock，no wait
新增Temp Table 引擎

## 数据字典

Information_schema的变化
mysql数据库变化
Sys schema 视图新增、变更

## 参数变化

新增参数
过期参数






