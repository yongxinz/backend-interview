<!-- TOC -->

- [编程语言](#编程语言)
    - [1、Python实现单例模式](#1Python实现单例模式)

- [数据结构](#数据结构)
    - [2、二维数组中的查找](#2二维数组中的查找)
    - [3、替换空格](#3替换空格)
    - [4、从尾到头打印单链表](#4从尾到头打印单链表)
    - [5、重建二叉树](#5重建二叉树)
    - [6、用两个栈实现队列](#6用两个栈实现队列)
- [算法和数据操作](算法和数据操作)
    - [7、旋转数组的最小数字](#7旋转数组的最小数字)
    - [8、斐波那契数列](#8斐波那契数列)
    - [9、二进制中1的个数](#9二进制中1的个数)


<!-- /TOC -->
## 编程语言
### 1、Python 实现单例模式

#### 方法一 使用__new__实现单例模式
> 使用__new__实现单例模式，具体我对__new__的理解可以点[这里](http://www.cnblogs.com/qiaojushuang/p/7805973.html)
```python
class SingleTon(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        # print cls._instance
        return cls._instance[cls]


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val

    def obj_fun(self):
        print self.val, 'obj_fun'

    @staticmethod
    def static_fun():
        print 'staticmethod'

    @classmethod
    def class_fun(cls):
        print cls.class_val, 'classmethod'


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print a is b   # True
    print id(a), id(b)  # 4367665424 4367665424
    # 类型验证
    print type(a)  # <class '__main__.MyClass'>
    print type(b)  # <class '__main__.MyClass'>
```

#### 方法二 使用装饰器实现单例模式
```python
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single


@single_ton
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)
    print s is t
    print s.a, t.a
    print s.val, t.val
```

#### 方法三 使用模块实现单例模式
> 可以使用模块创建单例模式，然后在其他模块中导入该单例，这个需要所有人遵守导入规则，不然就没法实现单例了

```python
# use_module.py
class SingleTon(object):

    def __init__(self, val):
        self.val = val

single = SingleTon(2)

# test_module.py
from use_module import single

a = single
b = single
print a.val, b.val
print a is b
a.val = 233
print a.val, b.val

```

#### 方法四 使用metaclass实现单例模式
> 目前我对元类还了解不深，以后来填坑

## 数据结构

### 2、二维数组中的查找 [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/)
> 题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
>
> 思路：从左下角或者右上角开始比较

```python
def find_integer(matrix, num):
    """
    :param matrix: [[]]
    :param num: int
    :return: bool
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False
```

### 3、替换空格
> 题目：把字符串中的空格替换成'20%'
>
>方法1：直接使用Python字符串的内置函数

```python
>>> ' a  b  '.replace(' ', '20%')
```
> 方法2: 使用正则表达式

```python
>>> import re
>>> ret = re.compile(' ')
>>> ret.sub('20%', '  a  b  ')
```

### 4、从尾到头打印单链表
> 方法1：使用栈,可以使用列表模拟

```python
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print stack.pop()
```
> 方法2：直接递归

```python
def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print links.val
```

### 5、重建二叉树 [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
> 要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
>
> 思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
>
> **提示**：二叉树结点，以及对二叉树的各种操作，测试代码见six.py
```python
def construct_tree(preorder=None, inorder=None):
    """
    构建二叉树
    """
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index+1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1+len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root
```

### 6、用两个栈实现队列
> 要求：用两个栈实现队列，分别实现入队和出队操作
> 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中

```python
class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'
```

## 算法和数据操作

### 7、旋转数组的最小数字
> 要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]
>
> 思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找

```python
def find_min(nums):
    if not nums:
        return False
    length = len(nums)
    left, right = 0, length - 1
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left + right) / 2
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[0]
```

### 8、斐波那契数列
> 思路：用生成器

```python
def fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield b
        a, b = b, a + b
```

### 9、二进制中1的个数
> 要求：求一个整数的二进制表示中，1的个数
>
> 思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1


```python
def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret
```
