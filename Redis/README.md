
### 1、Redis 是什么？

1. 是一个完全开源免费的 key-value 内存数据库 
2. 通常被认为是一个数据结构服务器，主要是因为其有着丰富的数据结构 strings、hash、list、sets、sorted sets

通常局限点来说，Redis也以消息队列的形式存在，作为内嵌的List存在，满足实时的高并发需求。在使用缓存的时候，redis比memcached具有更多的优势，并且支持更多的数据类型，把redis当作一个中间存储系统，用来处理高并发的数据库操作。

- 速度快：使用标准C写，所有数据都在内存中完成，读写速度分别达到10万/20万 
- 持久化：对数据的更新采用Copy-on-write技术，可以异步地保存到磁盘上，主要有两种策略，一是根据时间，更新次数的快照（save 300 10 ）二是基于语句追加方式(Append-only file，aof) 
- 自动操作：对不同数据类型的操作都是自动的，很安全 
- 快速的主--从复制，官方提供了一个数据，Slave在21秒即完成了对Amazon网站10G key set的复制。 
- Sharding技术：很容易将数据分布到多个Redis实例中，数据库的扩展是个永恒的话题，在关系型数据库中，主要是以添加硬件、以分区为主要技术形式的纵向扩展解决了很多的应用场景，但随着web2.0、移动互联网、云计算等应用的兴起，这种扩展模式已经不太适合了，所以近年来，像采用主从配置、数据库复制形式的，Sharding这种技术把负载分布到多个特定节点上去的横向扩展方式用处越来越多。

### 2、Redis 缺点

- 是数据库容量受到物理内存的限制,不能用作海量数据的高性能读写,因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。
- Redis较难支持在线扩容，在集群容量达到上限时在线扩容会变得很复杂。为避免这一问题，运维人员在系统上线时必须确保有足够的空间，这对资源造成了很大的浪费。
  
### 3、Redis宕机怎么解决？

宕机:服务器停止服务

如果只有一台redis，肯定会造成数据丢失，无法挽救

多台redis或者是redis集群，宕机则需要分为在主从模式下区分来看：

slave从redis宕机，配置主从复制的时候才配置从的redis，从的会从主的redis中读取主的redis的操作日志，在redis中从库重新启动后会自动加入到主从架构中，自动完成同步数据;

如果从数据库实现了持久化，此时千万不要立马重启服务，否则可能会造成数据丢失，正确的操作如下：在slave数据上执行SLAVEOF ON ONE,来断开主从关系并把slave升级为主库，此时重新启动主数据库，执行SLAVEOF，把它设置为从库，连接到主的redis上面做主从复制，自动备份数据。

以上过程很容易配置错误，可以使用redis提供的哨兵机制来简化上面的操作。简单的方法:redis的哨兵(sentinel)的功能

### 4、redis和mecached的区别，以及使用场景

区别

1、redis和Memcache都是将数据存放在内存中，都是内存数据库。不过memcache还可以用于缓存其他东西，例如图片，视频等等

2、Redis不仅仅支持简单的k/v类型的数据，同时还提供list,set,hash等数据结构的存储

3、虚拟内存-redis当物理内存用完时，可以将一些很久没用的value交换到磁盘

4、过期策略-memcache在set时就指定，例如set key1 0 0 8，即永不过期。Redis可以通过例如expire设定，例如expire name 10

5、分布式-设定memcache集群，利用magent做一主多从，redis可以做一主多从。都可以一主一丛

6、存储数据安全-memcache挂掉后，数据没了，redis可以定期保存到磁盘(持久化)

7、灾难恢复-memcache挂掉后，数据不可恢复，redis数据丢失后可以通过aof恢复

8、Redis支持数据的备份，即master-slave模式的数据备份

9、应用场景不一样，redis除了作为NoSQL数据库使用外，还能用做消息队列，数据堆栈和数据缓存等;Memcache适合于缓存SQL语句，数据集，用户临时性数据，延迟查询数据和session等

使用场景

1、如果有持久方面的需求或对数据类型和处理有要求的应该选择redis

2、如果简单的key/value存储应该选择memcached.

### 5、Redis集群方案该怎么做?都有哪些方案?

1、redis 目前用的最多的集群方案，基本和twemproxy一致的效果，但它支持在节点数量改变情况下，旧节点数据客恢复到新hash节点

2、redis cluster3.0自带的集群，特点在于他的分布式算法不是一致性hash，而是hash槽的概念，以及自身支持节点设置从节点。具体看官方介绍

3、在业务代码层实现，起几个毫无关联的redis实例，在代码层，对key进行hash计算，然后去对应的redis实例操作数据。这种方式对hash层代码要求比较高，考虑部分包括，节点失效后的替代算法方案，数据震荡后的字典脚本恢复，实例的监控，等等

### 6、Redis回收进程是如何工作的

一个客户端运行了新的命令，添加了新的数据。

redis检查内存使用情况，如果大于maxmemory的限制，则根据设定好的策略进行回收。

一个新的命令被执行等等，所以我们不断地穿越内存限制的边界，通过不断达到边界然后不断回收回到边界以下。

如果一个命令的结果导致大量内存被使用(例如很大的集合的交集保存到一个新的键)，不用多久内存限制就会被这个内存使用量超越。

### 7、Redis 跟 MySQL 缓存一致性

https://zhuanlan.zhihu.com/p/59167071

### 8、Redis 的几个基本数据类型，底层实现

https://zhuanlan.zhihu.com/p/344918922

### 9、Redis 为什么那么快

- https://zhuanlan.zhihu.com/p/160157573
- https://xie.infoq.cn/article/b3816e9fe3ac77684b4f29348

### 10、Redis 中常见集群部署情况，出现性能问题如何排查。

https://mp.weixin.qq.com/s/q79ji-cgfUMo7H0p254QRg

### 11、Redis 中的事务。

https://mp.weixin.qq.com/s/Hevg_4YJT_PzVd1Z_yE1TQ

### 12、缓存雪崩、击穿、穿透

https://mp.weixin.qq.com/s/_StOUX9Nu-Bo8UpX7ThZmg

### 13、Redis 的持久化

https://mp.weixin.qq.com/s/yP2HH8840OMY4e7tKMymiA

### 14、Redis不是号称单线程也有很高的性能么？为啥还需要多线程？

https://mp.weixin.qq.com/s/SYUYvKCxsyMbdBsRrJOZqA

### 15、Redis 过期策略和内存淘汰机制

https://segmentfault.com/a/1190000023060522

### 16、Redis 分布式锁怎么用？有什么问题？

https://mp.weixin.qq.com/s/IoDPieqgY995cyyWAQrQew

### 17、Redis为什么变慢了？一文讲透如何排查Redis性能问题

https://mp.weixin.qq.com/s/Qc4t_-_pL4w8VlSoJhRDcg
