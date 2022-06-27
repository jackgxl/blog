# MongDB 备份恢复

## 使用oplog做任意点数据恢复

准备环境

​	db ：gao

​	document：test

 ```shell
k8s-node-157:8888(mongod-4.2.0)[PRIMARY:test_rep1] gao> db.test.find().limit(100)
{
  "_id": ObjectId("5d6f819b1423b672806fd186"),
  "id": 1,
  "name": "gao"
}
{
  "_id": ObjectId("5d80a0d81037f179fa844c1c"),
  "name": "Ash",
  "age": 10,
  "city": "Pallet Town"
}
{
  "_id": ObjectId("5d80a0d81037f179fa844c1d"),
  "name": "Misty",
  "age": 10,
  "city": "Cerulean City"
}
{
  "_id": ObjectId("5d80a0d81037f179fa844c1e"),
  "name": "Brock",
  "age": 15,
  "city": "Pewter City"
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3d6"),
  "a": 0
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3d7"),
  "a": 1
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3d8"),
  "a": 2
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3d9"),
  "a": 3
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3da"),
  "a": 4
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3db"),
  "a": 5
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3dc"),
  "a": 6
}
{
  "_id": ObjectId("5d81d6aff6cb104959ceb3dd"),
  "a": 7
}
k8s-node-157:8888(mongod-4.2.0)[PRIMARY:test_rep1] gao> db.test.find().count()
100004
k8s-node-157:8888(mongod-4.2.0)[PRIMARY:test_rep1] gao> db.test.find().count()
100004

 ```

开始备份数据同时写入数据

备份

```shell
[root@artron_local_160 backup]# /usr/local/mongo/bin/mongodump --host=192.168.64.157 --port=8888 --oplog -v --out=test_bak
2019-09-18T16:06:43.686+0800    writing admin.system.version to 
2019-09-18T16:06:43.688+0800    done dumping admin.system.version (1 document)
2019-09-18T16:06:43.689+0800    getting most recent oplog timestamp
2019-09-18T16:06:43.693+0800    dumping up to 4 collections in parallel
2019-09-18T16:06:43.707+0800    writing gao.test to 
2019-09-18T16:06:43.707+0800    writing artplusclick.artplus_click_works_week_data to 
2019-09-18T16:06:43.707+0800    writing artplusclick.artplus_click_works_day_data to 
2019-09-18T16:06:43.708+0800    writing artplusclick.artplus_click_works_province_data to 
2019-09-18T16:06:43.943+0800    done dumping artplusclick.artplus_click_works_province_data (14261 documents)
2019-09-18T16:06:43.943+0800    writing artplusclick.artplus_click_works_month_data to 
2019-09-18T16:06:44.063+0800    done dumping artplusclick.artplus_click_works_week_data (23065 documents)
2019-09-18T16:06:44.063+0800    writing artplusclick.artplus_click_classcode_province_data to 
2019-09-18T16:06:44.157+0800    done dumping artplusclick.artplus_click_works_month_data (12964 documents)
2019-09-18T16:06:44.157+0800    writing artplusclick.artplus_click_classcode_day_data to 
2019-09-18T16:06:44.235+0800    done dumping artplusclick.artplus_click_classcode_province_data (12576 documents)
2019-09-18T16:06:44.235+0800    writing artplusclick.artplus_click_classcode_week_data to 
2019-09-18T16:06:44.299+0800    done dumping artplusclick.artplus_click_classcode_week_data (4037 documents)
2019-09-18T16:06:44.299+0800    writing artplusclick.artplus_click_works_year_data to 
2019-09-18T16:06:44.310+0800    done dumping artplusclick.artplus_click_works_day_data (36028 documents)
2019-09-18T16:06:44.310+0800    writing artplusclick.artplus_click_works_source_data to 
2019-09-18T16:06:44.322+0800    done dumping artplusclick.artplus_click_classcode_day_data (12056 documents)
2019-09-18T16:06:44.322+0800    writing artplusclick.artplus_click_classcode_source_data to 
2019-09-18T16:06:44.338+0800    done dumping artplusclick.artplus_click_works_source_data (1529 documents)
2019-09-18T16:06:44.339+0800    writing artplusclick.artplus_click_classcode_month_data to 
2019-09-18T16:06:44.347+0800    done dumping artplusclick.artplus_click_works_year_data (2901 documents)
2019-09-18T16:06:44.347+0800    writing artplusclick.artplus_click_classcode_year_data to 
2019-09-18T16:06:44.350+0800    done dumping artplusclick.artplus_click_classcode_source_data (1491 documents)
2019-09-18T16:06:44.352+0800    done dumping artplusclick.artplus_click_classcode_year_data (237 documents)
2019-09-18T16:06:44.358+0800    done dumping artplusclick.artplus_click_classcode_month_data (1393 documents)
2019-09-18T16:06:44.586+0800    done dumping gao.test (100004 documents)
2019-09-18T16:06:44.588+0800    writing captured oplog to 
2019-09-18T16:06:44.604+0800            dumped 1 oplog entry
[root@artron_local_160 backup]# cd test_bak/
[root@artron_local_160 test_bak]# ls
admin  artplusclick  gao  oplog.bson

```



数据插入

```shell
k8s-node-157:8888(mongod-4.2.0)[PRIMARY:test_rep1] gao> for (var i = 0;i< 100000;i++) { db.test.insert({b:i}) }

Inserted 1 record(s) in 3ms
Inserted 1 record(s) in 3ms
Inserted 1 record(s) in 3ms
Inserted 1 record(s) in 3ms
WriteResult({
  "nInserted": 1
})

k8s-node-157:8888(mongod-4.2.0)[PRIMARY:test_rep1] gao> db.test.find().count()
200004
```



