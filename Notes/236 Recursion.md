## Recursion

**1、这个函数是干嘛的**？

**2、这个函数参数中的变量是什么的是什么**？

**3、得到函数的递归结果，你应该干什么**？

​																----labuladong

### 解法思路：

![Picture2.png](https://pic.leetcode-cn.com/e48705d412500d43fa81c1d8fdd107bb2d0c7dfa12bdc588cd88f481b4b9f7d8-Picture2.png)

1. **这个函数是干嘛的**？。

   描述：给该函数输入三个参数`root`，`p`，`q`，它会返回一个节点。

2. **这个函数的参数中，变量是什么**？

   ![](https://tvax3.sinaimg.cn/large/005IQUPRly1gjvsi7gunij30xi0jq422.jpg)

3.  **得到函数的递归结果，你该干嘛**？

   ​	因为是后序遍历，所以得到了公共祖先一定是最近的公共祖先！所以一旦某个时候right和left不为空说明找到了p,q.，就可以进行判断了

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left == None and right == None:
            return None
        elif left != None and right != None:
            return root
        elif left != None:
            return left
        else:
            return right
```

![img](https://pic.leetcode-cn.com/c44f8946548954a2513f7d72e20be260c36c157b506749c788afce1e7bd3416c-Picture1.png)

![img](https://pic.leetcode-cn.com/55f7683ceee27def129a50c9a26305e56b25175dbd3da55983b5848145559354-Picture2.png)

![img](https://pic.leetcode-cn.com/0c3217c102953090030aec857ef2e1e96672b38c450a90356a3e64f0dfc97af2-Picture3.png)

![img](https://pic.leetcode-cn.com/f137a75004bf105ae2f9d2987d3d75c0d0cbddfda54126e549b5a3a99b06a6ef-Picture4.png)

![img](https://pic.leetcode-cn.com/3334d8bc74cad490584a03ca6e6637f4d431626f75ca589710d6a382fe9ab06b-Picture5.png)

![img](https://pic.leetcode-cn.com/fd6ef030cf8acac250792828c04df471ccab669d4153b49b934bc4cc3517efcf-Picture6.png)

![img](https://pic.leetcode-cn.com/e03f2505635e77816e12bdfd2ce5c1c4ace3d2dfa2a0e10eefe683e11e88c98b-Picture7.png)

![img](https://pic.leetcode-cn.com/a9cf21e0a271c74af5ab00e39da09d485de8a3dabbfaa6d6cd2a2a1c7f60d2a8-Picture8.png)

![img](https://pic.leetcode-cn.com/6540e7106efa4461cb19c21a682e9b7c9bd33367d6c5a8bd97982cc7bcec9ec3-Picture9.png)

![img](https://pic.leetcode-cn.com/d249c4379aee12e4a5bce4f20c4ad8b709ff35e358cfdb3255ed6d9c6dc4ae2c-Picture10.png)

![img](https://pic.leetcode-cn.com/fa87c46c8e8360cf3ab5ea852161ab5f9e4a2ca1b5ff6cd9e9ba0897dcbd455a-Picture11.png)

![img](https://pic.leetcode-cn.com/91287818231c969dcc8c69ac9c79197a9b29085d120b18b5230dda77d092f6d6-Picture12.png)

![img](https://pic.leetcode-cn.com/bf71136a0329cf5d48933cb7dc1d8c1bd0cec96c1ad13bcca97cea2f58d14fb5-Picture13.png)

![img](https://pic.leetcode-cn.com/68aced35d03027033c2552b35d477d700e38e7c01f8c1fa76b4cf8b0a1858d30-Picture14.png)

![img](https://pic.leetcode-cn.com/ddf6279a32122924d3608ad7fcdf3f518091da353a1961c0e0e1afaf51d09623-Picture15.png)

![img](https://pic.leetcode-cn.com/b4777e4a6ff72ed49356e20a0a897fd866bb3e4dfdb5e0c8fc1dc0f918029237-Picture16.png)

![img](https://pic.leetcode-cn.com/df510a1fe4750116a935e61ef63ad30a5092bfefe38845497ff9431b3656a793-Picture17.png)

![img](https://pic.leetcode-cn.com/0724b87055c4bc4d744ab64775e6eefa348777c0ea0b07a00ff917773f4b494e-Picture18.png)