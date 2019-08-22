<!-- TOC -->

- [系统编程](#%e7%b3%bb%e7%bb%9f%e7%bc%96%e7%a8%8b)
  - [1.select,poll和epoll](#1selectpoll%e5%92%8cepoll)
  - [2.调度算法](#2%e8%b0%83%e5%ba%a6%e7%ae%97%e6%b3%95)
  - [3.死锁](#3%e6%ad%bb%e9%94%81)
  - [4.程序编译与链接](#4%e7%a8%8b%e5%ba%8f%e7%bc%96%e8%af%91%e4%b8%8e%e9%93%be%e6%8e%a5)
  - [5.静态链接和动态链接](#5%e9%9d%99%e6%80%81%e9%93%be%e6%8e%a5%e5%92%8c%e5%8a%a8%e6%80%81%e9%93%be%e6%8e%a5)
  - [6.虚拟内存技术](#6%e8%99%9a%e6%8b%9f%e5%86%85%e5%ad%98%e6%8a%80%e6%9c%af)
  - [7.分页和分段](#7%e5%88%86%e9%a1%b5%e5%92%8c%e5%88%86%e6%ae%b5)
  - [8.页面置换算法](#8%e9%a1%b5%e9%9d%a2%e7%bd%ae%e6%8d%a2%e7%ae%97%e6%b3%95)
  - [9.边沿触发和水平触发](#9%e8%be%b9%e6%b2%bf%e8%a7%a6%e5%8f%91%e5%92%8c%e6%b0%b4%e5%b9%b3%e8%a7%a6%e5%8f%91)
  - [10.unix进程间通信方式(IPC)](#10unix%e8%bf%9b%e7%a8%8b%e9%97%b4%e9%80%9a%e4%bf%a1%e6%96%b9%e5%bc%8fipc)
  - [11.进程总结](#11%e8%bf%9b%e7%a8%8b%e6%80%bb%e7%bb%93)
  - [12.Python异步使用场景有那些？](#12python%e5%bc%82%e6%ad%a5%e4%bd%bf%e7%94%a8%e5%9c%ba%e6%99%af%e6%9c%89%e9%82%a3%e4%ba%9b)
  - [13.多线程共同操作同一个数据互斥锁同步？](#13%e5%a4%9a%e7%ba%bf%e7%a8%8b%e5%85%b1%e5%90%8c%e6%93%8d%e4%bd%9c%e5%90%8c%e4%b8%80%e4%b8%aa%e6%95%b0%e6%8d%ae%e4%ba%92%e6%96%a5%e9%94%81%e5%90%8c%e6%ad%a5)
  - [14.什么是多线程竞争？](#14%e4%bb%80%e4%b9%88%e6%98%af%e5%a4%9a%e7%ba%bf%e7%a8%8b%e7%ab%9e%e4%ba%89)
  - [15.请介绍一下Python的线程同步？](#15%e8%af%b7%e4%bb%8b%e7%bb%8d%e4%b8%80%e4%b8%8bpython%e7%9a%84%e7%ba%bf%e7%a8%8b%e5%90%8c%e6%ad%a5)
  - [16.解释以下什么是锁，有哪几种锁？](#16%e8%a7%a3%e9%87%8a%e4%bb%a5%e4%b8%8b%e4%bb%80%e4%b9%88%e6%98%af%e9%94%81%e6%9c%89%e5%93%aa%e5%87%a0%e7%a7%8d%e9%94%81)
  - [17.什么是死锁？](#17%e4%bb%80%e4%b9%88%e6%98%af%e6%ad%bb%e9%94%81)
  - [18.多线程交互访问数据，如果访问到了就不访问了？](#18%e5%a4%9a%e7%ba%bf%e7%a8%8b%e4%ba%a4%e4%ba%92%e8%ae%bf%e9%97%ae%e6%95%b0%e6%8d%ae%e5%a6%82%e6%9e%9c%e8%ae%bf%e9%97%ae%e5%88%b0%e4%ba%86%e5%b0%b1%e4%b8%8d%e8%ae%bf%e9%97%ae%e4%ba%86)
  - [19.什么是线程安全，什么是互斥锁？](#19%e4%bb%80%e4%b9%88%e6%98%af%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e4%bb%80%e4%b9%88%e6%98%af%e4%ba%92%e6%96%a5%e9%94%81)
  - [20.说说下面几个概念：同步，异步，阻塞，非阻塞？](#20%e8%af%b4%e8%af%b4%e4%b8%8b%e9%9d%a2%e5%87%a0%e4%b8%aa%e6%a6%82%e5%bf%b5%e5%90%8c%e6%ad%a5%e5%bc%82%e6%ad%a5%e9%98%bb%e5%a1%9e%e9%9d%9e%e9%98%bb%e5%a1%9e)
  - [21.什么是僵尸进程和孤儿进程？怎么避免僵尸进程？](#21%e4%bb%80%e4%b9%88%e6%98%af%e5%83%b5%e5%b0%b8%e8%bf%9b%e7%a8%8b%e5%92%8c%e5%ad%a4%e5%84%bf%e8%bf%9b%e7%a8%8b%e6%80%8e%e4%b9%88%e9%81%bf%e5%85%8d%e5%83%b5%e5%b0%b8%e8%bf%9b%e7%a8%8b)
  - [22.python中进程与线程的使用场景？](#22python%e4%b8%ad%e8%bf%9b%e7%a8%8b%e4%b8%8e%e7%ba%bf%e7%a8%8b%e7%9a%84%e4%bd%bf%e7%94%a8%e5%9c%ba%e6%99%af)
  - [23.线程是并发还是并行，进程是并发还是并行？](#23%e7%ba%bf%e7%a8%8b%e6%98%af%e5%b9%b6%e5%8f%91%e8%bf%98%e6%98%af%e5%b9%b6%e8%a1%8c%e8%bf%9b%e7%a8%8b%e6%98%af%e5%b9%b6%e5%8f%91%e8%bf%98%e6%98%af%e5%b9%b6%e8%a1%8c)
  - [24.并行（parallel）和并发（concurrency）?](#24%e5%b9%b6%e8%a1%8cparallel%e5%92%8c%e5%b9%b6%e5%8f%91concurrency)
  - [25.IO密集型和CPU密集型区别？](#25io%e5%af%86%e9%9b%86%e5%9e%8b%e5%92%8ccpu%e5%af%86%e9%9b%86%e5%9e%8b%e5%8c%ba%e5%88%ab)
  - [26.python asyncio的原理？](#26python-asyncio%e7%9a%84%e5%8e%9f%e7%90%86)
  - [27.谈谈你对多进程，多线程，以及协程的理解，项目是否用？](#27%e8%b0%88%e8%b0%88%e4%bd%a0%e5%af%b9%e5%a4%9a%e8%bf%9b%e7%a8%8b%e5%a4%9a%e7%ba%bf%e7%a8%8b%e4%bb%a5%e5%8f%8a%e5%8d%8f%e7%a8%8b%e7%9a%84%e7%90%86%e8%a7%a3%e9%a1%b9%e7%9b%ae%e6%98%af%e5%90%a6%e7%94%a8)

<!-- /TOC -->

## 系统编程

### 1.select,poll和epoll

其实所有的I/O都是轮询的方法，只不过实现的层面不同罢了。

这个问题可能有点深入了，但相信能回答出这个问题是对I/O多路复用有很好的了解了，其中tornado使用的就是 epoll。

[selec,poll和epoll区别总结](http://www.cnblogs.com/Anker/p/3265058.html)

基本上select有3个缺点:

1. 连接数受限
2. 查找配对速度慢
3. 数据由内核拷贝到用户态

poll改善了第一个缺点，epoll改了三个缺点。

关于epoll的: http://www.cnblogs.com/my_life/articles/3968782.html

### 2.调度算法

1. 先来先服务(FCFS, First Come First Serve)
2. 短作业优先(SJF, Shortest Job First)
3. 最高优先权调度(Priority Scheduling)
4. 时间片轮转(RR, Round Robin)
5. 多级反馈队列调度(multilevel feedback queue scheduling)

常见的调度算法总结:http://www.jianshu.com/p/6edf8174c1eb

实时调度算法:

1. 最早截至时间优先 EDF
2. 最低松弛度优先 LLF

### 3.死锁

原因:

1. 竞争资源
2. 程序推进顺序不当

必要条件:

1. 互斥条件
2. 请求和保持条件
3. 不剥夺条件
4. 环路等待条件

处理死锁基本方法:

1. 预防死锁(摒弃除1以外的条件)
2. 避免死锁(银行家算法)
3. 检测死锁(资源分配图)
4. 解除死锁
   1. 剥夺资源
   2. 撤销进程

死锁概念处理策略详细介绍:https://wizardforcel.gitbooks.io/wangdaokaoyan-os/content/10.html

### 4.程序编译与链接

推荐: http://www.ruanyifeng.com/blog/2014/11/compiler.html

Bulid过程可以分解为4个步骤:预处理(Prepressing), 编译(Compilation)、汇编(Assembly)、链接(Linking)

以c语言为例:

1、预处理

预编译过程主要处理那些源文件中的以“#”开始的预编译指令，主要处理规则有：

1. 将所有的“#define”删除，并展开所用的宏定义
2. 处理所有条件预编译指令，比如“#if”、“#ifdef”、 “#elif”、“#endif”
3. 处理“#include”预编译指令，将被包含的文件插入到该编译指令的位置，注：此过程是递归进行的
4. 删除所有注释
5. 添加行号和文件名标识，以便于编译时编译器产生调试用的行号信息以及用于编译时产生编译错误或警告时可显示行号
6. 保留所有的#pragma编译器指令。

2、编译

编译过程就是把预处理完的文件进行一系列的词法分析、语法分析、语义分析及优化后生成相应的汇编代码文件。这个过程是整个程序构建的核心部分。

3、汇编

汇编器是将汇编代码转化成机器可以执行的指令，每一条汇编语句几乎都是一条机器指令。经过编译、链接、汇编输出的文件成为目标文件(Object File)

4、链接

链接的主要内容就是把各个模块之间相互引用的部分处理好，使各个模块可以正确的拼接。主要过程包块地址和空间的分配（Address and Storage Allocation）、符号决议(Symbol Resolution)和重定位(Relocation)等步骤。

### 5.静态链接和动态链接

静态链接方法：静态链接的时候，载入代码就会把程序会用到的动态代码或动态代码的地址确定下来。静态库的链接可以使用静态链接，动态链接库也可以使用这种方法链接导入库。

动态链接方法：使用这种方式的程序并不在一开始就完成动态链接，而是直到真正调用动态库代码时，载入程序才计算(被调用的那部分)动态代码的逻辑地址，然后等到某个时候，程序又需要调用另外某块动态代码时，载入程序又去计算这部分代码的逻辑地址，所以，这种方式使程序初始化时间较短，但运行期间的性能比不上静态链接的程序。

### 6.虚拟内存技术

虚拟存储器是指具有请求调入功能和置换功能，能从逻辑上对内存容量加以扩充的一种存储系统.

### 7.分页和分段

分页: 用户程序的地址空间被划分成若干固定大小的区域，称为“页”，相应地，内存空间分成若干个物理块，页和块的大小相等。可将用户程序的任一页放在内存的任一块中，实现了离散分配。

分段: 将用户程序地址空间分成若干个大小不等的段，每段可以定义一组相对完整的逻辑信息。存储分配时，以段为单位，段与段在内存中可以不相邻接，也实现了离散分配。

分页与分段的主要区别：

1. 页是信息的物理单位,分页是为了实现非连续分配,以便解决内存碎片问题,或者说分页是由于系统管理的需要.段是信息的逻辑单位,它含有一组意义相对完整的信息,分段的目的是为了更好地实现共享,满足用户的需要.
2. 页的大小固定,由系统确定,将逻辑地址划分为页号和页内地址是由机器硬件实现的.而段的长度却不固定,决定于用户所编写的程序,通常由编译程序在对源程序进行编译时根据信息的性质来划分.
3. 分页的作业地址空间是一维的.分段的地址空间是二维的.

### 8.页面置换算法

1. 最佳置换算法OPT:不可能实现
2. 先进先出FIFO
3. 最近最久未使用算法LRU:最近一段时间里最久没有使用过的页面予以置换.
4. clock算法

### 9.边沿触发和水平触发

边缘触发是指每当状态变化时发生一个 io 事件，条件触发是只要满足条件就发生一个 io 事件。

### 10.unix进程间通信方式(IPC)

1. 管道（Pipe）：管道可用于具有亲缘关系进程间的通信，允许一个进程和另一个与它有共同祖先的进程之间进行通信。
2. 命名管道（named pipe）：命名管道克服了管道没有名字的限制，因此，除具有管道所具有的功能外，它还允许无亲缘关系进程间的通信。命名管道在文件系统中有对应的文件名。命名管道通过命令mkfifo或系统调用mkfifo来创建。
3. 信号（Signal）：信号是比较复杂的通信方式，用于通知接受进程有某种事件发生，除了用于进程间通信外，进程还可以发送信号给进程本身；linux除了支持Unix早期信号语义函数sigal外，还支持语义符合Posix.1标准的信号函数sigaction（实际上，该函数是基于BSD的，BSD为了实现可靠信号机制，又能够统一对外接口，用sigaction函数重新实现了signal函数）。
4. 消息（Message）队列：消息队列是消息的链接表，包括Posix消息队列system V消息队列。有足够权限的进程可以向队列中添加消息，被赋予读权限的进程则可以读走队列中的消息。消息队列克服了信号承载信息量少，管道只能承载无格式字节流以及缓冲区大小受限等缺
5. 共享内存：使得多个进程可以访问同一块内存空间，是最快的可用IPC形式。是针对其他通信机制运行效率较低而设计的。往往与其它通信机制，如信号量结合使用，来达到进程间的同步及互斥。
6. 内存映射（mapped memory）：内存映射允许任何多个进程间通信，每一个使用该机制的进程通过把一个共享的文件映射到自己的进程地址空间来实现它。
7. 信号量（semaphore）：主要作为进程间以及同一进程不同线程之间的同步手段。
8. 套接口（Socket）：更为一般的进程间通信机制，可用于不同机器之间的进程间通信。起初是由Unix系统的BSD分支开发出来的，但现在一般可以移植到其它类Unix系统上：Linux和System V的变种都支持套接字。

### 11.进程总结

进程：程序运行在操作系统上的一个实例，就称之为进程。进程需要相应的系统资源：内存、时间片、pid。

创建进程：

首先要导入 multiprocessing 中的 Process，然后创建一个 Process 对象，创建 Process 对象时，可以传递参数：

```python
p = Process(target=XXX, args=(tuple,), kwargs={key: value})
# target = XXX 指定的任务函数，不用加(),
# args=(tuple,)kwargs={key:value}给任务函数传递的参数
```

使用start()启动进程：

```python
import os
import time
from mulitprocessing import Process


def pro_func(name, age, **kwargs):
    for i in range(5):
        print("子进程正在运行中，name=%s,age=%d,pid=%d"%(name,age,os.getpid()))
        print(kwargs)
        time.sleep(0.2)

if __name__ =="__main__":
    #创建Process对象
    p = Process(target=pro_func,args=('小明',18),kwargs={'m':20})
    #启动进程
    p.start()
    time.sleep(1)
    #1秒钟之后，立刻结束子进程
    p.terminate()
    p.join()
```

注意：进程间不共享全局变量。

进程之间的通信-Queue

在初始化Queue()对象时（例如q=Queue(),若在括号中没有指定最大可接受的消息数量，获数量为负值时，那么就代表可接受的消息数量没有上限一直到内存尽头）

Queue.qsize():返回当前队列包含的消息数量

Queue.empty():如果队列为空，返回True，反之False

Queue.full():如果队列满了，返回True,反之False

Queue.get([block[,timeout]]):获取队列中的一条消息，然后将其从队列中移除

block默认值为True。

如果block使用默认值，且没有设置timeout（单位秒)，消息队列如果为空，此时程序将被阻塞（停在读中状态），直到消息队列读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出“Queue.Empty"异常：

Queue.get_nowait()相当于Queue.get(False)

Queue.put(item,[block[,timeout]]):将item消息写入队列，block默认值为True;

如果block使用默认值，且没有设置timeout（单位秒），消息队列如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息队列腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出”Queue.Full"异常；如果block值为False，消息队列如果没有空间可写入，则会立刻抛出"Queue.Full"异常;

Queue.put_nowait(item):相当Queue.put(item,False)

进程间通信Demo:

```python
import os
import time
import random
from multiprocessing import Process.Queue

#写数据进程执行的代码：
def write(q):
    for value in ['A','B','C']:
        print("Put %s to queue...",%value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue.",%value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw ，写入：
    pw.start()
    #等待pw结束
    pw.join()
    #启动子进程pr，读取：
    pr.start()
    pr.join()
    #pr 进程里是死循环，无法等待其结束，只能强行终止:
    print('')
    print('所有数据都写入并且读完')
```

进程池Pool

```python
#coding:utf-8

import os
import time
import random
from multiprocessing import Pool

def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为%d"%(msg,os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f”%（t_stop-t_start))

po = Pool(3)#定义一个进程池，最大进程数3
for i in range(0,10):
    po.apply_async(worker,(i,))

print("---start----")
po.close()
po.join()
print("----end----")
```

进程池中使用Queue

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，否则会得到如下的错误信息：

RuntimeError： Queue objects should only be shared between processs through inheritance

```python
import os
import time
import random
from multiprocessing import Manager, Pool

def reader(q):
    print("reader 启动(%s),父进程为（%s)"%(os.getpid(),os.getpid()))
    for i in range(q.qsize()):
        print("reader 从Queue获取到消息:%s"%q.get(True))

def writer(q):
    print("writer 启动（%s),父进程为(%s)"%(os.getpid(),os.getpid()))
    for i ini "itcast":
        q.put(i)
        
if __name__ == "__main__":
    print("(%s)start"%os.getpid())
    q = Manager().Queue()#使用Manager中的Queue
    po = Pool()
    po.apply_async(wrtier,(q,))
    time.sleep(1)
    po.apply_async(reader,(q,))
    po.close()
    po.join()
    print("(%s)End"%os.getpid())
```

### 12.Python异步使用场景有那些？

异步的使用场景:

1、 不涉及共享资源，获对共享资源只读，即非互斥操作

2、 没有时序上的严格关系

3、 不需要原子操作，或可以通过其他方式控制原子性

4、 常用于IO操作等耗时操作，因为比较影响客户体验和使用性能

5、 不影响主线程逻辑

### 13.多线程共同操作同一个数据互斥锁同步？

```python
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
    
        if mutex.acquire(1):
            num +=1
            msg = self.name + 'set num to ' +str(num)
            print msg
            mutex.release()

num = 0
mutex = threading.Lock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()
        
if __name__=="__main__":
    test()
```
### 14.什么是多线程竞争？

线程是非独立的，同一个进程里线程是数据共享的，当各个线程访问数据资源时会出现竞争状态即：数据几乎同步会被多个线程占用，造成数据混乱，即所谓的线程不安全。

那么怎么解决多线程竞争问题？---锁

锁的好处： 确保了某段关键代码（共享数据资源）只能由一个线程从头到尾完整地执行能解决多线程资源竞争下的原子操作问题。

锁的坏处： 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。

锁的致命问题: 死锁

### 15.请介绍一下Python的线程同步？

1、setDaemon(False)

当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行的最小单位，当设置多线程时，主线程会创建多个子线程，在Python中，默认情况下就是setDaemon(False)，主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。

```python
import time
import threading 


def thread():
    time.sleep(2)
    print('---子线程结束---')

def main():
    t1 = threading.Thread(target=thread)
    t1.start()
    print('---主线程--结束')

if __name__ =='__main__':
    main()

# output
# ---主线程--结束
# ---子线程结束---
```

2、setDaemon(True)

当我们使用setDaemon(True)时，这是子线程为守护线程，主线程一旦执行结束，则全部子线程被强制终止。

```python
import time
import threading

def thread():
    time.sleep(2)
    print(’---子线程结束---')

def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)#设置子线程守护主线程
    t1.start()
    print('---主线程结束---')

if __name__ =='__main__':
    main()

# 执行结果
# ---主线程结束--- #只有主线程结束，子线程来不及执行就被强制结束
```

3、join（线程同步)

join 所完成的工作就是线程同步，即主线程任务结束以后，进入堵塞状态，一直等待所有的子线程结束以后，主线程再终止。

当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序，所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和，简单的来说，就是给每个子线程一个timeou的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。

没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，主线程结束，但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出。

```python
import threading
import time

def thread():
    time.sleep(2)
    print('---子线程结束---')

def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
    t1.join(timeout=1)  #1 线程同步，主线程堵塞1s 然后主线程结束，子线程继续执行
                        #2 如果不设置timeout参数就等子线程结束主线程再结束
                        #3 如果设置了setDaemon=True和timeout=1主线程等待1s后会强制杀死子线程，然后主线程结束
    print('---主线程结束---')

if __name__=='__main___':
    main()
```

### 16.解释以下什么是锁，有哪几种锁？

锁(Lock)是python提供的对线程控制的对象。

有互斥锁，可重入锁，死锁。

### 17.什么是死锁？

若干子线程在系统资源竞争时，都在等待对方对某部分资源解除占用状态，结果是谁也不愿先解锁，互相干等着，程序无法执行下去，这就是死锁。

GIL锁 全局解释器锁

作用： 限制多线程同时执行，保证同一时间只有一个线程执行，所以cython里的多线程其实是伪多线程！

所以python里常常使用协程技术来代替多线程，协程是一种更轻量级的线程。

进程和线程的切换时由系统决定，而协程由我们程序员自己决定，而模块gevent下切换是遇到了耗时操作时才会切换

三者的关系：进程里有线程，线程里有协程。

### 18.多线程交互访问数据，如果访问到了就不访问了？

怎么避免重读？

创建一个已访问数据列表，用于存储已经访问过的数据，并加上互斥锁，在多线程访问数据的时候先查看数据是否在已访问的列表中，若已存在就直接跳过。

### 19.什么是线程安全，什么是互斥锁？

每个对象都对应于一个可称为「互斥锁」的标记，这个标记用来保证在任一时刻，只能有一个线程访问该对象。

同一进程中的多线程之间是共享系统资源的，多个线程同时对一个对象进行操作，一个线程操作尚未结束，另一线程已经对其进行操作，导致最终结果出现错误，此时需要对被操作对象添加互斥锁，保证每个线程对该对象的操作都得到正确的结果。

### 20.说说下面几个概念：同步，异步，阻塞，非阻塞？

同步： 多个任务之间有先后顺序执行，一个执行完下个才能执行。

异步： 多个任务之间没有先后顺序，可以同时执行，有时候一个任务可能要在必要的时候获取另一个同时执行的任务的结果，这个就叫回调！

阻塞： 如果卡住了调用者，调用者不能继续往下执行，就是说调用者阻塞了。

非阻塞： 如果不会卡住，可以继续执行，就是说非阻塞的。

同步异步相对于多任务而言，阻塞非阻塞相对于代码执行而言。

### 21.什么是僵尸进程和孤儿进程？怎么避免僵尸进程？

孤儿进程： 父进程退出，子进程还在运行的这些子进程都是孤儿进程，孤儿进程将被 init 进程（进程号为1）所收养，并由 init 进程对他们完成状态收集工作。

僵尸进程： 进程使用 fork 创建子进程，如果子进程退出，而父进程并没有调用 wait 或 waitpid 获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中的这些进程是僵尸进程。

避免僵尸进程的方法：

1.fork 两次用孙子进程去完成子进程的任务

2.用 wait() 函数使父进程阻塞

3.使用信号量，在 signal handler 中调用 waitpid，这样父进程不用阻塞。

###  22.python中进程与线程的使用场景？

多进程适合在CPU密集操作（cpu操作指令比较多，如位多的的浮点运算）。

多线程适合在IO密性型操作（读写数据操作比多的的，比如爬虫）

###  23.线程是并发还是并行，进程是并发还是并行？

线程是并发，进程是并行;

进程之间互相独立，是系统分配资源的最小单位，同一个线程中的所有线程共享资源。

### 24.并行（parallel）和并发（concurrency）?

并行： 同一时刻多个任务同时在运行

不会在同一时刻同时运行，存在交替执行的情况。

实现并行的库有： multiprocessing

实现并发的库有:  threading

程序需要执行较多的读写、请求和回复任务的需要大量的IO操作，IO密集型操作使用并发更好。

CPU运算量大的程序，使用并行会更好

### 25.IO密集型和CPU密集型区别？

IO密集型： 系统运行，大部分的状况是CPU在等 I/O（硬盘/内存）的读/写

CPU密集型： 大部分时间用来做计算，逻辑判断等CPU动作的程序称之CPU密集型。

### 26.python asyncio的原理？

asyncio这个库就是使用python的yield这个可以打断保存当前函数的上下文的机制， 封装好了 selector 摆脱掉了复杂的回调关系。

### 27.谈谈你对多进程，多线程，以及协程的理解，项目是否用？

这个问题被问的概念相当之大：

进程：一个运行的程序（代码）就是一个进程，没有运行的代码叫程序，进程是系统资源分配的最小单位，进程拥有自己独立的内存空间，所有进程间数据不共享，开销大。

线程: cpu调度执行的最小单位，也叫执行路径，不能独立存在，依赖进程存在，一个进程至少有一个线程，叫主线程，而多个线程共享内存（数据共享，共享全局变量)，从而极大地提高了程序的运行效率。

协程: 是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操中栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。
