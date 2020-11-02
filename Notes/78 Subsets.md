## 78 Subsets 回溯真是写爽了

![img](https://pic2.zhimg.com/80/v2-0409666e91e94287c167ef81670d19a5_1440w.jpg?source=1940ef5c)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]#amazing
        return res
```

