## 114 Binary tree expands into linked list

### 递归

- 总体递归思路：左右两侧假定已经转换成了链表，然后把左子树接到root右侧，右子树接到左侧
- 难点：右子树 如何 接在左子树最后一个节点的后面
- 解决办法：先把左子树接上，然后往右遍历到最后一个指针

![](https://tva3.sinaimg.cn/large/005IQUPRly1gjvvuk95uxj30u00gwdox.jpg)

### 栈，迭代

```python
def flatten(self, root:TreeNode) -> None:
    curr = root
    while curr:
        if curr.left:
            predecessor = nxt = curr.left
            while prodecessor.right:
                predecessor = prodecessor.right
            predecessor.right = curr.right
            curr.left = None
            curr.right = nxt
        curr = curr.right
```

