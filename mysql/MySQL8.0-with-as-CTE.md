# MySQL8.0-with-as-CTE

## 非递归CTE

1. 派生表(子查询subquery)


2. CTE



3. CTE引用其他CTE
    
    


## 递归CTE

```sql
with recursive d(n) as ( select 1 union all select n+1 from d where n < 5  ) select * from d;
```



## reference 

[csdn](https://blog.csdn.net/nangy2514/article/details/98614338?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

