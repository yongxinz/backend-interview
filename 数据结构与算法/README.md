<!-- TOC -->

- [数据结构](#数据结构)
    - [222.数组中出现次数超过一半的数字-Python版](#222数组中出现次数超过一半的数字-python版)
    - [223.求100以内的质数](#223求100以内的质数)
    - [224.无重复字符的最长子串-Python实现](#224无重复字符的最长子串-python实现)
    - [225.通过2个5/6升得水壶从池塘得到3升水](#225通过2个56升得水壶从池塘得到3升水)
    - [226.什么是MD5加密，有什么特点？](#226什么是md5加密有什么特点)
    - [227.什么是对称加密和非对称加密](#227什么是对称加密和非对称加密)
    - [228.冒泡排序的思想？](#228冒泡排序的思想)
    - [229.快速排序的思想？](#229快速排序的思想)
    - [230.如何判断单向链表中是否有环？](#230如何判断单向链表中是否有环)
    - [231.你知道哪些排序算法（一般是通过问题考算法）](#231你知道哪些排序算法一般是通过问题考算法)
    - [232.斐波那契数列](#232斐波那契数列)
    - [233.如何翻转一个单链表？](#233如何翻转一个单链表)
    - [234.青蛙跳台阶问题](#234青蛙跳台阶问题)
    - [235.两数之和 Two Sum](#235两数之和-two-sum)
    - [236.搜索旋转排序数组 Search in Rotated Sorted Array](#236搜索旋转排序数组-search-in-rotated-sorted-array)
    - [237.Python实现一个Stack的数据结构](#237python实现一个stack的数据结构)
    - [238.写一个二分查找](#238写一个二分查找)
    - [239.set 用 in 时间复杂度是多少，为什么？](#239set-用-in-时间复杂度是多少为什么)
    - [240.列表中有n个正整数范围在[0，1000]，进行排序；](#240列表中有n个正整数范围在01000进行排序)
    - [241.面向对象编程中有组合和继承的方法实现新的类](#241面向对象编程中有组合和继承的方法实现新的类)

<!-- /TOC -->

## 数据结构
### 222.数组中出现次数超过一半的数字-Python版

#### 方法一

```python
def majority_element(nums):
    nums.sort()
    return nums[len(nums) // 2]
```

#### 方法二

```python
from functools import reduce


def majority_element(nums):
    return reduce(lambda n, x: (n[0], n[1] + 1) if n[0] == x else ((x, 1) if n[1] - 1 < 0 else (n[0], n[1] - 1)), nums, (None, -1))[0]
```

#### 方法三

```python
from collections import Counter


def majority_element(nums):
    return Counter(nums).most_common(1)[0][0]
```

#### 方法四

```python
from random import choice


def majority_element(nums):
    length = len(nums) // 2
    while True:
        n = choice(nums)
        if nums.count(n) > length:
            return n
```

### 223.求100以内的质数
### 224.无重复字符的最长子串-Python实现
### 225.通过2个5/6升得水壶从池塘得到3升水
### 226.什么是MD5加密，有什么特点？
### 227.什么是对称加密和非对称加密
### 228.冒泡排序的思想？
### 229.快速排序的思想？
### 230.如何判断单向链表中是否有环？
### 231.你知道哪些排序算法（一般是通过问题考算法）
### 232.斐波那契数列

**数列定义: **

f 0 = f 1 = 1
f n = f (n-1) + f (n-2)

#### 根据定义

速度很慢，另外(暴栈注意！⚠️️） `O(fibonacci n)`

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### 线性时间的

**状态/循环**

```python
def fibonacci(n):
   a, b = 1, 1
   for _ in range(n):
       a, b = b, a + b
   return a
```

**递归**

```python
def fibonacci(n):
    def fib(n_, s):
        if n_ == 0:
            return s[0]
        a, b = s
        return fib(n_ - 1, (b, a + b))
    return fib(n, (1, 1))
```

**map(zipwith)**

```python
def fibs():
    yield 1
    fibs_ = fibs()
    yield next(fibs_)
    fibs__ = fibs()
    for fib in map(lambad a, b: a + b, fibs_, fibs__):
        yield fib
        
        
def fibonacci(n):
    fibs = fibs()
    for _ in range(n):
        next(fibs)
    return next(fibs)
```

#### Logarithmic

**矩阵**

```
import numpy as np
def fibonacci(n):
    return (np.matrix([[0, 1], [1, 1]]) ** n)[1, 1]
```

**不是矩阵**

```python
def fibonacci(n):
    def fib(n):
        if n == 0:
            return (1, 1)
        elif n == 1:
            return (1, 2)
        a, b = fib(n // 2 - 1)
        c = a + b
        if n % 2 == 0:
            return (a * a + b * b, c * c - a * a)
        return (c * c - a * a, b * b + c * c)
    return fib(n)[0]
```

### 233.如何翻转一个单链表？

```python
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        temp  = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

if __name__ == '__main__':
    link = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node7,Node(8.Node(9))))))))
    root = rev(link)
    while root:
        print(roo.data)
        root = root.next
```



### 234.青蛙跳台阶问题

一只青蛙要跳上n层高的台阶，一次能跳一级，也可以跳两级，请问这只青蛙有多少种跳上这个n层台阶的方法？

方法1：递归

设青蛙跳上n级台阶有f(n)种方法，把这n种方法分为两大类，第一种最后一次跳了一级台阶，这类共有f(n-1)种，第二种最后一次跳了两级台阶，这种方法共有f(n-2)种，则得出递推公式f(n)=f(n-1) + f(n-2),显然f(1)=1,f(2)=2，这种方法虽然代码简单，但效率低，会超出时间上限

```python
class Solution:
    def climbStairs(self,n):
        if n ==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
```

方法2：用循环来代替递归

```python
class Solution:
    def climbStairs(self,n):
        if n==1 or n==2:
            return n
        a,b,c = 1,2,3
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
        return c
```

### 235.两数之和 Two Sum



### 236.搜索旋转排序数组 Search in Rotated Sorted Array
### 237.Python实现一个Stack的数据结构
### 238.写一个二分查找
### 239.set 用 in 时间复杂度是多少，为什么？
### 240.列表中有n个正整数范围在[0，1000]，进行排序；
### 241.面向对象编程中有组合和继承的方法实现新的类
