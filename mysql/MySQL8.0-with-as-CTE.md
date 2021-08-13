# MySQL8.0-with-as-CTE

## 非递归CTE(common table express)

1. 派生表(子查询subquery)

```sql
WITH
  cte1 AS (SELECT a, b FROM table1),
  cte2 AS (SELECT c, d FROM table2)
SELECT b, d FROM cte1 JOIN cte2
WHERE cte1.a = cte2.c;
```

2. CTE

```
WITH cte (col1, col2) AS
(
  SELECT 1, 2
  UNION ALL
  SELECT 3, 4
)
SELECT col1, col2 FROM cte;

```

3. CTE引用其他CTE

```
WITH cte1 AS (SELECT 1)
SELECT * FROM (WITH cte2 AS (SELECT 2) SELECT * FROM cte2 JOIN cte1) AS dt;
```

## 递归CTE

```sql
with recursive d(n) as 
( select 1 union all select n+1 from d where n < 5  ) 
select * from d;
```



## reference 

[csdn](https://blog.csdn.net/nangy2514/article/details/98614338?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

[https://dev.mysql.com/doc/refman/8.0/en/with.html](https://dev.mysql.com/doc/refman/8.0/en/with.html)