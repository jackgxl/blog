# MySQL5.7 JSON索引

### 表结构
```
mysql> show create table test_json \G
*************************** 1. row ***************************
       Table: test_json
Create Table: CREATE TABLE `test_json` (
  `id` int(11) DEFAULT NULL,
  `art` json NOT NULL,
  `context` json NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
1 row in set (0.00 sec)

```
### 表数据
```
mysql> select * from test_json ;
+------+-----------------------------+----------------------------------------------------------------------+
| id   | art                         | context                                                              |
+------+-----------------------------+----------------------------------------------------------------------+
|    1 | {"age": 20, "name": "jack"} | {"text": "ffffffffffffffffff", "test2": "ggggggggggggggggggggggggg"} |
|    2 | {"age": 20, "name": "jack"} | {"text": "ffffffffffffffffff", "test2": "ggggggggggggggggggggggggg"} |
+------+-----------------------------+----------------------------------------------------------------------+
2 rows in set (0.00 sec)
```

### 创建索引
```

mysql> alter table test_json add `names_virtual` VARCHAR(20) GENERATED ALWAYS AS (art ->> '$.name') not null;
Query OK, 0 rows affected (0.18 sec)
Records: 0  Duplicates: 0  Warnings: 0


mysql> show create table test_json \G
*************************** 1. row ***************************
       Table: test_json
Create Table: CREATE TABLE `test_json` (
  `id` int(11) DEFAULT NULL,
  `art` json NOT NULL,
  `context` json NOT NULL,
  `names_virtual` varchar(20) GENERATED ALWAYS AS (json_unquote(json_extract(`art`,'$.name'))) VIRTUAL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

```


### 查询验证
```

mysql> desc select * from test_json where names_virtual="jack";
+----+-------------+-----------+------------+------+---------------+----------+---------+-------+------+----------+-------+
| id | select_type | table     | partitions | type | possible_keys | key      | key_len | ref   | rows | filtered | Extra |
+----+-------------+-----------+------------+------+---------------+----------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | test_json | NULL       | ref  | idx_name      | idx_name | 82      | const |    2 |   100.00 | NULL  |
+----+-------------+-----------+------------+------+---------------+----------+---------+-------+------+----------+-------+
1 row in set, 1 warning (0.00 sec)

mysql>  select * from test_json where names_virtual="jack";    
+------+-----------------------------+----------------------------------------------------------------------+---------------+
| id   | art                         | context                                                              | names_virtual |
+------+-----------------------------+----------------------------------------------------------------------+---------------+
|    1 | {"age": 20, "name": "jack"} | {"text": "ffffffffffffffffff", "test2": "ggggggggggggggggggggggggg"} | jack          |
|    2 | {"age": 20, "name": "jack"} | {"text": "ffffffffffffffffff", "test2": "ggggggggggggggggggggggggg"} | jack          |
+------+-----------------------------+----------------------------------------------------------------------+---------------+
2 rows in set (0.00 sec)

```