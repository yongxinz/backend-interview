<!-- TOC -->

- [知识迁移能力](#知识迁移能力)
    - [1、数字在排序数组中出现的次数](#1数字在排序数组中出现的次数)
    - [2、二叉树的深度](#2二叉树的深度)
    - [3、数组中只出现一次的数字](#3数组中只出现一次的数字)
    - [4、和为s的两个数字VS和为s的连续正数序列](#4和为s的两个数字VS和为s的连续正数序列)
    - [5、翻转单词顺序与左旋转字符串](#5翻转单词顺序与左旋转字符串)

- [抽象建模能力](#抽象建模能力)
    - [6、n个骰子的点数](#6n个骰子的点数)
    - [7、扑克牌的顺子](#7扑克牌的顺子)
    - [8、圆圈中最后剩下的数字](#8圆圈中最后剩下的数字)

- [发散思维能力](#发散思维能力)
    - [9、求1+2...+n](#9求1+2...+n)
    - [10、不用加减乘除做加法](#10不用加减乘除做加法)
    - [11、不能被继承的类](#8不能被继承的类)

- [案例](#案例)
    - [12、把字符串转化成整数](#12把字符串转化成整数)
    - [13、树中两个结点的最低公共祖先]](#13树中两个结点的最低公共祖先])


<!-- /TOC -->
## 知识迁移能力
### 1、数字在排序数组中出现的次数

> 思路: 使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减

```python
# coding=utf-8
"""
统计一个数字在排序数组中出现的次数
使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减
"""


def get_k_counts(nums, k):
    first = get_first_k(nums, k)
    last = get_last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    if first < 0 or last < 0:
        return 1
    return last - first + 1


def get_first_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < k:
            if mid + 1 < len(nums) and nums[mid+1] == k:
                return mid + 1
            left = mid + 1
        elif nums[mid] == k:
            if mid - 1 < 0 or (mid - 1 >= 0 and nums[mid-1] < k):
                return mid
            right = mid - 1
        else:
            right = mid - 1
    return -1


def get_last_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] == k:
            if mid + 1 == len(nums) or (mid + 1 < len(nums) and nums[mid+1] > k):
                return mid
            left = mid + 1
        else:
            if mid - 1 >= 0 and nums[mid-1] == k:
                return mid - 1
            right = mid - 1
    return -1

if __name__ == '__main__':
    test = [1, 2, 2, 3, 3, 3, 4]
    print get_k_counts(test, 5)
```

### 2、二叉树的深度

> 思路: 分别递归的求左右子树的深度

```python
# coding=utf-8
"""
求二叉树的深度
分别递归的求左右子树的深度
"""
from collections import deque


def get_depth(tree):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1
    return 1 + max(get_depth(tree.left), get_depth(tree.right))


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret


def bfs(tree):
    if not tree:
        return None
    stack = [tree]
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret

if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 3])
    print t.bfs()
    print get_depth(t.root)
```

### 3、数组中只出现一次的数字
> 要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍
>
> 思路: 按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组

```python
# coding=utf-8
"""
数组中除了两个只出现一次的数字外，其他数字都出现了两遍
按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组
"""


def get_only_one_number(nums):
    if not nums:
        return None
    tmp_ret = 0
    for n in nums:  # 获取两个值的异或结果
        tmp_ret ^= n
    last_one = get_bin(tmp_ret)
    a_ret, b_ret = 0, 0
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n
        else:
            b_ret ^= n
    return [a_ret, b_ret]


def get_bin(num):  # 得到第一个1
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):  # 验证t位是不是1
    num = num >> t
    return num & 0x01


if __name__ == '__main__':
    test = [1, 2, 3, 4, 3, 1, -1, -1]
    print get_only_one_number(test)
```

### 4、和为s的两个数字VS和为s的连续正数序列
#### 和为s的两个数字
> 要求：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
>
> 思路: 设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加

```python
# coding=utf-8
"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
"""


def sum_to_s(nums, s):
    head, end = 0, len(nums) - 1
    while head < end:
        if nums[head] + nums[end] == s:
            return [nums[head], nums[end]]
        elif nums[head] + nums[end] > s:
            end -= 1
        else:
            head += 1
    return None

if __name__ == '__main__':
    test = [-4, 0, 1, 2, 4, 6, 8, 10, 12, 15, 18]
    s = 12
    print sum_to_s(test, s)
```

#### 和为s的连续整数序列
> 要求：输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)
>
> 思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移

```python
# coding=utf-8
"""
输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)
使用两个指针，和比s小，大指针后移，比s大，小指针后移
"""


def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s / 2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b+1))
            a += 1
        elif sum(range(a, b+1)) < s:
            b += 1
        else:
            a += 1
    return ret

if __name__ == '__main__':
    test = 199
    print sum_to_s(test)
```

### 5、翻转单词顺序与左旋转字符串
#### 翻转单词顺序
> 要求：翻转一个英文句子中的单词顺序，标点和普通字符一样处理
>
> 思路: Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去

```python
# coding=utf-8
"""
翻转一个英文句子中的单词顺序，标点和普通字符一样处理
Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去
"""


def reverse_words(sentence):
    tmp = sentence.split()
    return ' '.join(tmp[::-1])  # 使用join效率更好，+每次都会创建新的字符串

if __name__ == '__main__':
    test = 'I am a engineer.'
    print reverse_words(test)

```
#### 左旋转字符串
> 思路: 把字符串的前面的若干位移到字符串的后面

```python
# coding=utf-8
"""
把字符串的前面的若干位移到字符串的后面
"""


def rotate_string(s, n):
    if not s:
        return ''
    n %= len(s)
    return s[n:] + s[:n]

if __name__ == '__main__':
    test = 'abcdefg'
    print rotate_string(test, 1)

```

## 抽象建模能力



### 6、n个骰子的点数
> 要求：求出n个骰子朝上一面之和s所有可能值出现的概率
>
> 思路：n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮

```python
# coding=utf-8
"""
求出n个骰子朝上一面之和s所有可能值出现的概率
n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮
"""


def get_probability(n):
    if n < 1:
        return []
    data1 = [0] + [1] * 6 + [0] * 6 * (n - 1)
    data2 = [0] + [0] * 6 * n   # 开头多一个0，方便按照习惯从1计数
    flag = 0
    for v in range(2, n+1):  # 控制次数
        if flag:
            for k in range(v, 6*v+1):
                data1[k] = sum([data2[k-j] for j in range(1, 7) if k > j])
            flag = 0
        else:
            for k in range(v, 6*v+1):
                data2[k] = sum([data1[k-j] for j in range(1, 7) if k > j])
            flag = 1
    ret = []
    total = 6 ** n
    data = data2[n:] if flag else data1[n:]
    for v in data:
        ret.append(v*1.0/total)
    print data
    return ret

if __name__ == '__main__':
    print get_probability(3)
```

### 7、扑克牌的顺子
> 要求：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
>
> 思路: 使用排序

```python
# coding=utf-8
"""
从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
使用排序
"""
import random


def is_continus(nums, k):
    data = [random.choice(nums) for _ in range(k)]
    data.sort()
    print data
    zero = data.count(0)
    small, big = zero, zero + 1
    while big < k:
        if data[small] == data[big]:
            return False
        tmp = data[big] - data[small]
        if tmp > 1:
            if tmp - 1 > zero:
                return False
            else:
                zero -= tmp - 1
                small += 1
                big += 1
        else:
            small += 1
            big += 1
    return True

if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            0, 0]
    t = 5
    print is_continus(test, t)
```

### 8、圆圈中最后剩下的数字
> 要求：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
>
> 思路：当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0，*关键是推导出关系表达式*


```python
# coding=utf-8
"""
0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0
"""


def last_num(n, m):
    ret = 0
    if n == 1:
        return 0
    for i in range(2, n+1):
        ret = (m + ret) % i
    return ret

if __name__ == '__main__':
    print last_num(3, 4)

```

## 发散思维能力


### 9、求1+2...+n
> 要求：不能使用乘除、for、while、if、else等
>
>方法一：使用range和sum
>
>方法二：使用reduce


```python
# coding=utf-8
"""
不能使用乘除、for、while、if、else等
方法一：使用range和sum
方法二：使用reduce
"""


def get_sum1(n):
    return sum(range(1, n+1))


def get_sum2(n):
    return reduce(lambda x, y: x+y, range(1, n+1))


if __name__ == '__main__':
    print get_sum1(4)
    print get_sum2(40)
```

### 10、不用加减乘除做加法
> 要求：不用加减乘除做加法
>
>方法一：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
>
>方法二：使用sum


```python
# coding=utf-8
"""
不用加减乘除做加法
方法一：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
方法二：使用sum
"""


def bit_add(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = 0xFFFFFFFF & ((n1 & n2) << 1)
        carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        n1 = s
        n2 = carry
    return n1


def add(n1, n2):
    return sum([n1, n2])

if __name__ == '__main__':
    a = 222
    b = -199
    print bit_add(a, b)
    print add(a, b)
```

### 11、不能被继承的类
>Python中不知道怎么实现不能被继承的类。以后补充代码或者原因。

## 案例


### 12、把字符串转化成整数
> 要求：把字符串转化成整数
>
> 测试用例：正负数和0，空字符，包含其他字符
>
> 备注：使用raise抛出异常作为非法提示


```python
# coding=utf-8
"""
把字符串转化成整数
测试用例：正负数和0，空字符，包含其他字符
备注：使用raise抛出异常作为非法提示
"""


def str_to_int(string):
    if not string:  # 空字符返回异常
        raise Exception('string cannot be None', string)
    flag = 0  # 用来表示第一个字符是否为+、-
    ret = 0  # 结果
    for k, s in enumerate(string):
        if s.isdigit():  # 数字直接运算
            val = ord(s) - ord('0')
            ret = ret * 10 + val
        else:
            if not flag:
                if s == '+' and k == 0:  # 避免中间出现+、-
                    flag = 1
                elif s == '-' and k == 0:
                    flag = -1
                else:
                    raise Exception('digit is need', string)
            else:
                raise Exception('digit is need', string)
    if flag and len(string) == 1:  # 判断是不是只有+、-
        raise Exception('digit is need', string)
    return ret if flag >= 0 else -ret


if __name__ == '__main__':
    test = '12399+'
    print str_to_int(test)
```

### 13、树中两个结点的最低公共祖先
> 要求：求普通二叉树中两个结点的最低公共祖先
>
>方法一：先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点
>
>备注：文件fifty.py中包含该代码的具体测试数据


```python
# coding=utf-8
"""
求普通二叉树中两个结点的最低公共祖先
先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点
"""
from collections import deque


class TreeNode(object):
    """树结点"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None
        self.nodes = []  # 树中的结点

    def construct_tree(self, values=None):
        """使用列表构造二叉树"""
        if not values:
            return None
        self.root = TreeNode(values[0])
        self.nodes.append(self.root)
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                self.nodes.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    self.nodes.append(node.right)
                    nums += 1
                nums += 1

    def get_node(self, index):
        """根据索引返回树中的某个结点"""
        if index >= len(self.nodes):
            return None
        return self.nodes[index]


class Solution(object):

    def __init__(self, root, node1, node2):
        self.root = root  # 树的根结点
        self.node1 = node1
        self.node2 = node2  # 需要求的两个结点

    @staticmethod
    def get_path(root, node, ret):
        """获取结点的路径"""
        if not root or not node:
            return False
        ret.append(root)
        if root == node:
            return True
        left = Solution.get_path(root.left, node, ret)
        right = Solution.get_path(root.right, node, ret)
        if left or right:
            return True
        ret.pop()

    def get_last_common_node(self):
        """获取公共结点"""
        route1 = []
        route2 = []  # 保存结点路径
        ret1 = Solution.get_path(self.root, self.node1, route1)
        ret2 = Solution.get_path(self.root, self.node2, route2)
        ret = None
        if ret1 and ret2:  # 路径比较
            length = len(route1) if len(route1) <= len(route2) else len(route2)
            index = 0
            while index < length:
                if route1[index] == route2[index]:
                    ret = route1[index]
                index += 1
        return ret

if __name__ == '__main__':
    vals = [0, 1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    tree.construct_tree(vals)
    r = tree.root  # 树的根结点
    n1 = tree.get_node(7)  # 结点1
    n2 = tree.get_node(4)  # 结点2
    s = Solution(r, n1, n2)
    parent = s.get_last_common_node()  # 公共结点
    print parent, parent.val if parent else None
```