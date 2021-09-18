# 本地MySQL同步腾讯云

## tips

```shell
MySQL大版本一致
gtid 模式开启
本地同步时从库命令如下：
CHANGE MASTER TO
  MASTER_HOST='110.16.10.113',
  MASTER_USER='bak',
  MASTER_PASSWORD='bak',
  MASTER_PORT=3306 ;

SET GLOBAL gtid_purged='23d1846a-0fb4-11ec-a575-6c92bf4823cd:1-172165, dcad7210-69fa-11e8-909a-f875884a392a:1-561';
CHANGE MASTER TO MASTER_AUTO_POSITION=1;
```



