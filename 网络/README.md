<!-- TOC -->

- [网络编程](#%e7%bd%91%e7%bb%9c%e7%bc%96%e7%a8%8b)
  - [1.三次握手和四次挥手](#1%e4%b8%89%e6%ac%a1%e6%8f%a1%e6%89%8b%e5%92%8c%e5%9b%9b%e6%ac%a1%e6%8c%a5%e6%89%8b)
  - [2.ARP协议](#2arp%e5%8d%8f%e8%ae%ae)
  - [3.urllib和urllib2的区别](#3urllib%e5%92%8curllib2%e7%9a%84%e5%8c%ba%e5%88%ab)
  - [4.Post和Get](#4post%e5%92%8cget)
  - [5.Cookie和Session](#5cookie%e5%92%8csession)
  - [6.apache和nginx的区别](#6apache%e5%92%8cnginx%e7%9a%84%e5%8c%ba%e5%88%ab)
  - [7.网站用户密码保存](#7%e7%bd%91%e7%ab%99%e7%94%a8%e6%88%b7%e5%af%86%e7%a0%81%e4%bf%9d%e5%ad%98)
  - [8.HTTP和HTTPS](#8http%e5%92%8chttps)
  - [9.CSRF和XSS](#9csrf%e5%92%8cxss)
  - [10.幂等 Idempotence](#10%e5%b9%82%e7%ad%89-idempotence)
  - [11.RESTful架构(SOAP,RPC)](#11restful%e6%9e%b6%e6%9e%84soaprpc)
  - [12.SOAP](#12soap)
  - [13.RPC](#13rpc)
  - [14.CGI和WSGI](#14cgi%e5%92%8cwsgi)
  - [15.中间人攻击](#15%e4%b8%ad%e9%97%b4%e4%ba%ba%e6%94%bb%e5%87%bb)
  - [16.c10k问题](#16c10k%e9%97%ae%e9%a2%98)
  - [17.socket](#17socket)
  - [18.浏览器缓存](#18%e6%b5%8f%e8%a7%88%e5%99%a8%e7%bc%93%e5%ad%98)
  - [19.HTTP1.0和HTTP1.1](#19http10%e5%92%8chttp11)
  - [20.Ajax](#20ajax)
  - [21.怎么实现强行关闭客户端和服务器之间的连接?](#21%e6%80%8e%e4%b9%88%e5%ae%9e%e7%8e%b0%e5%bc%ba%e8%a1%8c%e5%85%b3%e9%97%ad%e5%ae%a2%e6%88%b7%e7%ab%af%e5%92%8c%e6%9c%8d%e5%8a%a1%e5%99%a8%e4%b9%8b%e9%97%b4%e7%9a%84%e8%bf%9e%e6%8e%a5)
  - [22.简述TCP和UDP的区别以及优缺点?](#22%e7%ae%80%e8%bf%b0tcp%e5%92%8cudp%e7%9a%84%e5%8c%ba%e5%88%ab%e4%bb%a5%e5%8f%8a%e4%bc%98%e7%bc%ba%e7%82%b9)
  - [23.简述浏览器通过WSGI请求动态资源的过程?](#23%e7%ae%80%e8%bf%b0%e6%b5%8f%e8%a7%88%e5%99%a8%e9%80%9a%e8%bf%87wsgi%e8%af%b7%e6%b1%82%e5%8a%a8%e6%80%81%e8%b5%84%e6%ba%90%e7%9a%84%e8%bf%87%e7%a8%8b)
  - [24.描述用浏览器访问www.baidu.com的过程](#24%e6%8f%8f%e8%bf%b0%e7%94%a8%e6%b5%8f%e8%a7%88%e5%99%a8%e8%ae%bf%e9%97%aewwwbaiducom%e7%9a%84%e8%bf%87%e7%a8%8b)
  - [25.列出你知道的HTTP协议的状态码，说出表示什么意思？](#25%e5%88%97%e5%87%ba%e4%bd%a0%e7%9f%a5%e9%81%93%e7%9a%84http%e5%8d%8f%e8%ae%ae%e7%9a%84%e7%8a%b6%e6%80%81%e7%a0%81%e8%af%b4%e5%87%ba%e8%a1%a8%e7%a4%ba%e4%bb%80%e4%b9%88%e6%84%8f%e6%80%9d)
  - [26.说一下什么是tcp的2MSL？](#26%e8%af%b4%e4%b8%80%e4%b8%8b%e4%bb%80%e4%b9%88%e6%98%aftcp%e7%9a%842msl)
  - [27.为什么客户端在TIME-WAIT状态必须等待2MSL的时间？](#27%e4%b8%ba%e4%bb%80%e4%b9%88%e5%ae%a2%e6%88%b7%e7%ab%af%e5%9c%a8time-wait%e7%8a%b6%e6%80%81%e5%bf%85%e9%a1%bb%e7%ad%89%e5%be%852msl%e7%9a%84%e6%97%b6%e9%97%b4)
  - [28.谈一下HTTP协议以及协议头部中表示数据类型的字段？](#28%e8%b0%88%e4%b8%80%e4%b8%8bhttp%e5%8d%8f%e8%ae%ae%e4%bb%a5%e5%8f%8a%e5%8d%8f%e8%ae%ae%e5%a4%b4%e9%83%a8%e4%b8%ad%e8%a1%a8%e7%a4%ba%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b%e7%9a%84%e5%ad%97%e6%ae%b5)
  - [29.使用Socket套接字需要传入哪些参数 ？](#29%e4%bd%bf%e7%94%a8socket%e5%a5%97%e6%8e%a5%e5%ad%97%e9%9c%80%e8%a6%81%e4%bc%a0%e5%85%a5%e5%93%aa%e4%ba%9b%e5%8f%82%e6%95%b0)
  - [30.HTTP常见请求头？](#30http%e5%b8%b8%e8%a7%81%e8%af%b7%e6%b1%82%e5%a4%b4)
  - [31.七层模型？](#31%e4%b8%83%e5%b1%82%e6%a8%a1%e5%9e%8b)
  - [32.url的形式？](#32url%e7%9a%84%e5%bd%a2%e5%bc%8f)

<!-- /TOC -->

## 网络编程
### 1.三次握手和四次挥手

三次握手：

1. 客户端通过向服务器端发送一个SYN来创建一个主动打开，作为三次握手的一部分。客户端把这段连接的序号设定为随机数 A。
2. 服务器端应当为一个合法的SYN回送一个SYN/ACK。ACK 的确认码应为 A+1，SYN/ACK 包本身又有一个随机序号 B。
3. 最后，客户端再发送一个ACK。当服务端受到这个ACK的时候，就完成了三路握手，并进入了连接创建状态。此时包序号被设定为收到的确认号 A+1，而响应则为 B+1。

四次挥手：

注意: 中断连接端可以是客户端，也可以是服务器端。下面仅以客户端断开连接举例，反之亦然：

1. 客户端发送一个数据分段, 其中的 FIN 标记设置为1. 客户端进入 FIN-WAIT 状态. 该状态下客户端只接收数据, 不再发送数据.
2. 服务器接收到带有 FIN = 1 的数据分段, 发送带有 ACK = 1 的剩余数据分段, 确认收到客户端发来的 FIN 信息.
3. 服务器等到所有数据传输结束, 向客户端发送一个带有 FIN = 1 的数据分段, 并进入 CLOSE-WAIT 状态, 等待客户端发来带有 ACK = 1 的确认报文.
4. 客户端收到服务器发来带有 FIN = 1 的报文, 返回 ACK = 1 的报文确认, 为了防止服务器端未收到需要重发, 进入 TIME-WAIT 状态. 服务器接收到报文后关闭连接. 客户端等待 2MSL 后未收到回复, 则认为服务器成功关闭, 客户端关闭连接.

图解: http://blog.csdn.net/whuslei/article/details/6667471

### 2.ARP协议

地址解析协议(Address Resolution Protocol)，其基本功能为透过目标设备的IP地址，查询目标的MAC地址，以保证通信的顺利进行。它是IPv4网络层必不可少的协议，不过在IPv6中已不再适用，并被邻居发现协议（NDP）所替代。

### 3.urllib和urllib2的区别

这个面试官确实问过，当时答的urllib2可以Post而urllib不可以。

1. urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。
2. urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。这意味着，你不可以伪装你的User Agent字符串等。

### 4.Post和Get

[GET和POST有什么区别？及为什么网上的多数答案都是错的](http://www.cnblogs.com/nankezhishi/archive/2012/06/09/getandpost.html)

[知乎回答](https://www.zhihu.com/question/31640769?rf=37401322)

get: [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](http://tools.ietf.org/html/rfc2616#section-9.3)
post: [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](http://tools.ietf.org/html/rfc2616#section-9.5)

### 5.Cookie和Session

|          | Cookie                                               | Session  |
| :------- | :--------------------------------------------------- | :------- |
| 储存位置 | 客户端                                               | 服务器端 |
| 目的     | 跟踪会话，也可以保存用户偏好设置或者保存用户名密码等 | 跟踪会话 |
| 安全性   | 不安全                                               | 安全     |

session技术是要使用到cookie的，之所以出现session技术，主要是为了安全。

### 6.apache和nginx的区别

nginx 相对 apache 的优点：

- 轻量级，同样起 web 服务，比 apache 占用更少的内存及资源
- 抗并发，nginx 处理请求是异步非阻塞的，支持更多的并发连接，而 apache 则是阻塞型的，在高并发下 nginx 能保持低资源低消耗高性能
- 配置简洁
- 高度模块化的设计，编写模块相对简单
- 社区活跃

apache 相对 nginx 的优点：

- rewrite ，比 nginx 的 rewrite 强大
- 模块超多，基本想到的都可以找到
- 少 bug ，nginx 的 bug 相对较多
- 超稳定

### 7.网站用户密码保存

1. 明文保存
2. 明文hash后保存,如md5
3. MD5+Salt方式,这个salt可以随机
4. 知乎使用了Bcrypy(好像)加密

### 8.HTTP和HTTPS

| 状态码         | 定义                            |
| :------------- | :------------------------------ |
| 1xx 报告       | 接收到请求，继续进程            |
| 2xx 成功       | 步骤成功接收，被理解，并被接受  |
| 3xx 重定向     | 为了完成请求,必须采取进一步措施 |
| 4xx 客户端出错 | 请求包括错的顺序或不能完成      |
| 5xx 服务器出错 | 服务器无法完成显然有效的请求    |

403: Forbidden
404: Not Found

HTTPS握手,对称加密,非对称加密,TLS/SSL,RSA

### 9.CSRF和XSS

- CSRF(Cross-site request forgery)跨站请求伪造
- XSS(Cross Site Scripting)跨站脚本攻击

CSRF 重点在请求，XSS 重点在脚本。

### 10.幂等 Idempotence

HTTP方法的幂等性是指一次和多次请求某一个资源应该具有同样的**副作用**。(注意是副作用)

`GET http://www.bank.com/account/123456`，不会改变资源的状态，不论调用一次还是N次都没有副作用。请注意，这里强调的是一次和N次具有相同的副作用，而不是每次GET的结果相同。`GET http://www.news.com/latest-news`这个HTTP请求可能会每次得到不同的结果，但它本身并没有产生任何副作用，因而是满足幂等性的。

DELETE方法用于删除资源，有副作用，但它应该满足幂等性。比如：`DELETE http://www.forum.com/article/4231`，调用一次和N次对系统产生的副作用是相同的，即删掉id为4231的帖子；因此，调用者可以多次调用或刷新页面而不必担心引起错误。

POST所对应的URI并非创建的资源本身，而是资源的接收者。比如：`POST http://www.forum.com/articles`的语义是在`http://www.forum.com/articles`下创建一篇帖子，HTTP响应中应包含帖子的创建状态以及帖子的URI。两次相同的POST请求会在服务器端创建两份资源，它们具有不同的URI；所以，POST方法不具备幂等性。

PUT所对应的URI是要创建或更新的资源本身。比如：`PUT http://www.forum/articles/4231`的语义是创建或更新ID为4231的帖子。对同一URI进行多次PUT的副作用和一次PUT是相同的；因此，PUT方法具有幂等性。

### 11.RESTful架构(SOAP,RPC)

推荐: http://www.ruanyifeng.com/blog/2011/09/restful.html

### 12.SOAP

SOAP（原为Simple Object Access Protocol的首字母缩写，即简单对象访问协议）是交换数据的一种协议规范，使用在计算机网络Web服务（web service）中，交换带结构信息。SOAP为了简化网页服务器（Web Server）从XML数据库中提取数据时，节省去格式化页面时间，以及不同应用程序之间按照HTTP通信协议，遵从XML格式执行资料互换，使其抽象于语言实现、平台和硬件。

### 13.RPC

RPC（Remote Procedure Call Protocol）——远程过程调用协议，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。RPC协议假定某些传输协议的存在，如TCP或UDP，为通信程序之间携带信息数据。在OSI网络通信模型中，RPC跨越了传输层和应用层。RPC使得开发包括网络分布式多程序在内的应用程序更加容易。

总结:服务提供的两大流派.传统意义以方法调用为导向通称RPC。为了企业SOA,若干厂商联合推出webservice,制定了wsdl接口定义,传输soap.当互联网时代,臃肿SOA被简化为http+xml/json.但是简化出现各种混乱。以资源为导向,任何操作无非是对资源的增删改查，于是统一的REST出现了.

进化的顺序: RPC -> SOAP -> RESTful

### 14.CGI和WSGI

CGI是通用网关接口，是连接web服务器和应用程序的接口，用户通过CGI来获取动态数据或文件等。
CGI程序是一个独立的程序，它可以用几乎所有语言来写，包括perl，c，lua，python等等。

WSGI, Web Server Gateway Interface，是Python应用程序或框架和Web服务器之间的一种接口，WSGI的其中一个目的就是让用户可以用统一的语言(Python)编写前后端。

官方说明：[PEP-3333](https://www.python.org/dev/peps/pep-3333/)

### 15.中间人攻击

中间人攻击（Man-in-the-middle attack，通常缩写为MITM）是指攻击者与通讯的两端分别创建独立的联系，并交换其所收到的数据，使通讯的两端认为他们正在通过一个私密的连接与对方直接对话，但事实上整个会话都被攻击者完全控制。

### 16.c10k问题

所谓c10k问题，指的是服务器同时支持成千上万个客户端的问题，也就是concurrent 10 000 connection（这也是c10k这个名字的由来）。

推荐: https://my.oschina.net/xianggao/blog/664275

### 17.socket

推荐: http://www.360doc.com/content/11/0609/15/5482098_122692444.shtml

Socket=Ip address+ TCP/UDP + port

### 18.浏览器缓存

推荐: http://www.cnblogs.com/skynet/archive/2012/11/28/2792503.html

### 19.HTTP1.0和HTTP1.1

推荐: http://blog.csdn.net/elifefly/article/details/3964766

1. 请求头Host字段,一个服务器多个网站
2. 长链接
3. 文件断点续传
4. 身份认证,状态管理,Cache缓存

HTTP请求8种方法介绍 

HTTP/1.1协议中共定义了8种HTTP请求方法，HTTP请求方法也被叫做“请求动作”，不同的方法规定了不同的操作指定的资源方式。服务端也会根据不同的请求方法做不同的响应。

GET

GET请求会显示请求指定的资源。一般来说GET方法应该只用于数据的读取，而不应当用于会产生副作用的非幂等的操作中。

GET会方法请求指定的页面信息，并返回响应主体，GET被认为是不安全的方法，因为GET方法会被网络蜘蛛等任意的访问。

HEAD

HEAD方法与GET方法一样，都是向服务器发出指定资源的请求。但是，服务器在响应HEAD请求时不会回传资源的内容部分，即：响应主体。这样，我们可以不传输全部内容的情况下，就可以获取服务器的响应头信息。HEAD方法常被用于客户端查看服务器的性能。

POST

POST请求会 向指定资源提交数据，请求服务器进行处理，如：表单数据提交、文件上传等，请求数据会被包含在请求体中。POST方法是非幂等的方法，因为这个请求可能会创建新的资源或/和修改现有资源。

PUT

PUT请求会身向指定资源位置上传其最新内容，PUT方法是幂等的方法。通过该方法客户端可以将指定资源的最新数据传送给服务器取代指定的资源的内容。

DELETE

DELETE请求用于请求服务器删除所请求URI（统一资源标识符，Uniform Resource Identifier）所标识的资源。DELETE请求后指定资源会被删除，DELETE方法也是幂等的。

CONNECT

CONNECT方法是HTTP/1.1协议预留的，能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接与非加密的HTTP代理服务器的通信。

OPTIONS

OPTIONS请求与HEAD类似，一般也是用于客户端查看服务器的性能。 这个方法会请求服务器返回该资源所支持的所有HTTP请求方法，该方法会用’*’来代替资源名称，向服务器发送OPTIONS请求，可以测试服务器功能是否正常。JavaScript的XMLHttpRequest对象进行CORS跨域资源共享时，就是使用OPTIONS方法发送嗅探请求，以判断是否有对指定资源的访问权限。 允许

TRACE

TRACE请求服务器回显其收到的请求信息，该方法主要用于HTTP请求的测试或诊断。

HTTP/1.1之后增加的方法

在HTTP/1.1标准制定之后，又陆续扩展了一些方法。其中使用中较多的是 PATCH 方法：

PATCH

PATCH方法出现的较晚，它在2010年的RFC 5789标准中被定义。PATCH请求与PUT请求类似，同样用于资源的更新。二者有以下两点不同：

1、PATCH一般用于资源的部分更新，而PUT一般用于资源的整体更新。 

2、当资源不存在时，PATCH会创建一个新的资源，而PUT只会对已在资源进行更新。

### 20.Ajax

AJAX,Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）, 是与在不重新加载整个页面的情况下，与服务器交换数据并更新部分网页的技术。

### 21.怎么实现强行关闭客户端和服务器之间的连接?
### 22.简述TCP和UDP的区别以及优缺点?
### 23.简述浏览器通过WSGI请求动态资源的过程?

浏览器发送的请求被Nginx监听到，Nginx根据请求的URL的PATH或者后缀把请求静态资源的分发到静态资源的目录，别的请求根据配置好的转发到相应端口。

实现了WSGI的程序会监听某个端口，监听到Nginx转发过来的请求接收后(一般用socket的recv来接收HTTP的报文)以后把请求的报文封装成`environ`的字典对象，然后再提供一个`start_response`的方法。把这两个对象当成参数传入某个方法比如`wsgi_app(environ, start_response)`或者实现了`__call__(self, environ, start_response)`方法的某个实例。这个实例再调用`start_response`返回给实现了WSGI的中间件，再由中间件返回给Nginx。

### 24.描述用浏览器访问www.baidu.com的过程
### 25.列出你知道的HTTP协议的状态码，说出表示什么意思？
### 26.说一下什么是tcp的2MSL？
### 27.为什么客户端在TIME-WAIT状态必须等待2MSL的时间？
### 28.谈一下HTTP协议以及协议头部中表示数据类型的字段？
### 29.使用Socket套接字需要传入哪些参数 ？
### 30.HTTP常见请求头？
### 31.七层模型？
### 32.url的形式？
