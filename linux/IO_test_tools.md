# 磁盘速度测试工具

[TOC]

## Linux tools

```shell
nethogs:按进程查案流量占用
iptraf：按连接/端口查看流量
ifstat：按设备查看流量
ethtool：诊断工具
tcpdump：抓包工具
pstack :    gdb调试
ss：连接查看工具
其他：dstat  slurm  nload  bmon nc
sar -n DEV 1 4
sar -n tcp,etcp 1
load -u K

监控总体带宽使用――nload、bmon、slurm、bwm-ng、cbm、speedometer和netload
监控总体带宽使用（批量式输出）――vnstat、ifstat、dstat和collectl
每个套接字连接的带宽使用――iftop、iptraf、tcptrack、pktstat、netwatch和trafshow
每个进程的带宽使用――nethogs
```



## hdpam

*   安装

```
yum install -y hdpam
```
* 参数

    ```shell
    -a<快取分区>：设定读取文件时，预先存入块区的分区数，若不加上<快取分区>选项，则显示目前的设定；
    -A<0或1>：启动或关闭读取文件时的快取功能；
    -c<I/O模式>：设定IDE32位I/O模式；
    -C：检测IDE硬盘的电源管理模式；
    -d<0或1>：设定磁盘的DMA模式；
    -f：将内存缓冲区的数据写入硬盘，并清楚缓冲区；
    -g：显示硬盘的磁轨，磁头，磁区等参数；
    -h：显示帮助；
    -i：显示硬盘的硬件规格信息，这些信息是在开机时由硬盘本身所提供；
    -I：直接读取硬盘所提供的硬件规格信息；
    -k<0或1>：重设硬盘时，保留-dmu参数的设定；
    -K<0或1>：重设硬盘时，保留-APSWXZ参数的设定；
    -m<磁区数>：设定硬盘多重分区存取的分区数；
    -n<0或1>：忽略硬盘写入时所发生的错误；
    -p<PIO模式>：设定硬盘的PIO模式；
    -P<磁区数>：设定硬盘内部快取的分区数；
    -q:在执行后续的参数时，不在屏幕上显示任何信息；
    -r<0或1>:设定硬盘的读写模式；
    -S<时间>:设定硬盘进入省电模式前的等待时间；
    -t：评估硬盘的读取效率；
    -T：评估硬盘快取的读取效率；
    -u<0或1>：在硬盘存取时，允许其他中断要求同时执行；
    -v：显示硬盘的相关设定；
    -w<0或1>：设定硬盘的写入快取；
    -X<传输模式>：设定硬盘的传输模式；
    -y：使IDE硬盘进入省电模式；
    -Y：使IDE硬盘进入睡眠模式；
    -Z：关闭某些Seagate硬盘的自动省电功能。
    ```

    

* 测试
```
hdparm -T /dev/sda

/dev/sda:
 Timing cached reads:   10470 MB in  2.00 seconds = 5241.80 MB/sec
[root@artron_local_160 backup]# hdparm -C /dev/sda

```



## fio

```shell
wget http://brick.kernel.dk/snaps/fio-2.1.10.tar.gz
tar zxf fio-2.1.10.tar.gz 
cd fio-2.1.10
make -j 12
make install
```

*   参数说明

    ```shell
    filename=/dev/emcpowerb　支持文件系统或者裸设备，-filename=/dev/sda2或-filename=/dev/sdb
    direct=1                 测试过程绕过机器自带的buffer，使测试结果更真实
    rw=randwread             测试随机读的I/O
    rw=randwrite             测试随机写的I/O
    rw=randrw                测试随机混合写和读的I/O
    rw=read                  测试顺序读的I/O
    rw=write                 测试顺序写的I/O
    rw=rw                    测试顺序混合写和读的I/O
    bs=4k                    单次io的块文件大小为4k
    bsrange=512-2048         同上，提定数据块的大小范围
    size=5g                  本次的测试文件大小为5g，以每次4k的io进行测试
    numjobs=30               本次的测试线程为30
    runtime=1000             测试时间为1000秒，如果不写则一直将5g文件分4k每次写完为止
    ioengine=psync           io引擎使用pync方式，如果要使用libaio引擎，需要yum install libaio-devel包
    rwmixwrite=30            在混合读写的模式下，写占30%
    group_reporting          关于显示结果的，汇总每个进程的信息
    此外
    lockmem=1g               只使用1g内存进行测试
    zero_buffers             用0初始化系统buffer
    nrfiles=8                每个进程生成文件的数量
    ```

    

*   测试

    

    ```shell
    fio -filename=/data/backup/test_randread -direct=1 -iodepth 1 -thread -rw=randrw -rwmixread=70 -ioengine=psync -bs=16k -size=2G -numjobs=30 -runtime=120 -group_reporting -name=mytest        
    mytest: (g=0): rw=randrw, bs=16K-16K/16K-16K/16K-16K, ioengine=psync, iodepth=1
    ...
    fio-2.1.10
    Starting 30 threads
    mytest: Laying out IO file(s) (1 file(s) / 2048MB)
    Jobs: 30 (f=30): [mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm] [100.0% done] [10245KB/4603KB/0KB /s] [640/287/0 iops] [eta 00m:00s]
    mytest: (groupid=0, jobs=30): err= 0: pid=7421: Tue Jun 18 10:32:58 2019
      read : io=1231.7MB, bw=10504KB/s, iops=656, runt=120068msec
        clat (usec): min=66, max=259591, avg=16271.02, stdev=18910.72
         lat (usec): min=66, max=259591, avg=16271.40, stdev=18910.73
        clat percentiles (usec):
         |  1.00th=[   89],  5.00th=[ 1752], 10.00th=[ 2736], 20.00th=[ 4192],
         | 30.00th=[ 5664], 40.00th=[ 7264], 50.00th=[ 9664], 60.00th=[12864],
         | 70.00th=[17536], 80.00th=[24704], 90.00th=[37632], 95.00th=[52480],
         | 99.00th=[92672], 99.50th=[112128], 99.90th=[158720], 99.95th=[175104],
         | 99.99th=[226304]
        bw (KB  /s): min=   26, max=  926, per=3.36%, avg=353.32, stdev=138.71
      write: io=523920KB, bw=4363.6KB/s, iops=272, runt=120068msec
        clat (msec): min=2, max=609, avg=70.77, stdev=54.28
         lat (msec): min=2, max=609, avg=70.77, stdev=54.28
        clat percentiles (msec):
         |  1.00th=[   10],  5.00th=[   15], 10.00th=[   20], 20.00th=[   29],
         | 30.00th=[   37], 40.00th=[   46], 50.00th=[   57], 60.00th=[   69],
         | 70.00th=[   84], 80.00th=[  105], 90.00th=[  141], 95.00th=[  178],
         | 99.00th=[  262], 99.50th=[  302], 99.90th=[  392], 99.95th=[  441],
         | 99.99th=[  545]
        bw (KB  /s): min=   26, max=  318, per=3.34%, avg=145.83, stdev=45.57
        lat (usec) : 100=1.25%, 250=1.46%, 500=0.07%, 750=0.05%, 1000=0.03%
        lat (msec) : 2=1.38%, 4=9.00%, 10=23.17%, 20=19.15%, 50=24.14%
        lat (msec) : 100=13.36%, 250=6.57%, 500=0.35%, 750=0.01%
      cpu          : usr=0.03%, sys=0.13%, ctx=111770, majf=0, minf=9
      IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
         submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
         complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
         issued    : total=r=78825/w=32745/d=0, short=r=0/w=0/d=0
         latency   : target=0, window=0, percentile=100.00%, depth=1
    
    Run status group 0 (all jobs):
       READ: io=1231.7MB, aggrb=10504KB/s, minb=10504KB/s, maxb=10504KB/s, mint=120068msec, maxt=120068msec
      WRITE: io=523920KB, aggrb=4363KB/s, minb=4363KB/s, maxb=4363KB/s, mint=120068msec, maxt=120068msec
    
    Disk stats (read/write):
        dm-1: ios=79546/32835, merge=0/0, ticks=1867423/2496998, in_queue=4371326, util=100.00%, aggrios=79748/32885, aggrmerge=10/4, aggrticks=1925454/2497479, aggrin_queue=4422884, aggrutil=100.00%
      sda: ios=79748/32885, merge=10/4, ticks=1925454/2497479, in_queue=4422884, util=100.00%
    ```

    



## CPU 绑定

```
taskset  绑定cpu 

taskset -p -c 10  1220 //把1220 绑定到第10号cpu上
```

## lshw

```shell
yum install lshw -y
```
## mpstat

## 