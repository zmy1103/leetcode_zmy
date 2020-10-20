## 226 Iteration

递归实现也就是深度优先遍历的方式，那么对应的就是广度优先遍历。
广度优先遍历需要额外的数据结构--队列，来存放临时遍历到的元素。
深度优先遍历的特点是一竿子插到底，不行了再退回来继续；而广度优先遍历的特点是层层扫荡。
所以，我们需要先将根节点放入到队列中，然后不断的迭代队列中的元素。
对当前元素调换其左右子树的位置，然后：

- 判断其左子树是否为空，不为空就放入队列中
- 判断其右子树是否为空，不为空就放入队列中

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root == None:
        return None
    queue = [root]#存储节点得list
    while queue:
        tmp = queue.pop(0)
        tmp.left,tmp.right = tmp.right,tmp.left
        if tmp.left != None:
            queue.append(tmp.left)
        if tmp.right != None:
            queue.append(tmp.right)
   return root
```

