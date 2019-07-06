<!-- TOC -->

- [代码的完整性](#代码的完整性)
    - [1、数值的整数次方](#1数值的整数次方)
    - [2、打印1到最大的n位数](#2打印1到最大的n位数)
    - [3、O(1)时间删除链表结点](#3O(1)时间删除链表结点)
    - [4、调整数组顺序使寄数位于偶数前面](#4调整数组顺序使寄数位于偶数前面)

- [代码的鲁棒性](#代码的鲁棒性)
    - [5、链表中倒数第k个结点](#5链表中倒数第k个结点)
    - [6、反转链表](#6反转链表)
    - [7、合并两个排序的链表](#7合并两个排序的链表)
    - [8、树的子结构](#8树的子结构)



<!-- /TOC -->
## 代码的完整性
### 1、数值的整数次方

> 要求：求一个数的整数次方
>
> 思路：需要考虑次方是正数、负数和0，基数是0
>
> 浮点数相等不能直接用==

```python
def power(base, exponent):
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError
    ret = power_value(base, abs(exponent))
    if exponent < 0:
        return 1.0 / ret
    else:
        return ret


def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    ret = power_value(base, exponent >> 1)
    ret *= ret
    if exponent & 1 == 1:
        ret *= base
    return ret
```

### 2、打印1到最大的n位数
> 要求：输入n，打印出从1到最大的n位数
>
> 思路：Python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题

```python
def print_max_n(n):
    for i in xrange(10 ** n):
        print i
```

### 3、O(1)时间删除链表结点
> 要求：O(1)时间删除链表结点
>
> 思路：如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了

```python
def delete_node(link, node):
    if node == link:  # 只有一个结点
        del node
    if node.next is None:  # node是尾结点
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node
```
### 4、调整数组顺序使奇数位于偶数前面
> 思路：使用两个指针，前后各一个，为了更好的扩展性，可以把判断奇偶部分抽取出来

```python
def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while not func(nums[left]):
            left += 1
        while func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0
```

## 代码的鲁棒性

### 5、链表中倒数第k个结点
> 要求：求单链表中的倒数第k个结点
>
> 思路：使用快慢指针，快的先走k-1步，需要考虑空链表以及k为0

```python
def last_kth(link, k):
    if not link or k <= 0:
        return None
    move = link
    while move and k-1 >= 0:
        move = move.next
        k -= 1
    while move:
        move = move.next
        link = link.next
    if k == 0:
        return link.val
    return None
```

### 6、反转链表
> 要求：反转链表
>
> 思路：需要考虑空链表，只有一个结点的链表

```python
def reverse_link(head):
    if not head or not head.next:
        return head
    then = head.next
    head.next = None
    last = then.next
    while then:
        then.next = head
        head = then
        then = last
        if then:
            last = then.next
    return head
```

### 7、合并两个排序的链表
> 要求：合并两个排序的链表
>
> 思路：使用递归

```python
def merge_link(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        ret = head1
        ret.next = merge_link(head1.next, head2)
    else:
        ret = head2
        ret.next = merge_link(head1, head2.next)
    return ret

```

### 8、树的子结构
> 要求：判断一棵二叉树是不是另一个的子结构
>
> 思路：使用递归

```python
def sub_tree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True
```