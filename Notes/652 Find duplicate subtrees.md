## 652 Find duplicate subtrees

### 问题描述：

​	输入是一棵二叉树的根节点`root`，返回的是一个列表，里面装着若干个二叉树节点，这些节点对应的子树在原二叉树中是存在重复的。

### 关键点：

- 遍历到一个节点，节点要确定他的孩子们，所以适合采用后序遍历。
- 判断子树可以用它们的值得序列来记录

```python
class Solution:
    emm = []
    List_node = []
    def jkdf(self):
        self.emm = []
        self.List_node = []
    def tra(self, root: TreeNode):
        if root == None:
            return "*"
        temp = ""
        temp += self.tra(root.left)
        temp += "left,"
        temp += self.tra(root.right)
        temp += "right,"
        temp += str(root.val)
        self.emm.append(temp) 
        self.List_node.append(root)
        return temp
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.jkdf()
        self.tra(root)
        for i in set(self.emm):
            index = self.emm.index(i)
            self.emm.remove(i)
            self.List_node.pop(index)
        List_node_result = []
        for i in set(self.emm):
            index = self.emm.index(i)
            self.emm.remove(i)
            List_node_result.append(self.List_node[index]) 
            self.List_node.pop(index)
        return List_node_result

```

