## 494  target-sum（0/1背包）

### 转换成0/1背包：

1. 首先定义数组动态规划的数组dp[i] [j] : 从数组中0-i个元素进行加减得到j的方法数量 
   - **dp[ i ] [ j ] = dp[ i - 1 ] [ j - nums[ i ] ] + dp[ i - 1 ] [ j + nums[ i ] ]**
2. 然后进行画表

![image.png](https://pic.leetcode-cn.com/05f8151bbb0f1818723710b2455695f01c33d75a38653eeee181ab61217e8f16-image.png)

### 用满二叉树来理解（回溯）：

不知道二叉树有没有堆那种heapq库，超出时间限制了

![](https://tvax1.sinaimg.cn/large/005IQUPRly1gkd93xpuyqj31hc0onqv5.jpg)

```python
class Solution:
    res = 0
    S = 0
    def backtrace(self, nums, s):
        if len(nums) == 0:#如果这个第六层了
            if s == self.S: 
                self.res += 1
            return
        max_sum = s + nums[0]
        min_sum = s - nums[0]
        self.backtrace(nums[1:], max_sum)
        self.backtrace(nums[1:], min_sum)
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        self.S = S
        self.backtrace(nums,0)
        return self.res
```

