# MySQL恢复root用户超级权限

1、配置文件添加

```
skip-grant-tables
```

2、重启MySQL服务，无密码登录。手动修改用户权限。

```
update mysql.user set Grant_priv='Y',Super_priv='Y' where User='root' ;
```

3、刷新缓冲区

```
flush privileges;
```

4、授权

```
grant all on *.* to root@'localhost' with grant option;
```

5、查看用户权限

```
select * from mysql.user ;
```
