# MySQL sql\_mode  之 only\_full\_group_by 解决方案

## 问题

SQL如下：

```sql
mysql()>SELECT 
    ->     MAX(id),
    ->     news_id,
    ->     app_id,
    ->     target_id,
    ->     created_at,
    ->     status,
    ->     last_error
    -> FROM
    ->     `news_handout`
    -> WHERE
    ->     `news_handout`.`news_id` IN (450837 , 450838,
    ->         450839,
    ->         450840,
    ->         450841,
    ->         450842,
    ->         450843,
    ->         450844,
    ->         450845,
    ->         450846,
    ->         450847,
    ->         450848,
    ->         450849,
    ->         450850,
    ->         450851,
    ->         450852)
    -> GROUP BY `app_id`
    -> ORDER BY `id` DESC;
    
```
错误信息：
```
ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'cms-news.news_handout.news_id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```
sql_mode :

```
mysql()>select @@sql_mode;
+-------------------------------------------------------------------------------------------------------------------------------------------+
| @@sql_mode                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------+
| ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+-------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

## 原因

MySQL从5.7.5版本开始 sql\_mode默认加入 "ONLY\_FULL\_GROUP_BY"。
ONLY\_FULL\_GROUP\_BY是MySQL提供的一个sql\_mode，通过这个sql\_mode来提供SQL语句GROUP BY合法性的检查，在MySQL的sql\_mode是非ONLY\_FULL\_GROUP_BY语义时。一条select语句，MySQL允许target list中输出的表达式是除聚集函数或group by column以外的表达式，这个表达式的值可能在经过group by操作后变成undefined。

## 解决方案

1.修改sql\_mode(在sql\_mode中去掉only\_full\_group_by)

```
set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION '
```

2.修改配置文件

```
修改my.cnf中的sql_mode 的设置
```

3.改写SQL,加入any_value()函数

```
SELECT
	any_value(max(id)),
	any_value(news_id),
	any_value(app_id),
	any_value(target_id),
	any_value(created_at),
	any_value(STATUS),
	any_value(last_error)
FROM
	`news_handout`
WHERE
	any_value(`news_id`)IN(
		450837,
		450838,
		450839,
		450840,
		450841,
		450842,
		450843,
		450844,
		450845,
		450846,
		450847,
		450848,
		450849,
		450850,
		450851,
		450852
	)
GROUP BY
	`app_id`
ORDER BY
	any_value(`id`)DESC;

+--------------------+--------------------+-------------------+----------------------+-----------------------+-------------------+-----------------------+
| any_value(max(id)) | any_value(news_id) | any_value(app_id) | any_value(target_id) | any_value(created_at) | any_value(STATUS) | any_value(last_error) |
+--------------------+--------------------+-------------------+----------------------+-----------------------+-------------------+-----------------------+
|             441655 |             450837 |                 1 | 481750               | 2018-07-19 21:31:55   |                 1 | 导入                  |
+--------------------+--------------------+-------------------+----------------------+-----------------------+-------------------+-----------------------+
1 row in set (1.55 sec)

```

TIPs：

[ywnds](http://www.ywnds.com/?p=8184)

[https://blog.csdn.net/xuezhezhishen/article/details/78629711](https://blog.csdn.net/xuezhezhishen/article/details/78629711)

[https://www.cnblogs.com/anstoner/p/6414440.html](https://www.cnblogs.com/anstoner/p/6414440.html)