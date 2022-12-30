# docker tips

## error
问题

```
oot@5b5ba67010b8:/# apt-get install vim
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package vim
root@5b5ba67010b8:/# ping www.baidu.com
bash: ping: command not found
root@5b5ba67010b8:/# apt-get intall ping
E: Invalid operation intall
root@5b5ba67010b8:/# apt-get install ping
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package ping
root@5b5ba67010b8:/# exit
exit
```

解决

```
$ docker attach 3aeb41c338a2
root@3aeb41c338a2:/# apt-get update
```


参考：

[https://blog.csdn.net/lafengwnagzi/article/details/77984616](https://blog.csdn.net/lafengwnagzi/article/details/77984616)

[https://blog.csdn.net/achilles12345/article/details/47122963](https://blog.csdn.net/achilles12345/article/details/47122963)