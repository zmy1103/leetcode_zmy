## 116 Fill the next right node pointer of each node

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png)

### 递归：

难点：连接不同父节点的两个相邻节点

解决：虽然⑤⑥是不同的父节点，但是他们的父节点总是相邻的。

所以对于两个节点node1和node2，可以这样：

1. node1.left.next = node1.right
2. node2.left.next = node2.right
3. node1.right.next = node2.left

所以不能只以root一个节点最为参照，要传两个参数进去root.left root.right

不能以一个节点为单位完成所有的操作，就以两个为单位

```python
lass Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.left == None:
            return root
        self.connecttwonode(root.left, root.right)
        return root
    def connecttwonode(self, node1: 'Node', node2: 'Node'):#两个相邻节点
        if node1 == None:
            return node1
        node1.next = node2
        self.connecttwonode(node1.left, node1.right)
        self.connecttwonode(node2.left, node2.right)
        self.connecttwonode(node1.right, node2.left)
```

### 层次遍历：

一层一层访问刚好可以让同一层相邻的节点在队列中靠在一起，所以自然想到用队列实现层次遍历

```python
import collection 
def connect(self, root:'Node') -> 'Node':
    if not root:
        return root
    Q = collections.deque([root])#初始化队列
    while Q:
        size = len(Q)
        for i in range(0,size):
            node = Q.popleft()
           	if i < size-1:
                node.next = Q[0]
            if node.left:
                Q.append(node.left)
            if node.right:
 	            Q.append(node.right)
     return root
```



## 117 升级版

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)

层次遍历得代码完全适用

除此之外也可以使用使用已建立得next指针

```python
def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:  # 当前层的头节点
            cur = head  # 当前层处理节点
            pre = head = None  # 初始化下一层头节点和前置节点
            while cur:
                if cur.left:
                    if not pre:  # 若尚未找到下一层前置节点，则同步更新下一层头节点和前置节点
                        pre = head =cur.left
                    else:  # 已找到下一层前置节点，则将前置节点指向当前子节点，并前移pre
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
        return root

```

![](https://tvax2.sinaimg.cn/large/005IQUPRly1gjy2j376bdj30ry0mg41p.jpg)

![](https://tva2.sinaimg.cn/large/005IQUPRly1gjy2jb6mnlj30lr0n2776.jpg)

![](https://tva3.sinaimg.cn/large/005IQUPRly1gjy2jgdciyj30of0ceq4c.jpg)