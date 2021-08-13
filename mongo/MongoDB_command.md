# MongoDB 命令

## MongoDB 查看设置


```shell
test_rep1:PRIMARY> db.serverStatus().mem
{ "bits" : 64, "resident" : 63, "virtual" : 1917, "supported" : true }
```


```shell
test_rep1:PRIMARY> db.serverStatus().connections
{ "current" : 11, "available" : 49989, "totalCreated" : 31, "active" : 2 }
```

## MongoDB 修改设置


```
use admin
test_rep1:PRIMARY> db.adminCommand({getParameter:1,wiredTigerEngineRuntimeConfig:1})
{
        "wiredTigerEngineRuntimeConfig" : "",
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1568002464, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1568002464, 1)
}
test_rep1:PRIMARY> db.adminCommand({setParameter: 1, wiredTigerEngineRuntimeConfig: "cache_size=8G"})
{
        "was" : "",
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1568002504, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1568002504, 1)
}
test_rep1:PRIMARY> db.adminCommand({getParameter:1,wiredTigerEngineRuntimeConfig:1})
{
        "wiredTigerEngineRuntimeConfig" : "cache_size=8G",
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1568002514, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1568002514, 1)
}
```

## 表迁移

```shell
db.adminCommand({renameCollection:"artplusclick.artplus_click_classcode_day_data",to:"analytics.artplus_click_classcode_day_data"}) ;

```

