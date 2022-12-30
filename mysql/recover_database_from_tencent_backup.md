# 从腾讯云备份恢复数据库到线下

## 逻辑备份恢复

```
xbstream -x < test0.xb

qpress -d cdb-jp0zua5k_backup_20191202182218.sql.qp .
```