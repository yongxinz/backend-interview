<!-- TOC -->

- [画图让抽象问题形象化](#画图让抽象问题形象化)
    - [1、二叉树的镜像](#1二叉树的镜像)
    - [2、顺时针打印矩阵](#2顺时针打印矩阵)

- [举例让抽象问题具体化](#举例让抽象问题具体化)
    - [3、包含min函数的栈](#3包含min函数的栈)
    - [4、栈的压入弹出序列](#4栈的压入弹出序列)
    - [5、从上往下打印二叉树](#5从上往下打印二叉树)
    - [6、二叉树的后序遍历序列](#6二叉树的后序遍历序列)
    - [7、二叉树中和为某一值的路径](#7二叉树中和为某一值的路径)

- [分解让复杂问题简单化](#分解让复杂问题简单化)
    - [8、复杂链表的复制](#8复杂链表的复制)
    - [9、二叉搜索树与双向链表](#9二叉搜索树与双向链表)
    - [10、字符串的排列](#10字符串的排列)


<!-- /TOC -->
## 画图让抽象问题形象化
### 1、二叉树的镜像

> 思路一：可以按层次遍历，每一层从右到左
>
> 思路二：使用递归


```python
# coding=utf-8
"""
求二叉树的镜像
思路一：按层次遍历，每一层从右到左
思路二：递归遍历
"""
from collections import deque


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


def mirror_bfs(root):
    ret = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ret.append(node.val)
            queue.append(node.right)
            queue.append(node.left)
    return ret


def mirror_pre(root):
    ret = []

    def traversal(root):
        if root:
            ret.append(root.val)
            traversal(root.right)
            traversal(root.left)
    traversal(root)
    return ret


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 6, 4, 3, 7, 5])
    print t.bfs()
    print mirror_bfs(t.root)
    print mirror_pre(t.root)
```

### 2、顺时针打印矩阵

> 思路：每一圈的开始位置总是坐上角元素[0, 0], [1, 1]...

```python
# coding=utf-8
"""
按从外到里的顺序顺时针打印矩阵
每一圈的开始位置总是坐上角元素[0, 0], [1, 1]...
"""


def print_matrix(matrix):
    """
    :param matrix: [[]]
    """
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    print ret


def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1  # 最后一行
    col = cols - start - 1
    # left->right
    for c in range(start, col+1):
        ret.append(matrix[start][c])
    # top->bottom
    if start < row:
        for r in range(start+1, row+1):
            ret.append(matrix[r][col])
    # right->left
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom->top
    if start < row and start < col:
        for r in range(start+1, row)[::-1]:
            ret.append(matrix[r][start])


if __name__ == '__main__':
    """
    mat = [[1, 2, 3],
           [5, 6, 7],
           [9, 10, 11]]
    mat = [[]]
    mat = [[1]]
    mat = [[1, 2, 3, 4]]
    mat = [[1], [2], [3], [4]]
    """
    mat = [[1, 2],
           [5, 6]]
    print_matrix(mat)
```

## 举例让抽象问题具体化

### 3、包含min函数的栈
> 要求：栈的push，pop，min操作的时间复杂度都是O(1)
>
> 思路：使用一个辅助栈保存最小值

```python
# coding=utf-8
"""
包含min函数的栈
栈的push，pop，min操作的时间复杂度都是O(1)
使用一个辅助栈保存最小值
"""


class MyStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        if self.stack:
            self.min.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min[-1] if self.min else None

if __name__ == '__main__':
    s = MyStack()
    s.push(2)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(2)
    print s.stack
    print s.min
```

### 4、栈的压入弹出序列
> 要求：判断给定的两个序列中，后者是不是前者的弹出序列，给定栈不包含相同值
>
> 思路：使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
> 如果最后出栈序列为空，则是入栈的弹出序列值

```python
# coding=utf-8
"""
栈的压入弹出序列，判断给定的两个序列中，后者是不是前者的弹出序列
序列中不存在相同值
使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
如果最后出栈序列为空，则是入栈的弹出序列
"""


def pop_order(push_stack, pop_stack):
    if not push_stack or not pop_stack:
        return False
    stack = []
    while pop_stack:
        pop_val = pop_stack[0]
        if stack and stack[-1] == pop_val:
            stack.pop()
            pop_stack.pop(0)
        else:
            while push_stack:
                if push_stack[0] != pop_val:
                    stack.append(push_stack.pop(0))
                else:
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break
        if not push_stack:
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False
    if not pop_stack:
        return True
    return False


if __name__ == '__main__':
    print pop_order([1, 2, 3], [2, 3, 1])
```

### 5、从上往下打印二叉树
> 思路：广度优先搜索，按层次遍历

```python
# coding=utf-8
"""
从上往下打印二叉树
树的广度优先，按层次遍历，使用一个辅助队列就可以
"""


from collections import deque


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
    t.construct_tree([1, 2, 6, 4, 3, 7, 5])
    print t.bfs()
    print bfs(t.root)
```

### 6、二叉搜索树的后序遍历序列
> 要求：判断给定的整数数组是不是二叉搜索树的后序遍历序列
>
> 整数数组中不包含重复值
>
> 整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树

```python
# coding=utf-8
"""
判断给定的整数数组是不是二叉搜索树的后序遍历序列
整数数组中不包含重复值
整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
"""


def is_post_order(order):
    length = len(order)
    if length:
        root = order[-1]
        left = 0
        while order[left] < root:
            left += 1
        right = left
        while right < length - 1:
            if order[right] < root:
                return False
            right += 1
        left_ret = True if left == 0 else is_post_order(order[:left])
        right_ret = True if left == right else is_post_order(order[left:right])
        return left_ret and right_ret
    return False


if __name__ == '__main__':
    print is_post_order([9, 6, 7])
```

### 7、二叉树中和为某一值的路径
> 要求：输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径
>
> 深度优先搜索变形

```python
# coding=utf-8
"""
输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径
深度优先搜索变形
"""


from collections import deque


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


def find_path(tree, num):
    ret = []
    if not tree:
        return ret
    path = [tree]
    sums = [tree.val]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1]+tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()

    dfs(tree)
    return ret


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 3, 6, 4, 3, 1, 1])
    print find_path(t.root, 8)
```

## 分解让复杂问题简单化
### 8、复杂链表的复制

> 要求：链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
>
> 分为三步完成：
> 
> 一:复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
> 
> 二:为每个新结点设置other指针
> 
> 三:把复制后的结点链表拆开
> 
> 题目设置了复杂链表的实现，测试代码见文件twenth_six.py


```python
# coding=utf-8
"""
复杂链表的复制
链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
分为三步完成：
一复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
二为每个新结点设置other指针
三把复制后的结点链表拆开
"""
import random


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.other = None


class Solution(object):

    @staticmethod
    def clone_nodes(head):
        # 结点复制
        move = head
        while move:
            tmp = Node(move.val)
            tmp.next = move.next
            move.next = tmp
            move = tmp.next
        return head

    @staticmethod
    def set_nodes(head):
        # other指针设置
        move = head
        while move:
            m_next = move.next
            if move.other:
                m_next.other = move.other.next
            move = m_next.next
        return head

    @staticmethod
    def reconstruct_nodes(head):
        # 结点拆分
        ret = head.next if head else Node
        move = ret
        while head:
            head = move.next
            if head:
                move.next = head.next
                move = move.next
        return ret

    @staticmethod
    def clone_link(head):
        # 结果
        h = Solution.clone_nodes(head)
        h = Solution.set_nodes(h)
        ret = Solution.reconstruct_nodes(h)
        return ret

    @staticmethod
    def print_nodes(head):
        # 打印结点值，结点other的值，用来比较
        ret = []
        while head:
            tmp = [head.val]
            if head.other:
                tmp.append(head.other.val)
            ret.append(tmp)
            head = head.next
        print ret

    @staticmethod
    def construct_nodes(vals):
        """
        构造一个简单的复杂链表
        :param vals: list
        :return: Nodes
        """
        if not vals:
            return Node
        move = head = Node(vals.pop(0))
        nodes = [None, head]
        for v in vals:
            tmp = Node(v)
            move.next = tmp
            nodes.append(tmp)
            move = move.next
        # print [node.val for node in nodes if node]
        move = head
        while move:
            # 设置other指针为随机结点
            move.other = random.choice(nodes)
            move = move.next
        return head


if __name__ == '__main__':
    link = Solution.construct_nodes([1, 2, 3, 4, 5])
    Solution.print_nodes(link)
    test = Solution.clone_link(link)  # 复制
    Solution.print_nodes(test)
```

### 9、二叉搜索树与双向链表

> 要求: 将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向
> 
> 思路: 中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
>
> 注意: 题目构造了一个普通二叉树用来测试，构造时按照二叉搜索树的顺序输入结点，空结点用None表示，详情见twenty_seven.py


```python
# coding=utf-8
"""
将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向，不用新结点
中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    """
    非二叉搜索树，建树的时候values中的顺序需要注意
    之后有时间会改成二叉搜索树
    """
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        # 结点值不存在的话，values中用None表示
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


class Solution(object):

    @staticmethod
    def convert(tree):
        """结点转换"""
        if not tree:
            return None
        p_last = Solution.convert_nodes(tree, None)
        while p_last and p_last.left:  # 获取链表头结点
            p_last = p_last.left
        return p_last

    @staticmethod
    def convert_nodes(tree, last):
        if not tree:
            return None
        if tree.left:
            last = Solution.convert_nodes(tree.left, last)
        if last:
            last.right = tree
        tree.left = last
        last = tree
        if tree.right:
            last = Solution.convert_nodes(tree.right, last)
        return last

    @staticmethod
    def print_nodes(tree):
        # 正序链表打印
        ret = []
        while tree:
            tmp = []
            tmp.append(tree.left.val if tree.left else None)
            tmp.append(tree.val)
            tmp.append(tree.right.val if tree.right else None)
            ret.append(tmp)
            tree = tree.right
        print ret

if __name__ == '__main__':
    r = Tree()
    # r.construct_tree([2, 1])
    # r.construct_tree([2, None, 3])
    # r.construct_tree([2, 1, 3])
    # r.construct_tree([])
    r.construct_tree([5, 3, 6, 2, 4, None, 7, 1])
    t = Solution.convert(r.root)
    Solution.print_nodes(t)
```

### 10、字符串的排列

> 要求：求输入字符串的全排列
>
> 思路：递归完成，也可以直接使用库函数


```python
# coding=utf-8
"""
求输入字符串的全排列
递归完成，也可以直接使用库函数
"""

from itertools import permutations


def my_permutation(s):
    str_set = []
    ret = []  # 最后的结果

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()

    permutation(s)
    return ret


if __name__ == '__main__':
    s = 'abc'
    print my_permutation(s)
    print [''.join(p) for p in permutations(s)]
```
