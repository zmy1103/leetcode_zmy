## 692 Top K high frequency words

### 方法一：排序

```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = list(count.keys())
        candidates.sort(key = lambda w: (-count[w], w))#按照字典倒序排列 当两个样本次数一样时，按字母排列
        return candidates[:k]
```

### 方法二：堆

```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]
```

