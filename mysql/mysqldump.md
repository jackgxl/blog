# mysqldump 全备排除表

## 全备份库排除部分表
```shell
/usr/local/mysql3306/bin/mysqldump -uroot -pxxxxxx -x --hex-blob  --default-character-set=utf8mb4 --databases   t --ignore-table=t.a --ignore-table=t.b > tnb.sql
```



