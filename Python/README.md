<!-- TOC -->

- [Python精选](#Python精选)
    - [必备知识](必备知识)
        - [1.Python的函数参数传递](#1python%e7%9a%84%e5%87%bd%e6%95%b0%e5%8f%82%e6%95%b0%e4%bc%a0%e9%80%92)
        - [2.Python中的元类(metaclass)](#2python%e4%b8%ad%e7%9a%84%e5%85%83%e7%b1%bbmetaclass)
        - [3.@staticmethod和@classmethod](#3@staticmethod和@classmethod)
        - [4.类变量和实例变量](#4类变量和实例变量)
        - [5.Python自省](#5python%e8%87%aa%e7%9c%81)
        - [6.字典推导式](#6字典推导式)
        - [7.Python中单下划线和双下划线](#7python%e4%b8%ad%e5%8d%95%e4%b8%8b%e5%88%92%e7%ba%bf%e5%92%8c%e5%8f%8c%e4%b8%8b%e5%88%92%e7%ba%bf)
        - [8.字符串格式化:%和.format](#8%e5%ad%97%e7%ac%a6%e4%b8%b2%e6%a0%bc%e5%bc%8f%e5%8c%96%e5%92%8cformat)
        - [9.迭代器和生成器](#9%e8%bf%ad%e4%bb%a3%e5%99%a8%e5%92%8c%e7%94%9f%e6%88%90%e5%99%a8)
        - [10.`*args` 和 `**kwargs`](#10args-%e5%92%8c-kwargs)
        - [11.面向切面编程AOP和装饰器](#11%e9%9d%a2%e5%90%91%e5%88%87%e9%9d%a2%e7%bc%96%e7%a8%8baop%e5%92%8c%e8%a3%85%e9%a5%b0%e5%99%a8)
        - [12.鸭子类型](#12%e9%b8%ad%e5%ad%90%e7%b1%bb%e5%9e%8b)
        - [13.Python中重载](#13python%e4%b8%ad%e9%87%8d%e8%bd%bd)
        - [14.新式类和旧式类](#14%e6%96%b0%e5%bc%8f%e7%b1%bb%e5%92%8c%e6%97%a7%e5%bc%8f%e7%b1%bb)
        - [15.`__new__`和`__init__`的区别](#15new%e5%92%8cinit%e7%9a%84%e5%8c%ba%e5%88%ab)
        - [16.单例模式](#16%e5%8d%95%e4%be%8b%e6%a8%a1%e5%bc%8f)
        - [17.Python中的作用域](#17python%e4%b8%ad%e7%9a%84%e4%bd%9c%e7%94%a8%e5%9f%9f)
        - [18.GIL线程全局锁](#18gil%e7%ba%bf%e7%a8%8b%e5%85%a8%e5%b1%80%e9%94%81)
        - [19.协程](#19%e5%8d%8f%e7%a8%8b)
        - [20.闭包](#20%e9%97%ad%e5%8c%85)
        - [21.lambda函数](#21lambda%e5%87%bd%e6%95%b0)
        - [22.Python函数式编程](#22python%e5%87%bd%e6%95%b0%e5%bc%8f%e7%bc%96%e7%a8%8b)
        - [23.Python里的拷贝](#23python%e9%87%8c%e7%9a%84%e6%8b%b7%e8%b4%9d)
        - [24.Python垃圾回收机制](#24python%e5%9e%83%e5%9c%be%e5%9b%9e%e6%94%b6%e6%9c%ba%e5%88%b6)
        - [25.Python的List](#25python%e7%9a%84list)
        - [26.Python的is](#26python%e7%9a%84is)
        - [27.read,readline和readlines](#27readreadline%e5%92%8creadlines)
        - [28.Python2和3的区别](#28python2%e5%92%8c3%e7%9a%84%e5%8c%ba%e5%88%ab)
        - [29.super init](#29super-init)
        - [30.range and xrange](#30range-and-xrange)
- [Python基础](#python基础)
    - [文件操作](#文件操作)
        - [31.Python 处理文件](#31python-%e5%a4%84%e7%90%86%e6%96%87%e4%bb%b6)
        - [32.遍历文件夹](#32%e9%81%8d%e5%8e%86%e6%96%87%e4%bb%b6%e5%a4%b9)
    - [模块与包](#模块与包)
        - [33.输入日期，判断这一天是这一年的第几天？](#33%e8%be%93%e5%85%a5%e6%97%a5%e6%9c%9f%e5%88%a4%e6%96%ad%e8%bf%99%e4%b8%80%e5%a4%a9%e6%98%af%e8%bf%99%e4%b8%80%e5%b9%b4%e7%9a%84%e7%ac%ac%e5%87%a0%e5%a4%a9)
        - [34.打乱一个排好序的list对象](#34%e6%89%93%e4%b9%b1%e4%b8%80%e4%b8%aa%e6%8e%92%e5%a5%bd%e5%ba%8f%e7%9a%84list%e5%af%b9%e8%b1%a1)
    - [数据类型](#数据类型)
        - [35.将字典按value值进行排序](#35%e5%b0%86%e5%ad%97%e5%85%b8%e6%8c%89value%e5%80%bc%e8%bf%9b%e8%a1%8c%e6%8e%92%e5%ba%8f)
        - [36.请反转字符串 "aStr"](#36%e8%af%b7%e5%8f%8d%e8%bd%ac%e5%ad%97%e7%ac%a6%e4%b8%b2-%22astr%22)
        - [37.将字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {k:1,k1:2,...}](#37%e5%b0%86%e5%ad%97%e7%ac%a6%e4%b8%b2-%22k1k12k23k34%22-%e5%a4%84%e7%90%86%e6%88%90%e5%ad%97%e5%85%b8-k1k12)
        - [38.列表切片](#38%e5%88%97%e8%a1%a8%e5%88%87%e7%89%87)
        - [39.写一个列表生成式，产生一个公差为11的等差数列](#39%e5%86%99%e4%b8%80%e4%b8%aa%e5%88%97%e8%a1%a8%e7%94%9f%e6%88%90%e5%bc%8f%e4%ba%a7%e7%94%9f%e4%b8%80%e4%b8%aa%e5%85%ac%e5%b7%ae%e4%b8%ba11%e7%9a%84%e7%ad%89%e5%b7%ae%e6%95%b0%e5%88%97)
        - [40.给定两个列表，找出他们相同的元素和不同的元素](#40%e7%bb%99%e5%ae%9a%e4%b8%a4%e4%b8%aa%e5%88%97%e8%a1%a8%e6%89%be%e5%87%ba%e4%bb%96%e4%bb%ac%e7%9b%b8%e5%90%8c%e7%9a%84%e5%85%83%e7%b4%a0%e5%92%8c%e4%b8%8d%e5%90%8c%e7%9a%84%e5%85%83%e7%b4%a0)
        
    - [企业面试题](#企业面试题)
        - [41.python中内置的数据结构有几种](#41python%e4%b8%ad%e5%86%85%e7%bd%ae%e7%9a%84%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84%e6%9c%89%e5%87%a0%e7%a7%8d)
        - [42.反转一个整数，例如-123 --> -321](#42%e5%8f%8d%e8%bd%ac%e4%b8%80%e4%b8%aa%e6%95%b4%e6%95%b0%e4%be%8b%e5%a6%82-123-----321)
        - [43.实现遍历目录与子目录，抓取.pyc文件](#43%e5%ae%9e%e7%8e%b0%e9%81%8d%e5%8e%86%e7%9b%ae%e5%bd%95%e4%b8%8e%e5%ad%90%e7%9b%ae%e5%bd%95%e6%8a%93%e5%8f%96pyc%e6%96%87%e4%bb%b6)
        - [44.Python遍历列表时删除元素的正确做法](#44python%e9%81%8d%e5%8e%86%e5%88%97%e8%a1%a8%e6%97%b6%e5%88%a0%e9%99%a4%e5%85%83%e7%b4%a0%e7%9a%84%e6%ad%a3%e7%a1%ae%e5%81%9a%e6%b3%95)
        - [45.字符串 `"123"` 转换成 `123`，不使用内置api，例如 `int()`](#45%e5%ad%97%e7%ac%a6%e4%b8%b2-%22123%22-%e8%bd%ac%e6%8d%a2%e6%88%90-123%e4%b8%8d%e4%bd%bf%e7%94%a8%e5%86%85%e7%bd%aeapi%e4%be%8b%e5%a6%82-int)
        - [46.统计一个文本中单词频次最高的10个单词](#46%e7%bb%9f%e8%ae%a1%e4%b8%80%e4%b8%aa%e6%96%87%e6%9c%ac%e4%b8%ad%e5%8d%95%e8%af%8d%e9%a2%91%e6%ac%a1%e6%9c%80%e9%ab%98%e7%9a%8410%e4%b8%aa%e5%8d%95%e8%af%8d)
        - [47.阅读一下代码他们的输出结果是什么？](#47%e9%98%85%e8%af%bb%e4%b8%80%e4%b8%8b%e4%bb%a3%e7%a0%81%e4%bb%96%e4%bb%ac%e7%9a%84%e8%be%93%e5%87%ba%e7%bb%93%e6%9e%9c%e6%98%af%e4%bb%80%e4%b9%88)

- [Python高级](#python高级)
    - [元类](#元类)
        - [48.介绍Cython，Pypy Cpython Numba各有什么缺点](#48%e4%bb%8b%e7%bb%8dcythonpypy-cpython-numba%e5%90%84%e6%9c%89%e4%bb%80%e4%b9%88%e7%bc%ba%e7%82%b9)
        - [49.请描述抽象类和接口类的区别和联系](#49%e8%af%b7%e6%8f%8f%e8%bf%b0%e6%8a%bd%e8%b1%a1%e7%b1%bb%e5%92%8c%e6%8e%a5%e5%8f%a3%e7%b1%bb%e7%9a%84%e5%8c%ba%e5%88%ab%e5%92%8c%e8%81%94%e7%b3%bb)
        - [50.Python中如何动态获取和设置对象的属性](#50python%e4%b8%ad%e5%a6%82%e4%bd%95%e5%8a%a8%e6%80%81%e8%8e%b7%e5%8f%96%e5%92%8c%e8%ae%be%e7%bd%ae%e5%af%b9%e8%b1%a1%e7%9a%84%e5%b1%9e%e6%80%a7)
    
    - [内存管理与垃圾回收机制](#内存管理与垃圾回收机制)
        - [51.哪些操作会导致Python内存溢出，怎么处理](#51%e5%93%aa%e4%ba%9b%e6%93%8d%e4%bd%9c%e4%bc%9a%e5%af%bc%e8%87%b4python%e5%86%85%e5%ad%98%e6%ba%a2%e5%87%ba%e6%80%8e%e4%b9%88%e5%a4%84%e7%90%86)
        - [52.内存泄露是什么？如何避免？](#52内存泄露是什么如何避免)
    
    - [函数](#函数)
        - [53.手写一个判断时间的装饰器](#53%e6%89%8b%e5%86%99%e4%b8%80%e4%b8%aa%e5%88%a4%e6%96%ad%e6%97%b6%e9%97%b4%e7%9a%84%e8%a3%85%e9%a5%b0%e5%99%a8)
        - [54.带参数的装饰器](#54%e5%b8%a6%e5%8f%82%e6%95%b0%e7%9a%84%e8%a3%85%e9%a5%b0%e5%99%a8)
        - [55.线程安全的装饰器](#55%e7%ba%bf%e7%a8%8b%e5%ae%89%e5%85%a8%e7%9a%84%e8%a3%85%e9%a5%b0%e5%99%a8)
        - [56.交换两个变量的值](#56%e4%ba%a4%e6%8d%a2%e4%b8%a4%e4%b8%aa%e5%8f%98%e9%87%8f%e7%9a%84%e5%80%bc)
        - [57.hasattr() getattr() setattr() 函数使用详解](#57hasattr-getattr-setattr-%e5%87%bd%e6%95%b0%e4%bd%bf%e7%94%a8%e8%af%a6%e8%a7%a3)
        
    - [设计模式](#设计模式)
        - [58.对装饰器的理解，并写出一个计时器记录方法执行性能的装饰器](#58%e5%af%b9%e8%a3%85%e9%a5%b0%e5%99%a8%e7%9a%84%e7%90%86%e8%a7%a3%e5%b9%b6%e5%86%99%e5%87%ba%e4%b8%80%e4%b8%aa%e8%ae%a1%e6%97%b6%e5%99%a8%e8%ae%b0%e5%bd%95%e6%96%b9%e6%b3%95%e6%89%a7%e8%a1%8c%e6%80%a7%e8%83%bd%e7%9a%84%e8%a3%85%e9%a5%b0%e5%99%a8)
        - [59.Python中yield的用法](#59python中yield的用法)
    
    - [面向对象](#面向对象)
        - [60.Python的魔法方法](#60python%e7%9a%84%e9%ad%94%e6%b3%95%e6%96%b9%e6%b3%95)
        - [61.面向对象中怎么实现只读属性](#61%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e4%b8%ad%e6%80%8e%e4%b9%88%e5%ae%9e%e7%8e%b0%e5%8f%aa%e8%af%bb%e5%b1%9e%e6%80%a7)
        - [62.谈谈你对面向对象的理解](#62%e8%b0%88%e8%b0%88%e4%bd%a0%e5%af%b9%e9%9d%a2%e5%90%91%e5%af%b9%e8%b1%a1%e7%9a%84%e7%90%86%e8%a7%a3)

    - [正则表达式](#正则表达式)
        - [63.请写出一段代码用正则匹配出ip](#63%e8%af%b7%e5%86%99%e5%87%ba%e4%b8%80%e6%ae%b5%e4%bb%a3%e7%a0%81%e7%94%a8%e6%ad%a3%e5%88%99%e5%8c%b9%e9%85%8d%e5%87%baip)
        - [64.Python字符串查找和替换？](#64python字符串查找和替换)
        - [65.正则表达式贪婪与非贪婪模式的区别？](#65正则表达式贪婪与非贪婪模式的区别)
        - [66.写出开头匹配字母和下划线，末尾是数字的正则表达式？](#66写出开头匹配字母和下划线末尾是数字的正则表达式)
        - [67.怎么过滤评论中的表情？](#67怎么过滤评论中的表情)
        - [68.Python里match与search的区别？](#68python里match与search的区别)

- [Web](#web)
    - [Flask](#flask)
        - [140.对Flask蓝图(Blueprint)的理解？](#140对flask蓝图blueprint的理解)
        - [141.Flask 和 Django 路由映射的区别？](#141flask-和-django-路由映射的区别)
    - [Django](#django)
        - [142.什么是wsgi,uwsgi,uWSGI?](#142什么是wsgiuwsgiuwsgi)
        - [143.Django、Flask、Tornado的对比？](#143djangoflasktornado的对比)
        - [144.CORS 和 CSRF的区别？](#144cors-和-csrf的区别)
        - [145.Session,Cookie,JWT的理解](#145sessioncookiejwt的理解)
        - [146.简述Django请求生命周期](#146简述django请求生命周期)
        - [147.用的restframework完成api发送时间时区](#147用的restframework完成api发送时间时区)
        - [148.nginx,tomcat,apach到都是什么？](#148nginxtomcatapach到都是什么)
        - [149.请给出你熟悉关系数据库范式有哪些，有什么作用？](#149请给出你熟悉关系数据库范式有哪些有什么作用)
        - [150.简述QQ登陆过程](#150简述qq登陆过程)
        - [151.post 和 get的区别?](#151post-和-get的区别)
        - [152.项目中日志的作用](#152项目中日志的作用)
        - [153.django中间件的使用？](#153django中间件的使用)
        - [154.谈一下你对uWSGI和nginx的理解？](#154谈一下你对uwsgi和nginx的理解)
        - [155.Django中哪里用到了线程？哪里用到了协程？哪里用到了进程？](#155django中哪里用到了线程哪里用到了协程哪里用到了进程)
        - [156.有用过Django REST framework吗？](#156有用过django-rest-framework吗)
    - [爬虫](#爬虫)
        - [159.试列出至少三种目前流行的大型数据库](#159试列出至少三种目前流行的大型数据库)
        - [160.列举您使用过的Python网络爬虫所用到的网络数据包?](#160列举您使用过的python网络爬虫所用到的网络数据包)
        - [161.爬取数据后使用哪个数据库存储数据的，为什么？](#161爬取数据后使用哪个数据库存储数据的为什么)
        - [162.你用过的爬虫框架或者模块有哪些？优缺点？](#162你用过的爬虫框架或者模块有哪些优缺点)
        - [163.写爬虫是用多进程好？还是多线程好？](#163写爬虫是用多进程好还是多线程好)
        - [164.常见的反爬虫和应对方法？](#164常见的反爬虫和应对方法)
        - [165.解析网页的解析器使用最多的是哪几个?](#165解析网页的解析器使用最多的是哪几个)
        - [166.需要登录的网页，如何解决同时限制ip，cookie,session](#166需要登录的网页如何解决同时限制ipcookiesession)
        - [167.验证码的解决?](#167验证码的解决)
        - [168.使用最多的数据库，对他们的理解？](#168使用最多的数据库对他们的理解)
        - [169.编写过哪些爬虫中间件？](#169编写过哪些爬虫中间件)
        - [170.“极验”滑动验证码如何破解？](#170极验滑动验证码如何破解)
        - [171.爬虫多久爬一次，爬下来的数据是怎么存储？](#171爬虫多久爬一次爬下来的数据是怎么存储)
        - [172.cookie过期的处理问题？](#172cookie过期的处理问题)
        - [173.动态加载又对及时性要求很高怎么处理？](#173动态加载又对及时性要求很高怎么处理)
        - [174.HTTPS有什么优点和缺点？](#174https有什么优点和缺点)
        - [175.HTTPS是如何实现安全传输数据的？](#175https是如何实现安全传输数据的)
        - [176.TTL，MSL，RTT各是什么？](#176ttlmslrtt各是什么)
        - [177.谈一谈你对Selenium和PhantomJS了解](#177谈一谈你对selenium和phantomjs了解)
        - [178.平常怎么使用代理的 ？](#178平常怎么使用代理的-)
        - [179.存放在数据库(redis、mysql等)。](#179存放在数据库redismysql等)
        - [180.怎么监控爬虫的状态?](#180怎么监控爬虫的状态)
        - [181.描述下scrapy框架运行的机制？](#181描述下scrapy框架运行的机制)
        - [182.谈谈你对Scrapy的理解？](#182谈谈你对scrapy的理解)
        - [183.怎么样让 scrapy 框架发送一个 post 请求（具体写出来）](#183怎么样让-scrapy-框架发送一个-post-请求具体写出来)
        - [184.怎么监控爬虫的状态 ？](#184怎么监控爬虫的状态-)
        - [185.怎么判断网站是否更新？](#185怎么判断网站是否更新)
        - [186.图片、视频爬取怎么绕过防盗连接](#186图片视频爬取怎么绕过防盗连接)
        - [187.你爬出来的数据量大概有多大？大概多长时间爬一次？](#187你爬出来的数据量大概有多大大概多长时间爬一次)
        - [188.用什么数据库存爬下来的数据？部署是你做的吗？怎么部署？](#188用什么数据库存爬下来的数据部署是你做的吗怎么部署)
        - [189.增量爬取](#189增量爬取)
        - [190.爬取下来的数据如何去重，说一下scrapy的具体的算法依据。](#190爬取下来的数据如何去重说一下scrapy的具体的算法依据)
        - [191.Scrapy的优缺点?](#191scrapy的优缺点)
        - [192.怎么设置爬取深度？](#192怎么设置爬取深度)
        - [193.scrapy和scrapy-redis有什么区别？为什么选择redis数据库？](#193scrapy和scrapy-redis有什么区别为什么选择redis数据库)
        - [194.分布式爬虫主要解决什么问题？](#194分布式爬虫主要解决什么问题)
        - [195.什么是分布式存储？](#195什么是分布式存储)
        - [196.你所知道的分布式爬虫方案有哪些？](#196你所知道的分布式爬虫方案有哪些)
        - [197.scrapy-redis，有做过其他的分布式爬虫吗？](#197scrapy-redis有做过其他的分布式爬虫吗)
    
    - [测试](#测试)
        - [213.编写测试计划的目的是](#213编写测试计划的目的是)
        - [214.对关键词触发模块进行测试](#214对关键词触发模块进行测试)
        - [215.其他常用笔试题目网址汇总](#215其他常用笔试题目网址汇总)
        - [216.测试人员在软件开发过程中的任务是什么](#216测试人员在软件开发过程中的任务是什么)
        - [217.一条软件Bug记录都包含了哪些内容？](#217一条软件bug记录都包含了哪些内容)
        - [218.简述黑盒测试和白盒测试的优缺点](#218简述黑盒测试和白盒测试的优缺点)
        - [219.请列出你所知道的软件测试种类，至少5项](#219请列出你所知道的软件测试种类至少5项)
        - [220.Alpha测试与Beta测试的区别是什么？](#220alpha测试与beta测试的区别是什么)
        - [221.举例说明什么是Bug？一个bug report应包含什么关键字？](#221举例说明什么是bug一个bug-report应包含什么关键字)
    
    - [大数据](#大数据)
        - [242.找出1G的文件中高频词](#242找出1g的文件中高频词)
        - [243.一个大约有一万行的文本文件统计高频词](#243一个大约有一万行的文本文件统计高频词)
        - [244.怎么在海量数据中找出重复次数最多的一个？](#244怎么在海量数据中找出重复次数最多的一个)
        - [245.判断数据是否在大量数据中](#245判断数据是否在大量数据中)

<!-- /TOC -->
# Python精选
## 必备知识
### 1.Python的函数参数传递

看两个例子:

```python
a = 1
def fun(a):
    a = 2
fun(a)
print a  # 1
```

```python
a = []
def fun(a):
    a.append(1)
fun(a)
print a  # [1]
```

所有的变量都可以理解是内存中一个对象的“引用”，或者，也可以看似 C 中 `void*` 的感觉。

通过`id`来看引用`a`的内存地址可以比较理解：

```python
a = 1
def fun(a):
    print "func_in",id(a)   # func_in 41322472
    a = 2
    print "re-point",id(a), id(2)   # re-point 41322448 41322448
print "func_out",id(a), id(1)  # func_out 41322472 41322472
fun(a)
print a  # 1
```

注：具体的值在不同电脑上运行时可能不同。

可以看到，在执行完`a = 2`之后，`a`引用中保存的值，即内存地址发生变化，由原来`1`对象的所在地址变成了`2`这个实体对象的内存地址。

而第2个例子`a`引用保存的内存值就不会发生变化：

```python
a = []
def fun(a):
    print "func_in",id(a)  # func_in 53629256
    a.append(1)
print "func_out",id(a)     # func_out 53629256
fun(a)
print a  # [1]
```

这里记住的是类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。在python中，strings, tuples, 和numbers是不可更改的对象，而 list, dict, set 等则是可以修改的对象。(这就是这个问题的重点)

当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.

如果还不明白的话,这里有更好的解释: http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

### 2.Python中的元类(metaclass)

这个非常的不常用,但是像ORM这种复杂的结构还是会需要的,详情请看:http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

### 3.@staticmethod和@classmethod

Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()
```

这里先理解下函数参数里面的self和cls。这个self和cls是对类或者实例的绑定，对于一般的函数来说我们可以这么调用`foo(x)`，这个函数就是最常用的，它的工作跟任何东西(类,实例)无关。对于实例方法，我们知道在类里每次定义方法的时候都需要绑定这个实例，就是`foo(self, x)`，为什么要这么做呢？因为实例方法的调用离不开实例，我们需要把实例自己传给函数，调用的时候是这样的`a.foo(x)`(其实是`foo(a, x)`)。类方法一样,只不过它传递的是类而不是实例，`A.class_foo(x)`。注意这里的self和cls可以替换别的参数，但是python的约定是这俩，还是不要改的好。

对于静态方法其实和普通的方法一样，不需要对谁进行绑定，唯一的区别是调用的时候需要使用 `a.static_foo(x)` 或者 `A.static_foo(x)` 来调用。

| \\      | 实例方法 | 类方法         | 静态方法        |
| :------ | :------- | :------------- | :-------------- |
| a = A() | a.foo(x) | a.class_foo(x) | a.static_foo(x) |
| A       | 不可用   | A.class_foo(x) | A.static_foo(x) |

更多关于这个问题:

1. http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
2. https://realpython.com/blog/python/instance-class-and-static-methods-demystified/

### 4.类变量和实例变量

**类变量：**

是可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。例如下例中，num_of_instance 就是类变量，用于跟踪存在着多少个 Test 的实例。

**实例变量：**

实例化之后，每个实例单独拥有的变量。

```python
class Test(object):  
    num_of_instance = 0  
    def __init__(self, name):  
        self.name = name  
        Test.num_of_instance += 1  
  
if __name__ == '__main__':  
    print Test.num_of_instance   # 0
    t1 = Test('jack')  
    print Test.num_of_instance   # 1
    t2 = Test('lucy')  
    print t1.name , t1.num_of_instance  # jack 2
    print t2.name , t2.num_of_instance  # lucy 2
```

补充的例子：

```python
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa
```

这里`p1.name="bbb"`是实例调用了类变量，这其实和上面第一个问题一样，就是函数传参的问题，`p1.name` 一开始是指向的类变量`name="aaa"`，但是在实例的作用域里把类变量的引用改变了，就变成了一个实例变量，`self.name` 不再引用Person的类变量name了。

可以看看下面的例子:

```python
class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]
```

参考:http://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block

### 5.Python自省

这个也是python彪悍的特性。

自省就是面向对象的语言所写的程序在运行时，所能知道对象的类型，简单一句就是运行时能够获得对象的类型。比如type()，dir()，getattr()，hasattr()，isinstance()。

```python
a = [1,2,3]
b = {'a':1,'b':2,'c':3}
c = True
print type(a),type(b),type(c) # <type 'list'> <type 'dict'> <type 'bool'>
print isinstance(a,list)  # True
```

### 6.字典推导式

可能你见过列表推导式，却没有见过字典推导式，在2.7中才加入的：

```python
d = {key: value for (key, value) in iterable}
```

### 7.Python中单下划线和双下划线

```python
>>> class MyClass():
...     def __init__(self):
...             self.__superprivate = "Hello"
...             self._semiprivate = ", world!"
...
>>> mc = MyClass()
>>> print mc.__superprivate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: myClass instance has no attribute '__superprivate'
>>> print mc._semiprivate
, world!
>>> print mc.__dict__
{'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}
```

`__foo__`：一种约定，Python内部的名字，用来区别其他用户自定义的命名，以防冲突，就是例如：`__init__()`，`__del__()`，`__call__()` 这些特殊方法；

`_foo`：一种约定，用来指定变量私有，程序员用来指定私有变量的一种方式。不能用 `from module import *` 导入，其他方面和公有一样访问；

`__foo`：这个有真正的意义：解析器用 `_classname__foo` 来代替这个名字，以区别和其他类相同的命名，它无法直接像公有成员一样随便访问，通过 `对象名._类名__xxx` 这样的方式可以访问。

详情见:http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python

或者: http://www.zhihu.com/question/19754941

### 8.字符串格式化:%和.format

`.format` 在许多方面看起来更便利。对于 `%` 最烦人的是它无法同时传递一个变量和元组。你可能会想下面的代码不会有什么问题:

```python
"hi there %s" % name
```

但是，如果name恰好是(1,2,3)，它将会抛出一个 TypeError 异常。为了保证它总是正确的，你必须这样做：

```python
"hi there %s" % (name,)   # 提供一个单元素的数组而不是一个参数
```

`.format` 就没有这些问题。

为了和Python2.5兼容(譬如logging库建议使用`%`([issue #4](https://github.com/taizilongxu/interview_python/issues/4)))

http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

### 9.迭代器和生成器

这个是stackoverflow里python排名第一的问题,值得一看: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

这是中文版: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/1/README.html

这里有个关于生成器的创建问题面试官有考：
问：将列表生成式中 `[]` 改成 `()` 之后数据结构是否改变？ 
答案：是，从列表变为生成器。

```python
>>> L = [x*x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x*x for x in range(10))
>>> g
<generator object <genexpr> at 0x0000028F8B774200>
```

通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator

迭代器是遵循迭代协议的对象。用户可以使用 iter() 以从任何序列得到迭代器（如 list, tuple, dictionary, set 等）。另一个方法则是创建一个另一种形式的迭代器 —— generator 。要获取下一个元素，则使用成员函数 next()（Python 2）或函数 next() function （Python 3） 。当没有元素时，则引发 StopIteration 此例外。若要实现自己的迭代器，则只要实现 next()（Python 2）或 `__next__`()（ Python 3）

生成器（Generator），只是在需要返回数据的时候使用yield语句。每次next()被调用时，生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）

区别： 生成器能做到迭代器能做的所有事，而且因为自动创建iter()和next()方法，生成器显得特别简洁，而且生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出StopIteration异常。

官方介绍：https://docs.python.org/3/tutorial/classes.html#iterators

### 10.`*args` 和 `**kwargs`

用`*args`和`**kwargs`只是为了方便并没有强制使用它们.

当你不确定你的函数里将要传递多少参数时你可以用`*args`.例如,它可以传递任意数量的参数:

```python
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print '{0}. {1}'.format(count, thing)
...
>>> print_everything('apple', 'banana', 'cabbage')
1. apple
2. banana
3. cabbage
```

相似的,`**kwargs`允许你使用没有事先定义的参数名:

```python
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print '{0} = {1}'.format(name, value)
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```

你也可以混着用.命名参数首先获得参数值然后所有的其他参数都传递给`*args`和`**kwargs`.命名参数在列表的最前端.例如:

```python
def table_things(titlestring, **kwargs)
```

`*args`和`**kwargs`可以同时在函数的定义中,但是`*args`必须在`**kwargs`前面.

当调用函数时你也可以用`*`和`**`语法.例如:

```python
>>> def print_three_things(a, b, c):
...     print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)

a = aardvark, b = baboon, c = cat
```

就像你看到的一样,它可以传递列表(或者元组)的每一项并把它们解包.注意必须与它们在函数里的参数相吻合.当然,你也可以在函数定义或者函数调用时用 `*`.

http://stackoverflow.com/questions/3394835/args-and-kwargs

### 11.面向切面编程AOP和装饰器

这个AOP一听起来有点懵,同学面阿里的时候就被问懵了...

装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。

概括的讲，**装饰器的作用就是为已经存在的对象添加额外的功能。**

这个问题比较大,推荐: http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python

中文: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html

### 12.鸭子类型

“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”

我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。

比如在python中，有很多file-like的东西，比如StringIO,GzipFile,socket。它们有很多相同的方法，我们把它们当作文件使用。

又比如list.extend()方法中,我们并不关心它的参数是不是list,只要它是可迭代的,所以它的参数可以是list/tuple/dict/字符串/生成器等.

鸭子类型在动态语言中经常使用，非常灵活，使得python不想java那样专门去弄一大堆的设计模式。

### 13.Python中重载

引自知乎:http://www.zhihu.com/question/20053359

函数重载主要是为了解决两个问题。

1. 可变参数类型。
2. 可变参数个数。

另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。

好吧，那么对于情况 1，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数。

那么对于情况 2，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。

好了，鉴于情况 1 跟情况 2 都有了解决方案，python 自然就不需要函数重载了。

### 14.新式类和旧式类

这个面试官问了，我说了老半天，不知道他问的真正意图是什么。

[stackoverflow](http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python)

这篇文章很好的介绍了新式类的特性: http://www.cnblogs.com/btchenguang/archive/2012/09/17/2689146.html

新式类很早在2.2就出现了，所以旧式类完全是兼容的问题，Python3 里的类全部都是新式类。

这里有一个 MRO 问题可以了解下(新式类继承是根据C3算法，旧式类是深度优先)，<Python核心编程>里讲的也很多。

> 一个旧式类的深度优先的例子

```python
class A():
    def foo1(self):
        print "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass

d = D()
d.foo1()

# A
```

**按照经典类的查找顺序`从左到右深度优先`的规则，在访问`d.foo1()`的时候,D这个类是没有的..那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过**

### 15.`__new__`和`__init__`的区别

这个`__new__`确实很少见到,先做了解吧.

1. `__new__`是一个静态方法,而`__init__`是一个实例方法.
2. `__new__`方法会返回一个创建的实例,而`__init__`什么都不返回.
3. 只有在`__new__`返回一个cls的实例时后面的`__init__`才能被调用.
4. 当创建一个新实例时调用`__new__`,初始化一个实例时用`__init__`.

[stackoverflow](http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init)

ps: `__metaclass__`是创建类时起作用.所以我们可以分别使用`__metaclass__`,`__new__`和`__init__`来分别在类创建,实例创建和实例初始化的时候做一些小手脚.

### 16.单例模式

> ​	单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。
>
> `__new__()`在`__init__()`之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例
> **这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.**

#### 1 使用`__new__`方法

```python
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
```

#### 2 共享属性

创建实例时把所有实例的`__dict__`指向同一个字典,这样它们具有相同的属性和方法.

```python
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1
```

#### 3 装饰器版本

```python
def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
  ...
```

#### 4 import方法

作为python的模块是天然的单例模式

```python
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()
```

**[单例模式伯乐在线详细解释](http://python.jobbole.com/87294/)**

### 17.Python中的作用域

函数作用域的 LEGB 顺序：

L：local 函数内部作用域

E：enclosing 函数内部与内嵌函数之间

G：global 全局作用域

B：build-in 内置作用域

Python 中，一个变量的作用域总是由在代码中被赋值的地方所决定的。

当 Python 遇到一个变量的话他会按照这样的顺序进行搜索：

本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）

### 18.GIL线程全局锁

线程全局锁(Global Interpreter Lock),即Python为了保证线程安全而采取的独立线程运行的限制,说白了就是一个核只能在同一时间运行一个线程.**对于io密集型任务，python的多线程起到作用，但对于cpu密集型任务，python的多线程几乎占不到任何优势，还有可能因为争夺资源而变慢。**

见[Python 最难的问题](http://www.oschina.net/translate/pythons-hardest-problem)

解决办法就是多进程和下面的协程(协程也只是单CPU,但是能减小切换代价提升性能).

### 19.协程

知乎被问到了,呵呵哒,跪了

简单点说协程是进程和线程的升级版,进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间,而协程就是用户自己控制切换的时机,不再需要陷入系统的内核态.

Python里最常见的yield就是协程的思想!可以查看第九个问题.

### 20.闭包

闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

当一个内嵌函数引用其外部作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:

1. 必须有一个内嵌函数
2. 内嵌函数必须引用外部函数中的变量
3. 外部函数的返回值必须是内嵌函数

感觉闭包还是有难度的,几句话是说不明白的,还是查查相关资料.

重点是函数运行后并不会被撤销,就像16题的instance字典一样,当函数运行完后,instance并不被销毁,而是继续留在内存空间里.这个功能类似类里的类变量,只不过迁移到了函数上.

闭包就像个空心球一样,你知道外面和里面,但你不知道中间是什么样.

### 21.lambda函数

其实就是一个匿名函数,为什么叫lambda?因为和后面的函数式编程有关.

推荐: [知乎](http://www.zhihu.com/question/20125256)

### 22.Python函数式编程

这个需要适当的了解一下吧,毕竟函数式编程在Python中也做了引用.

推荐: [酷壳](http://coolshell.cn/articles/10822.html)

python中函数式编程支持:

filter 函数的功能相当于过滤器。调用一个布尔函数`bool_func`来迭代遍历每个seq中的元素；返回一个使`bool_seq`返回值为true的元素的序列。

```python
>>>a = [1,2,3,4,5,6,7]
>>>b = filter(lambda x: x > 5, a)
>>>print b
>>>[6,7]
```

map函数是对一个序列的每个项依次执行函数，下面是对一个序列每个项都乘以2：

```python
>>> a = map(lambda x:x*2,[1,2,3])
>>> list(a)
[2, 4, 6]
```

reduce函数是对一个序列的每个项迭代调用函数，下面是求3的阶乘：

```python
>>> reduce(lambda x,y:x*y,range(1,4))
6
```

### 23.Python里的拷贝

引用和copy(),deepcopy()的区别

```python
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'd = ', d

输出结果：
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
```

### 24.Python垃圾回收机制

Python GC 主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。

#### 1 引用计数

PyObject是每个对象必有的内容，其中`ob_refcnt`就是做为引用计数。当一个对象有新的引用时，它的`ob_refcnt`就会增加，当引用它的对象被删除，它的`ob_refcnt`就会减少.引用计数为0时，该对象生命就结束了。

优点:

1. 简单
2. 实时性

缺点:

1. 维护引用计数消耗资源
2. 循环引用

#### 2 标记-清除机制

基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。

#### 3 分代技术

分代回收的整体思想是：将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。

Python默认定义了三代对象集合，索引数越大，对象存活时间越长。

举例：
当某些内存块M经过了3次垃圾收集的清洗之后还存活时，我们就将内存块M划到一个集合A中去，而新分配的内存都划分到集合B中去。当垃圾收集开始工作时，大多数情况都只对集合B进行垃圾回收，而对集合A进行垃圾回收要隔相当长一段时间后才进行，这就使得垃圾收集机制需要处理的内存少了，效率自然就提高了。在这个过程中，集合B中的某些内存块由于存活时间长而会被转移到集合A中，当然，集合A中实际上也存在一些垃圾，这些垃圾的回收会因为这种分代的机制而被延迟。

### 25.Python的List

推荐: http://www.jianshu.com/p/J4U6rR

### 26.Python的is

is是对比地址,==是对比值

### 27.read,readline和readlines

- read        读取整个文件
- readline    读取下一行,使用生成器方法
- readlines   读取整个文件到一个迭代器以供我们遍历

### 28.Python2和3的区别

推荐：[Python 2.7.x 与 Python 3.x 的主要差异](http://chenqx.github.io/2014/11/10/Key-differences-between-Python-2-7-x-and-Python-3-x/)

### 29.super init

super() lets you avoid referring to the base class explicitly, which can be nice. But the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen. See the standard docs on super if you haven't already.

Note that the syntax changed in Python 3.0: you can just say super().`__init__`() instead of super(ChildB, self).`__init__`() which IMO is quite a bit nicer.

http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

[Python2.7中的super方法浅见](http://blog.csdn.net/mrlevo520/article/details/51712440)

https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html

### 30.range and xrange

都在循环时使用，xrange内存性能更好。
for i in range(0, 20):
for i in xrange(0, 20):
What is the difference between range and xrange functions in Python 2.X?
 range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
 xrange is a sequence object that evaluates lazily.

http://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x

# Python基础

## 文件操作

### 31.Python 处理文件

有一个 jsonline 格式的文件 file.txt 大小约为 10K，很简单，直接读取处理就可以了。

```python
def get_lines():
    with open('file.txt','rb') as f:
        return f.readlines()

if __name__ == '__main__':
    for e in get_lines():
        process(e) # 处理每一行数据
```

现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改 `get_lines` 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？

生成器方式：

```python
def get_lines():
    with open('file.txt','rb') as f:
        for i in f:
            yield i
```

分块读取方式：

```python
from mmap import mmap

def get_lines(fp):
    with open(fp,"r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char==b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1

if __name__=="__main__":
    for i in get_lines("fp_some_huge_file"):
        print(i)
```

要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入分批读入数据要记录每次读入数据的位置。分批每次读取数据的大小，太小会在读取操作花费过多时间。
https://stackoverflow.com/questions/30294146/python-fastest-way-to-process-large-file

### 32.遍历文件夹

```python
import os

def print_directory_contents(sPath):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)
```

## 模块与包

### 33.输入日期，判断这一天是这一年的第几天？

```python
import datetime

def dayofyear():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return (date1-date2).days+1
```

### 34.打乱一个排好序的list对象

```python
import random

alist = [1,2,3,4,5]
random.shuffle(alist)
print(alist)
```

## 数据类型

### 35.将字典按value值进行排序

```python
sorted(d.items(), key=lambda x:x[1])
```

### 36.请反转字符串 "aStr"

```python
print("aStr"[::-1])
```

### 37.将字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {k:1,k1:2,...}

```python
str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key, value = iterms.split(':')
        dict1[key] = value
    return dict1
```

或者直接用字典推导式：

```python
d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
```

### 38.列表切片

```python
list = ['a','b','c','d','e']
print(list[10:])
```

代码将输出 `[]`，不会产生IndexError错误，就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如，尝试获取list[10]和之后的成员，会导致IndexError。

然而，尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。

### 39.写一个列表生成式，产生一个公差为11的等差数列

```python
print([x*11 for x in range(10)])
```

### 40.给定两个列表，找出他们相同的元素和不同的元素

```python
list1 = [1,2,3]
list2 = [3,4,5]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)
print(set1 ^ set2)
```

## 企业面试题

### 41.python中内置的数据结构有几种
a. 整型 int、 长整型 long、浮点型 float、 复数 complex

b. 字符串 str、 列表 list、 元组 tuple

c. 字典 dict 、 集合 set

d. Python3 中没有 long，只有无限精度的 int

### 42.反转一个整数，例如-123 --> -321

```python
class Solution(object):
    def reverse(self,x):
        if -10<x<10:
            return x

        str_x = str(x)
        if str_x[0] !="-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x

        return x if -2147483648<x<2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)
```

### 43.实现遍历目录与子目录，抓取.pyc文件

第一种方法：

```python
import os

def get_files(dir,suffix):
    res = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root,filename))
    print(res)

get_files("./",'.pyc')
```

第二种方法：

```python
import os

def pick(obj):
    if ob.endswith(".pyc"):
        print(obj)
    
def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)
    
if __name__=='__main__':
    path = input('输入目录')
    scan_path(path)
```

第三种方法：

```python
from glob import iglob

def func(fp, postfix):
    for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
        print(i)

if __name__ == "__main__":
    postfix = ".pyc"
    func("K:\Python_script", postfix)
```

### 44.Python遍历列表时删除元素的正确做法

a.遍历时在新列表操作，删除时在原来的列表操作：

```python
a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i>5:
        pass
    else:
        a.remove(i)
    print(a)
print(id(a))
```

b.使用filter：

```python
a=[1,2,3,4,5,6,7,8]
b = filter(lambda x: x>5,a)
print(list(b))
```

c.列表生成式：

```python
a=[1,2,3,4,5,6,7,8]
b = [i for i in a if i>5]
print(b)
```

d.倒序删除：

因为列表总是‘向前移’，所以可以倒序遍历，即使后面的元素被修改了，还没有被遍历的元素和其坐标还是保持不变的。

```python
a=[1,2,3,4,5,6,7,8]
print(id(a))
for i in range(len(a)-1,-1,-1):
    if a[i]>5:
        pass
    else:
        a.remove(a[i])
print(id(a))
print(a)
```

### 45.字符串 `"123"` 转换成 `123`，不使用内置api，例如 `int()`

方法一： 利用 `str` 函数

```python
def atoi(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num
```

方法二： 利用 `ord` 函数

```python
def atoi(s):
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord('0')
    return num
```

方法三: 利用 `eval` 函数

```python
def atoi(s):
    num = 0
    for v in s:
        t = "%s * 1" % v
        n = eval(t)
        num = num * 10 + n
    return num
```

方法四: 结合方法二，使用 `reduce`，一行解决

```python
from functools import reduce

def atoi(s):
    return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s, 0)
```
  
### 46.统计一个文本中单词频次最高的10个单词

```python
# 方法一
import re

def test(filepath):
    distone = {}

    with open(filepath) as f:
        for line in f:
            line = re.sub("\W+", " ", line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1

    num_ten = sorted(distone.items(), key=lambda x:x[1], reverse=True)[:10]
    num_ten =[x[0] for x in num_ten]
    return num_ten
 
# 方法二 
# 使用 built-in 的 Counter 里面的 most_common
import re
from collections import Counter

def test2(filepath):
    with open(filepath) as f:
        return list(map(lambda c: c[0], Counter(re.sub("\W+", " ", f.read()).split()).most_common(10)))
```

### 47.阅读一下代码他们的输出结果是什么？

```python
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(3) for m in multi()])
```

正确答案是[9,9,9,9]，而不是[0,3,6,9]产生的原因是Python的闭包的后期绑定导致的，这意味着在闭包中的变量是在内部函数被调用的时候被查找的，因为，最后函数被调用的时候，for循环已经完成, i 的值最后是3,因此每一个返回值的i都是3,所以最后的结果是[9,9,9,9]

你如何修改上面的multipliers的定义产生想要的结果？

上述问题产生的原因是python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内进行查找。因此，当任何由multipliers()返回的函数被调用时,i的值将在附近的范围进行查找。那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3.

```python
def multipliers():
    for i in range(4):
        yield lambda x: i *x
```

```python
def multipliers():
    return [lambda x,i = i: i*x for i in range(4)]
```

# Python高级

## 元类

### 48.介绍Cython，Pypy Cpython Numba各有什么缺点
### 49.请描述抽象类和接口类的区别和联系
### 50.Python中如何动态获取和设置对象的属性

## 内存管理与垃圾回收机制

### 51.哪些操作会导致Python内存溢出，怎么处理

### 52.内存泄露是什么？如何避免？

**内存泄漏**指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。

有`__del__()`函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。

通过 Python 扩展模块 gc 来查看不能回收的对象的详细信息。

可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露。

## 函数

### 53.手写一个判断时间的装饰器

```python
import datetime


class TimeException(Exception):
    def __init__(self, exception_info):
        super().__init__()
        self.info = exception_info

    def __str__(self):
        return self.info


def timecheck(func):
    def wrapper(*args, **kwargs):
        if datetime.datetime.now().year == 2019:
            func(*args, **kwargs)
        else:
            raise TimeException("函数已过时")

    return wrapper


@timecheck
def test(name):
    print("Hello {}, 2019 Happy".format(name))


if __name__ == "__main__":
    test("backbp")
```

### 54.带参数的装饰器

a.带定长参数的装饰器：

```python
def new_func(func):
    def wrappedfun(username, passwd):
        if username == 'root' and passwd == '123456789':
            print('通过认证')
            print('开始执行附加功能')
            return func()
       	else:
            print('用户名或密码错误')
            return
    return wrappedfun

@new_func
def origin():
    print('开始执行函数')
origin('root','123456789')
```

b.带不定长参数的装饰器：

```python
def new_func(func):
    def wrappedfun(*parts):
        if parts:
            counts = len(parts)
            print('本系统包含 ', end='')
            for part in parts:
                print(part, ' ',end='')
            print('等', counts, '部分')
            return func()
        else:
            print('用户名或密码错误')
            return func()
   return wrappedfun
```

### 55.线程安全的装饰器

### 56.交换两个变量的值

```python
a, b = b, a
```

### 57.hasattr() getattr() setattr() 函数使用详解

hasattr(object,name)函数:

判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否则返回False。

```python
class function_demo(object):
    name = 'demo'
    def run(self):
        return "hello function"
functiondemo = function_demo()
res = hasattr(functiondemo, "name") # 判断对象是否有name属性，True
res = hasattr(functiondemo, "run") # 判断对象是否有run方法，True
res = hasattr(functiondemo, "age") # 判断对象是否有age属性，False
print(res)
```

getattr(object, name[,default])函数：

获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面添加括号().

```python
functiondemo = function_demo()
getattr(functiondemo, "name")# 获取name属性，存在就打印出来 --- demo
getattr(functiondemo, "run") # 获取run 方法，存在打印出方法的内存地址
getattr(functiondemo, "age") # 获取不存在的属性，报错
getattr(functiondemo, "age", 18)# 获取不存在的属性，返回一个默认值
```

setattr(object, name, values)函数：

给对象的属性赋值，若属性不存在，先创建再赋值

```python
class function_demo(object):
    name = "demo"
    def run(self):
        return "hello function"
functiondemo = function_demo()
res = hasattr(functiondemo, "age") # 判断age属性是否存在，False
print(res)
setattr(functiondemo, "age", 18) # 对age属性进行赋值，无返回值
res1 = hasattr(functiondemo, "age") # 再次判断属性是否存在，True
```

综合使用

```python
class function_demo(object):
    name = "demo"
    def run(self):
        return "hello function"

functiondemo = function_demo()
res = hasattr(functiondemo, "addr") # 先判断是否存在
if res:
    addr = getattr(functiondemo, "addr")
    print(addr)
else:
    addr = getattr(functiondemo, "addr", setattr(functiondemo, "addr", "北京首都"))
    print(addr)
```

##  设计模式

### 58.对装饰器的理解，并写出一个计时器记录方法执行性能的装饰器
装饰器本质上是一个callable object，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。

```python
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.clock()
        ret = func(*args, **kwargs)
        end = time.clock()
        print('used:',end-start)
        return ret
    
    return wrapper

@timeit
def foo():
    print('in foo()'foo())
```

### 59.Python中yield的用法

yield就是保存当前程序执行状态。你用for循环的时候，每次取一个元素的时候就会计算一次。用yield的函数叫generator,和iterator一样，它的好处是不用一次计算所有元素，而是用一次算一次，可以节省很多空间，generator每次计算需要上一次计算结果，所以用yield,否则一return，上次计算结果就没了

## 面向对象

### 60.Python的魔法方法

魔法方法就是可以给你的类增加魔力的特殊方法，如果你的对象实现（重载）了这些方法中的某一个，那么这个方法就会在特殊的情况下被Python所调用，你可以定义自己想要的行为，而这一切都是自动发生的，它们经常是两个下划线包围来命名的（比如`__init___`,`__len__`),Python的魔法方法是非常强大的所以了解其使用方法也变得尤为重要!

`__init__`构造器，当一个实例被创建的时候初始化的方法，但是它并不是实例化调用的第一个方法。

`__new__`才是实例化对象调用的第一个方法，它只取下cls参数，并把其他参数传给`__init___`.

`___new__`很少使用，但是也有它适合的场景，尤其是当类继承自一个像元祖或者字符串这样不经常改变的类型的时候。

`__call__`让一个类的实例像函数一样被调用

`__getitem__`定义获取容器中指定元素的行为，相当于self[key]

`__getattr__`定义当用户试图访问一个不存在属性的时候的行为。

`__setattr__`定义当一个属性被设置的时候的行为

`__getattribute___`定义当一个属性被访问的时候的行为

### 61.面向对象中怎么实现只读属性

将对象私有化，通过共有方法提供一个读取数据的接口

```python
class person:
    def __init__(self, x):
        self.__age = 10
    def age(self):
        return self.__age
t = person(22)
# t.__age =100
print(t.age())
```

最好的方法

```python
class MyCls(object):
    __weight = 50
    
    @property
    def weight(self):
        return self.__weight
```

### 62.谈谈你对面向对象的理解

面向对象是相当于面向过程而言的，面向过程语言是一种基于功能分析的，以算法为中心的程序设计方法，而面向对象是一种基于结构分析的，以数据为中心的程序设计思想。在面向对象语言中有一个很重要的东西，叫做类。面向对象有三大特性：封装、继承、多态。

## 正则表达式

### 63.请写出一段代码用正则匹配出ip

```python
def ip_match(ip_str):
    partterns = re.compile(r"(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}")
    print(partterns.search(ip_str).group(0))
```

### 64.Python字符串查找和替换？
### 65.正则表达式贪婪与非贪婪模式的区别？
### 66.写出开头匹配字母和下划线，末尾是数字的正则表达式？
### 67.怎么过滤评论中的表情？
### 68.Python里match与search的区别？

match 方法用于查找字符串的头部（也可以指定起始位置），它是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果。它的一般使用形式如下：

match(string[, pos[, endpos]])
其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。因此，**当你不指定 pos 和 endpos 时，match 方法默认匹配字符串的头部**。

当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。

```python
>>> import re
>>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
>>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
>>> print m                                         # 返回一个 Match 对象
<_sre.SRE_Match object at 0x10a42aac0>
>>> m.group(0)   # 可省略 0
'12'
>>> m.start(0)   # 可省略 0
3
>>> m.end(0)     # 可省略 0
5
>>> m.span(0)    # 可省略 0
(3, 5)
```

search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，它的一般使用形式如下：

search(string[, pos[, endpos]])
其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。

当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。

```python
>>> import re
>>> pattern = re.compile('\d+')
>>> m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配
>>> m
<_sre.SRE_Match object at 0x10cc03ac0>
>>> m.group()
'12'
>>> m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
>>> m
<_sre.SRE_Match object at 0x10cc03b28>
>>> m.group()
'34'
>>> m.span()
(13, 15)
```

# Web
## Flask
### 140.对Flask蓝图(Blueprint)的理解？

蓝图的定义：

蓝图 Blueprint 是Flask应用程序组件化的方法，可以在一个应用内或跨越多个项目共用蓝图。使用蓝图可以极大简化大型应用的开发难度，也为Flask扩展提供了一种在应用中注册服务的集中式机制。

蓝图的应用场景：

把一个应用分解为一个蓝图的集合。这对大型应用是理想的。一个项目可以实例化一个应用对象，初始化几个扩展，并注册一集合的蓝图。

以URL前缀和/或子域名，在应用上注册一个蓝图。URL前缀/子域名中的参数即成为这个蓝图下的所有视图函数的共同的视图参数（默认情况下）
在一个应用中用不同的URL规则多次注册一个蓝图。

通过蓝图提供模板过滤器、静态文件、模板和其他功能。一个蓝图不一定要实现应用或视图函数。

初始化一个Flask扩展时，在这些情况中注册一个蓝图。

蓝图的缺点：

不能在应用创建后撤销注册一个蓝图而不销毁整个应用对象。

使用蓝图的三个步骤：

1.创建一个蓝图对象

```python
blue = Blueprint("blue",__name__)
```

2.在这个蓝图对象上进行操作，例如注册路由、指定静态文件夹、注册模板过滤器...

```python
@blue.route('/')
def blue_index():
    return "Welcome to my blueprint"
```

3.在应用对象上注册这个蓝图对象

```python
app.register_blueprint(blue,url_prefix="/blue")
```

### 141.Flask 和 Django 路由映射的区别？

在django中，路由是浏览器访问服务器时，先访问的项目中的url，再由项目中的url找到应用中url，这些url是放在一个列表里，遵从从前往后匹配的规则。在flask中，路由是通过装饰器给每个视图函数提供的，而且根据请求方式的不同可以一个url用于不同的作用。

## Django
### 142.什么是wsgi,uwsgi,uWSGI?

WSGI:

web服务器网关接口，是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架。

实现wsgi协议的模块：wsgiref，本质上就是编写一socket服务端，用于接收用户请求（django)

werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)

uwsgi：与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议，用于定义传输信息的类型。

uWSGI：是一个web服务器，实现了WSGI的协议，uWSGI协议，http协议。

### 143.Django、Flask、Tornado的对比？

1、Django走的大而全的方向，开发效率高。它的MTV框架，自带的ORM，admin后台管理，自带的sqlite数据库和开发测试用的服务器，给开发者提高了超高的开发效率。

重量级web框架，功能齐全，提供一站式解决的思路，能让开发者不用在选择上花费大量时间。

自带ORM和模板引擎，支持jinja等非官方模板引擎。

自带ORM使Django和关系型数据库耦合度高，如果要使用非关系型数据库，需要使用第三方库。

自带数据库管理app

成熟，稳定，开发效率高，相对于Flask，Django的整体封闭性比较好，适合做企业级网站的开发。python web框架的先驱，第三方库丰富。

2、Flask 是轻量级的框架，自由，灵活，可扩展性强，核心基于Werkzeug WSGI工具 和jinja2 模板引擎

适用于做小网站以及web服务的API,开发大型网站无压力，但架构需要自己设计

与关系型数据库的结合不弱于Django，而与非关系型数据库的结合远远优于Django

3、Tornado走的是少而精的方向，性能优越，它最出名的异步非阻塞的设计方式

Tornado的两大核心模块：

iostraem：对非阻塞的socket进行简单的封装

ioloop：对I/O 多路复用的封装,它实现一个单例

### 144.CORS 和 CSRF的区别？

什么是CORS？

CORS是一个W3C标准，全称是“跨域资源共享"(Cross-origin resoure sharing)。
它允许浏览器向跨源服务器，发出XMLHttpRequest请求，从而客服了AJAX只能同源使用的限制。

什么是CSRF？

CSRF主流防御方式是在后端生成表单的时候生成一串随机token，内置到表单里成为一个字段，同时，将此串token置入session中。每次表单提交到后端时都会检查这两个值是否一致，以此来判断此次表单提交是否是可信的，提交过一次之后，如果这个页面没有生成CSRF token,那么token将会被清空,如果有新的需求，那么token会被更新。

攻击者可以伪造POST表单提交，但是他没有后端生成的内置于表单的token，session中没有token都无济于事。

### 145.Session,Cookie,JWT的理解

为什么要使用会话管理

众所周知，HTTP协议是一个无状态的协议，也就是说每个请求都是一个独立的请求，请求与请求之间并无关系。但在实际的应用场景，这种方式并不能满足我们的需求。举个大家都喜欢用的例子，把商品加入购物车，单独考虑这个请求，服务端并不知道这个商品是谁的，应该加入谁的购物车？因此这个请求的上下文环境实际上应该包含用户的相关信息，在每次用户发出请求时把这一小部分额外信息，也做为请求的一部分，这样服务端就可以根据上下文中的信息，针对具体的用户进行操作。所以这几种技术的出现都是对HTTP协议的一个补充，使得我们可以用HTTP协议+状态管理构建一个的面向用户的WEB应用。

Session 和 Cookie 的区别：

这里我想先谈谈session与cookies,因为这两个技术是做为开发最为常见的。那么session与cookies的区别是什么？个人认为session与cookies最核心区别在于额外信息由谁来维护。利用cookies来实现会话管理时，用户的相关信息或者其他我们想要保持在每个请求中的信息，都是放在cookies中,而cookies是由客户端来保存，每当客户端发出新请求时，就会稍带上cookies,服务端会根据其中的信息进行操作。

当利用session来进行会话管理时，客户端实际上只存了一个由服务端发送的session_id,而由这个session_id,可以在服务端还原出所需要的所有状态信息，从这里可以看出这部分信息是由服务端来维护的。

除此以外，session与cookies都有一些自己的缺点：
    
cookies的安全性不好，攻击者可以通过获取本地cookies进行欺骗或者利用cookies进行CSRF攻击。使用cookies时,在多个域名下，会存在跨域问题。

session 在一定的时间里，需要存放在服务端，因此当拥有大量用户时，也会大幅度降低服务端的性能，当有多台机器时，如何共享session也会是一个问题.(redis集群)也就是说，用户第一个访问的时候是服务器A，而第二个请求被转发给了服务器B，那服务器B如何得知其状态。实际上，session与cookies是有联系的，比如我们可以把session_id存放在cookies中的。

JWT是如何工作的

首先用户发出登录请求，服务端根据用户的登录请求进行匹配，如果匹配成功，将相关的信息放入payload中，利用算法，加上服务端的密钥生成token，这里需要注意的是secret_key很重要，如果这个泄露的话，客户端就可以随机篡改发送的额外信息，它是信息完整性的保证。生成token后服务端将其返回给客户端，客户端可以在下次请求时，将token一起交给服务端，一般是说我们可以将其放在Authorization首部中，这样也就可以避免跨域问题。

### 146.简述Django请求生命周期

一般是用户通过浏览器向我们的服务器发起一个请求(request),这个请求会去访问视图函数，如果不涉及到数据调用，那么这个时候视图函数返回一个模板也就是一个网页给用户）

视图函数调用模型毛模型去数据库查找数据，然后逐级返回，视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。

1.wsgi ,请求封装后交给web框架（Flask，Django)

2.中间件，对请求进行校验或在请求对象中添加其他相关数据，例如：csrf,request.session

3.路由匹配 根据浏览器发送的不同url去匹配不同的视图函数

4.视图函数，在视图函数中进行业务逻辑的处理，可能涉及到：orm，templates 

5.中间件，对响应的数据进行处理

6.wsgi，将响应的内容发送给浏览器

### 147.用的restframework完成api发送时间时区

当前的问题是用django的rest framework模块做一个get请求的发送时间以及时区信息的api

```python
class getCurrenttime(APIView):
    def get(self,request):
        local_time = time.localtime()
        time_zone =settings.TIME_ZONE
        temp = {'localtime':local_time,'timezone':time_zone}
        return Response(temp)
```

### 148.nginx,tomcat,apach到都是什么？

Nginx（engine x)是一个高性能的HTTP和反向代理服务器，也是 一个IMAP/POP3/SMTP服务器，工作在OSI七层，负载的实现方式：轮询，IP_HASH,fair,session_sticky。

Apache HTTP Server是一个模块化的服务器，源于NCSAhttpd服务器。

Tomcat 服务器是一个免费的开放源代码的Web应用服务器，属于轻量级应用服务器，是开发和调试JSP程序的首选。

### 149.请给出你熟悉关系数据库范式有哪些，有什么作用？

在进行数据库的设计时，所遵循的一些规范，只要按照设计规范进行设计，就能设计出没有数据冗余和数据维护异常的数据库结构。

数据库的设计的规范有很多，通常来说我们在设是数据库时只要达到其中一些规范就可以了，这些规范又称之为数据库的三范式，一共有三条，也存在着其他范式，我们只要做到满足前三个范式的要求，就能设陈出符合我们的数据库了，我们也不能全部来按照范式的要求来做，还要考虑实际的业务使用情况，所以有时候也需要做一些违反范式的要求。

1.数据库设计的第一范式(最基本)，基本上所有数据库的范式都是符合第一范式的，符合第一范式的表具有以下几个特点：

数据库表中的所有字段都只具有单一属性，单一属性的列是由基本的数据类型（整型，浮点型，字符型等）所构成的设计出来的表都是简单的二比表

2.数据库设计的第二范式(是在第一范式的基础上设计的)，要求一个表中只具有一个业务主键，也就是说符合第二范式的表中不能存在非主键列对只对部分主键的依赖关系

3.数据库设计的第三范式，指每一个非主属性既不部分依赖与也不传递依赖于业务主键，也就是第二范式的基础上消除了非主属性对主键的传递依赖

### 150.简述QQ登陆过程

qq登录，在我们的项目中分为了三个接口，

第一个接口是请求qq服务器返回一个qq登录的界面;

第二个接口是通过扫码或账号登陆进行验证，qq服务器返回给浏览器一个code和state,利用这个code通过本地服务器去向qq服务器获取access_token覆返回给本地服务器，凭借access_token再向qq服务器获取用户的openid(openid用户的唯一标识)

第三个接口是判断用户是否是第一次qq登录，如果不是的话直接登录返回的jwt-token给用户，对没有绑定过本网站的用户，对openid进行加密生成token进行绑定

### 151.post 和 get的区别?

1.GET是从服务器上获取数据，POST是向服务器传送数据

2.在客户端，GET方式在通过URL提交数据，数据在URL中可以看到，POST方式，数据放置在HTML——HEADER内提交

3.对于GET方式，服务器端用Request.QueryString获取变量的值，对于POST方式，服务器端用Request.Form获取提交的数据

### 152.项目中日志的作用

一、日志相关概念

1.日志是一种可以追踪某些软件运行时所发生事件的方法

2.软件开发人员可以向他们的代码中调用日志记录相关的方法来表明发生了某些事情

3.一个事件可以用一个包含可选变量数据的消息来描述

4.此外，事件也有重要性的概念，这个重要性也可以被成为严重性级别(level)

二、日志的作用

1.通过log的分析，可以方便用户了解系统或软件、应用的运行情况;

2.如果你的应用log足够丰富，可以分析以往用户的操作行为、类型喜好，地域分布或其他更多信息;

3.如果一个应用的log同时也分了多个级别，那么可以很轻易地分析得到该应用的健康状况，及时发现问题并快速定位、解决问题，补救损失。

4.简单来讲就是我们通过记录和分析日志可以了解一个系统或软件程序运行情况是否正常，也可以在应用程序出现故障时快速定位问题。不仅在开发中，在运维中日志也很重要，日志的作用也可以简单。总结为以下几点：

1.程序调试

2.了解软件程序运行情况，是否正常

3,软件程序运行故障分析与问题定位

4,如果应用的日志信息足够详细和丰富，还可以用来做用户行为分析

### 153.django中间件的使用？

Django在中间件中预置了六个方法，这六个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

1.初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件

```python
def __init__():
    pass
```

2.处理请求前：在每个请求上调用，返回None或HttpResponse对象。

```python
def process_request(request):
    pass
```

3.处理视图前:在每个请求上调用，返回None或HttpResponse对象。

```python
def process_view(request,view_func,view_args,view_kwargs):
    pass
```

4.处理模板响应前：在每个请求上调用，返回实现了render方法的响应对象。

```python
def process_template_response(request,response):
    pass
```

5.处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。

```python
def process_response(request,response):
    pass
```

6.异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。

```python
def process_exception(request,exception):
    pass
```

### 154.谈一下你对uWSGI和nginx的理解？

1.uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。WSGI是一种Web服务器网关接口。它是一个Web服务器（如nginx，uWSGI等服务器）与web应用（如用Flask框架写的程序）通信的一种规范。

要注意WSGI/uwsgi/uWSGI这三个概念的区分。

WSGI是一种通信协议。

uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。

uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

nginx 是一个开源的高性能的HTTP服务器和反向代理：

1.作为web服务器，它处理静态文件和索引文件效果非常高

2.它的设计非常注重效率，最大支持5万个并发连接，但只占用很少的内存空间

3.稳定性高，配置简洁。

4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用

### 155.Django中哪里用到了线程？哪里用到了协程？哪里用到了进程？

1.Django中耗时的任务用一个进程或者线程来执行，比如发邮件，使用celery.

2.部署django项目是时候，配置文件中设置了进程和协程的相关配置。

### 156.有用过Django REST framework吗？

Django REST framework是一个强大而灵活的Web API工具。使用RESTframework的理由有：

Web browsable API对开发者有极大的好处

包括OAuth1a和OAuth2的认证策略

支持ORM和非ORM数据资源的序列化

全程自定义开发--如果不想使用更加强大的功能，可仅仅使用常规的function-based views额外的文档和强大的社区支持


## 爬虫
### 159.试列出至少三种目前流行的大型数据库
### 160.列举您使用过的Python网络爬虫所用到的网络数据包?
### 161.爬取数据后使用哪个数据库存储数据的，为什么？
### 162.你用过的爬虫框架或者模块有哪些？优缺点？
### 163.写爬虫是用多进程好？还是多线程好？
### 164.常见的反爬虫和应对方法？
### 165.解析网页的解析器使用最多的是哪几个?
### 166.需要登录的网页，如何解决同时限制ip，cookie,session
### 167.验证码的解决?
### 168.使用最多的数据库，对他们的理解？
### 169.编写过哪些爬虫中间件？
### 170.“极验”滑动验证码如何破解？
### 171.爬虫多久爬一次，爬下来的数据是怎么存储？
### 172.cookie过期的处理问题？
### 173.动态加载又对及时性要求很高怎么处理？
### 174.HTTPS有什么优点和缺点？
### 175.HTTPS是如何实现安全传输数据的？
### 176.TTL，MSL，RTT各是什么？
### 177.谈一谈你对Selenium和PhantomJS了解
### 178.平常怎么使用代理的 ？
### 179.存放在数据库(redis、mysql等)。
### 180.怎么监控爬虫的状态?
### 181.描述下scrapy框架运行的机制？
### 182.谈谈你对Scrapy的理解？
### 183.怎么样让 scrapy 框架发送一个 post 请求（具体写出来）
### 184.怎么监控爬虫的状态 ？
### 185.怎么判断网站是否更新？
### 186.图片、视频爬取怎么绕过防盗连接
### 187.你爬出来的数据量大概有多大？大概多长时间爬一次？
### 188.用什么数据库存爬下来的数据？部署是你做的吗？怎么部署？
### 189.增量爬取
### 190.爬取下来的数据如何去重，说一下scrapy的具体的算法依据。
### 191.Scrapy的优缺点?
### 192.怎么设置爬取深度？
### 193.scrapy和scrapy-redis有什么区别？为什么选择redis数据库？
### 194.分布式爬虫主要解决什么问题？
### 195.什么是分布式存储？
### 196.你所知道的分布式爬虫方案有哪些？
### 197.scrapy-redis，有做过其他的分布式爬虫吗？

## 测试
### 213.编写测试计划的目的是
### 214.对关键词触发模块进行测试
### 215.其他常用笔试题目网址汇总
### 216.测试人员在软件开发过程中的任务是什么
### 217.一条软件Bug记录都包含了哪些内容？
### 218.简述黑盒测试和白盒测试的优缺点
### 219.请列出你所知道的软件测试种类，至少5项
### 220.Alpha测试与Beta测试的区别是什么？
### 221.举例说明什么是Bug？一个bug report应包含什么关键字？

## 大数据
### 242.找出1G的文件中高频词
### 243.一个大约有一万行的文本文件统计高频词
### 244.怎么在海量数据中找出重复次数最多的一个？
### 245.判断数据是否在大量数据中

## 架构

### [Python后端架构演进](<https://zhu327.github.io/2018/07/19/python%E5%90%8E%E7%AB%AF%E6%9E%B6%E6%9E%84%E6%BC%94%E8%BF%9B/>)

这篇文章几乎涵盖了python会用的架构，在面试可以手画架构图，根据自己的项目谈下技术选型和优劣，遇到的坑等。绝对加分