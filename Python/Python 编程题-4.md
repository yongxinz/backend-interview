<!-- TOC -->

- [时间效率](#时间效率)
    - [1、数组中出现次数超过一半的数字](#1数组中出现次数超过一半的数字)
    - [2、最小的k个数](#2最小的k个数)
    - [3、连续子数组的最大和](#3连续子数组的最大和)
    - [4、从1到n整数中1出现的次数](#4从1到n整数中1出现的次数)
    - [5、把数组排成最小的数](#5把数组排成最小的数)

- [时间效率与空间效率的平衡](#时间效率与空间效率的平衡)
    - [6、丑数](#6丑数)
    - [7、第一个只出现一次的字符](#7第一个只出现一次的字符)
    - [8、数组中的逆序对](#8数组中的逆序对)
    - [9、两个链表的第一个公共结点](#5两个链表的第一个公共结点)



<!-- /TOC -->
## 时间效率
### 1、数组中出现次数超过一半的数字

> 思路: 使用hash，key是数字，value是出现的次数
>
> 注意: 列表的len方法的时间复杂度是O(1)
>

```python
# coding=utf-8
"""
数组中出现次数超过一半的数字
思路: 使用hash，key是数字，value是出现的次数
注意: 列表的len方法的时间复杂度是O(1)
"""


def get_more_half_num(nums):
    hashes = dict()
    length = len(nums)
    for n in nums:
        hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
        if hashes[n] > length / 2:
            return n

if __name__ == '__main__':
    test = [1, 2, 1, 2, 3, 1, 1]
    print get_more_half_num(test)
```

### 2、最小的k个数
> 要求：求数组中出现次数超过一半的数字
>
> 思路: 使用heapq，该模块是一个最小堆，需要转化成最大堆，只要在入堆的时候把值取反就可以转化成最大堆(仅适用于数字)
>
> 思路二: 数组比较小的时候可以直接使用heapq的nsmallest方法

```python
# coding=utf-8
"""
求数组中最小的k个数
思路：使用heapq，该模块是一个最小堆，需要转化成最大堆，
只要在入堆的时候把值取反就可以转化成最大堆，仅适用于数字
"""
import random
import heapq


def get_least_k_nums(nums, k):
    # 数组比较小的时候可以直接使用
    return heapq.nsmallest(k, nums)


class MaxHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        elem = -elem  # 入堆的时候取反，堆顶就是最大值的相反数了
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            least = self.data[0]
            if elem > least:
                heapq.heapreplace(self.data, elem)

    def get_least_k_nums(self):
        return sorted([-x for x in self.data])

if __name__ == '__main__':
    test = random.sample(xrange(100000), 100)
    print get_least_k_nums(test, 4)
    h = MaxHeap(4)
    for t in test:
        h.push(t)
    print h.get_least_k_nums()
```

### 3、连续子数组的最大和
> 思路: 动态规划问题

```python
# coding=utf-8
"""
连续子数组的最大和
动态规划问题
"""


def max_sum(nums):
    ret = float("-inf")  # 负无穷
    if not nums:
        return ret
    current = 0
    for i in nums:
        if current <= 0:
            current = i
        else:
            current += i
        ret = max(ret, current)
    return ret

if __name__ == '__main__':
    test = [1, 2, -2, 3, 6, 0, -2]
    print max_sum(test)
```
### 4、从1到n整数中1出现的次数
> 要求：求从1到n整数的十进制表示中，1出现的次数
>
> 思路: 获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
>
> 此题中，作者的描述我没有理解，按照自己的理解写了一下，具体内容请点击[这里](http://www.cnblogs.com/qiaojushuang/p/7780445.html)

```python
# coding=utf-8
"""
求从1到n整数的十进制表示中，1出现的次数
思路：获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
"""


def get_digits(n):
    # 求整数n的位数
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret


def get_1_digits(n):
    """
    获取每个位数之间1的总数
    :param n: 位数
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current


def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)


def test_n(num):
    # 常规方法用来比较
    ret = 0
    for n in range(1, num+1):
        for s in str(n):
            if s == '1':
                ret += 1
    return ret

if __name__ == '__main__':
    test = 9923446
    import time
    t = time.clock()
    print test_n(test)
    print time.clock() - t
    t1 = time.clock()
    print get_1_nums(test)
    print time.clock() - t1
```


### 5、把数组排成最小的数
> 要求：把数组中的值拼接，找出能产生的最小的数[321,32,3]最小的数是321323
>
> 思路: Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以

```python
# coding=utf-8
"""
把数组中的值拼接，找出能产生的最小的数[321,32,3]最小的数是321323
Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以
"""


def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def print_mini(nums):
    if not nums:
        return
    print int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))


if __name__ == '__main__':
    test = []
    print_mini(test)
```

## 时间效率与空间效率的平衡

### 6、丑数 [LeetCode](https://leetcode.com/problems/ugly-number-ii/)
> 要求：只含有2、3、5因子的数是丑数，求第1500个丑数
>
> 思路: 按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值

```python
# coding=utf-8
"""
只含有2、3、5因子的数是丑数，求第1500个丑数
按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        t2 = t3 = t5 = 0
        while len(ugly) < n:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5))
        return ugly[-1]


if __name__ == '__main__':
    print Solution().nthUglyNumber(1500)
```

### 7、第一个只出现一次的字符
> 要求：求字符串中第一个只出现一次的字符
>
> 思路: 使用两个hash，一个记录每个字符穿线的次数，另一个记录每个字符第一次出现的位置

```python
# coding=utf-8
"""
求字符串中第一个只出现一次的字符
使用两个hash，一个记录每个字符穿线的次数，另一个记录每个字符第一次出现的位置
"""


def first_not_repeating_char(string):
    if not string:
        return -1
    count = {}
    loc = {}
    for k, s in enumerate(string):
        count[s] = count[s] + 1 if count.get(s) else 1
        loc[s] = loc[s] if loc.get(s) else k
    ret = float('inf')
    for k in loc.keys():
        if count.get(k) == 1 and loc[k] < ret:
            ret = loc[k]
    return ret

if __name__ == '__main__':
    test = 'abaccbdse'
    print first_not_repeating_char(test)
```

### 8、数组中的逆序对
> 要求：在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数
>
> 思路: 归并排序,先把数组依次拆开，然后合并的时候统计逆序对数目，并排序

```python
# coding=utf-8
"""
在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数
归并排序,先把数组依次拆开，然后合并的时候统计逆序对数目，并排序
"""
import copy


def get_inverse_pairs(nums):
    if not nums:
        return 0
    start, end = 0, len(nums) - 1
    tmp = copy.deepcopy(nums)
    return inverse_pairs(tmp, start, end)


def inverse_pairs(tmp, start, end):
    if start == end:  # 递归结束条件
        return 0
    mid = (end - start) / 2  # 分别对左右两边递归求值
    left = inverse_pairs(tmp, start, start+mid)
    right = inverse_pairs(tmp, start+mid+1, end)

    count = 0  # 本次逆序对数目
    l_right, r_right = start + mid, end
    t = []
    while l_right >= start and r_right >= start + mid + 1:
        if tmp[l_right] > tmp[r_right]:
            t.append(tmp[l_right])
            count += (r_right - mid - start)
            l_right -= 1
        else:
            t.append(tmp[r_right])
            r_right -= 1
    while l_right >= start:
        t.append(tmp[l_right])
        l_right -= 1
    while r_right >= start+mid+1:
        t.append(tmp[r_right])
        r_right -= 1
    tmp[start:end+1] = t[::-1]
    return count + left + right

if __name__ == '__main__':
    test = [7, 5, 6, 4, 8, 1, 2, 9]
    print get_inverse_pairs(test)
```

### 9、两个链表的第一个公共结点
> 思路: 先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历
>
> 文件thirty_seven.py中包含了设置链表公共结点的代码，可以用来测试

```python
# coding=utf-8
"""
求两个链表的第一个公共结点
先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历
"""


def get_first_common_node(link1, link2):
    if not link1 or not link2:
        return None
    length1 = length2 = 0
    move1, move2 = link1, link2
    while move1:  # 获取链表长度
        length1 += 1
        move1 = move1.next
    while move2:
        length2 += 1
        move2 = move2.next
    while length1 > length2:  # 长链表先走多的长度
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next
    while link1:  # 链表一起走
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Nodes(object):
    def __init__(self, values=None):
        self.nodes = self._set_link(values) if values else None

    def get_link(self):
        return self.nodes

    def get_tail(self):
        # 获取尾指针
        tail = self.nodes
        while tail.next:
            tail = tail.next
        return tail

    def print_self(self):
        Nodes.print_link(self.nodes)

    @staticmethod
    def print_link(link=None):
        count = 1
        while link:
            if count == 1:
                print link.val,
            elif count % 5 == 0:
                print '->', link.val
            else:
                print '->', link.val,
            count += 1
            link = link.next
        print

    def _set_link(self, values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print e
        return head.next

if __name__ == '__main__':
    t1 = [1, 2, 3, 4]
    t2 = [5, 6, 7, 8, 12]
    t3 = [9, 10, 11]
    node1, node2, common = Nodes(t1), Nodes(t2), Nodes(t3)
    h1 = node1.get_link()
    h2 = node2.get_link()
    h3 = common.get_link()
    tail1 = node1.get_tail()
    tail2 = node2.get_tail()
    tail2.next = h3  # 设置公共链表
    tail1.next = h3
    print get_first_common_node(h1, h2)
    print h3
```
