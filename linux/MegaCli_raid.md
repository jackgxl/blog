# MegaCli 采集raid的基本信息


### MegaCli64 raid对应关系

```
RAID Level : Primary-1, Secondary-0, RAID Level Qualifier-0       RAID 1
RAID Level : Primary-0, Secondary-0, RAID Level Qualifier-0       RAID 0
RAID Level : Primary-5, Secondary-0, RAID Level Qualifier-3       RAID 5
RAID Level : Primary-1, Secondary-3, RAID Level Qualifier-0       RAID 10

```


### 命令使用：
```
MegaCli -LDInfo -Lall -aALL 查raid级别

MegaCli -AdpAllInfo -aALL 查raid卡信息

MegaCli -PDList -aALL 查看硬盘信息

MegaCli -AdpBbuCmd -aAll 查看电池信息

MegaCli -FwTermLog -Dsply -aALL 查看raid卡日志
MegaCli常用参数介绍

MegaCli -adpCount 【显示适配器个数】

MegaCli -AdpGetTime –aALL 【显示适配器时间】

MegaCli -AdpAllInfo -aAll 【显示所有适配器信息】

MegaCli -LDInfo -LALL -aAll 【显示所有逻辑磁盘组信息】

MegaCli -PDList -aAll 【显示所有的物理信息】

MegaCli -AdpBbuCmd -GetBbuStatus -aALL |grep ‘Charger Status’ 【查看充电状态】

MegaCli -AdpBbuCmd -GetBbuStatus -aALL【显示BBU状态信息】

MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aALL【显示BBU容量信息】

MegaCli -AdpBbuCmd -GetBbuDesignInfo -aALL 【显示BBU设计参数】

MegaCli -AdpBbuCmd -GetBbuProperties -aALL 【显示当前BBU属性】

MegaCli -cfgdsply -aALL 【显示Raid卡型号，Raid设置，Disk相关信息】
磁带状态的变化，从拔盘，到插盘的过程中。

Device |Normal|Damage|Rebuild|Normal

Virtual Drive |Optimal|Degraded|Degraded|Optimal

Physical Drive |Online|Failed –> Unconfigured|Rebuild|Online
```

### 查看rebulid的进度
```
megacli -pdrbld -showprog -physdrv [E:S] -aALL 

E = Enclosure Device ID ##megacli -PDList -aALL|grep Enclosure
S = Slot Number 磁盘编号
a0e32s11 E=32 S=11
如：megacli -pdrbld -showprog -physdrv  [32:11] -aALL
megacli -FwTermLog -Dsply -aAll|grep -i rebuild 查看磁盘rebulid进度
```