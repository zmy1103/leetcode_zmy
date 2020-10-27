## 295 Find the Median of a Number Stream 

### 双堆问题：

一个最小堆用来找最小元素；一个最大堆，拿到最大元素。这种模式将一半的元素放在最大堆中，这样你可以从这一堆中秒找到最大元素。同理，把剩下一半丢到最小堆中，O(1)时间找到他们中的最小元素。通过这样的方式，这一大堆元素的**中位数**就可以从两个堆的堆顶拿到数字，从而计算出来。

```python
class MedianFinder:

    def __init__(self, capacity):
        """
        initialize your data structure here.
        """
        self.data = [None for _ in range(capacitiy+1)]

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

