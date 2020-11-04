## 347 top-k-frequent-elements (Python Heap的实现)

[TOC]

堆结构就是一种完全二叉树。堆可分为最大堆和最小堆，区别就是父节点是否大于所有子节点。最大堆的父节点大于它的子节点，而最小堆中子节点大于父节点。

对于 topk 问题：最大堆求topk小，最小堆求 topk 大。

topk小：构建一个 k 个数的最大堆，当读取的数小于根节点时，替换根节点，重新塑造最大堆
topk大：构建一个 k 个数的最小堆，当读取的数大于根节点时，替换根节点，重新塑造最小堆

![img](https://img-blog.csdn.net/2018091712014232)

### 可以用list来表示

```python
按照层序遍历顺序将每个节点上的值存放在数组中。父节点和子节点之间存在如下的关系：
parent = int((i-1) / 2)    # 取整
left = 2 * i + 1
right = 2 * i + 2
#其中i表示数组中的索引，如果left、right的值超出了数组的索引，则表示这个节点是不存在的。
```

![img](https://img-blog.csdn.net/20180917194848174)

### 往堆中插入值，sift-up操作：

![img](https://img-blog.csdn.net/20180917200043958)

把新加入的节点放在最后一层的最后一个叶子节点上，也就是list直接append

然后与父节点比较大小：>父节点得值，交换位置，递归向上，直到根节点

### 获取或删除根节点，sift-down操作

![img](https://img-blog.csdn.net/20180917200108791)

弹出根节点之后，为了维持堆得形状，先将最后一个位置得值放到根节点上，再递归向下比较

交换位置要满足几个条件条件，比如跟左子节点交换的条件：

- 存在左子节点，
- 左子节点大于右子节点，
- 左子节点大于父节点

### 最大堆实现

```python
def sifup(ndx):#新插入节点下标
    if ndx>0:
        parent = int((ndx-1)/2)#父节点坐标
       	if 新插入节点得值 > 父节点的值：
        	交换两个值的位置
            递归siftup(parent)
def sifdown(ndx):
    left = 2 * ndx + 1
    right = 2 * ndx + 2
    largest = ndx
    if left< 最大长度 and 左孩子比较大 and 左孩子比右孩子大：#有左孩子
    	最大值变成了左孩子
     elif 有右孩子 and 右孩子最大
    
    如果确定发生了交换：
    	和对应位置的值进行交换
        递归进行下一次下沉
```

### 最小堆实现

```python
def _siftup(self, index):
        if index > 0:
            parent = int((index - 1) / 2)
            if self._elements[parent] > self._elements[index]:
                self._elements[parent], self._elements[index] = self._elements[index], self._elements[parent]
                self._siftup(parent)
def _siftdown(self, index):
     if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < self._count and right < self._count \
                and self._elements[left] <= self._elements[right] \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)
            elif left < self._count and right < self._count \
                and self._elements[left] >= self._elements[right] \
                and self._elements[right] <= self._elements[index]:
                self._elements[right], self._elements[index] = self._elements[index], self._elements[right]
                self._siftdown(left)

            if left < self._count and right > self._count \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)
```

###  Python中的heapq模块

这个模块提供了的堆是一个最小堆，索引值从0开始。而很多教材中都使用最大堆作为教学的例子，因为其排序是稳定的，而最小堆排序是不稳定的。
**Python中创建一个堆可以直接使用list的创建方式H = [], 或者使用heapify()函数将一个存在的列表转为堆。**

这个模块提供了下面几种堆的操作：

- **heapq.heappush(heap, item)**
  往堆中插入一个值，同时要保持为最小堆。

- **heapq.heappop(heap)**
  返回堆中的最小值，并把它从堆中删除，同时保持为最小堆；如果堆为空，发生 IndexError。直接通过heap[0]可以获取最小值并不从堆中把它删除。

- **heapq.heappushpop(heap, item)**
  向堆中插入值后再弹出堆中的最小值，这个函数的速度比直接使用heappush() 和heappop()的效率更加高。

- **heapq.heapreplace(heap, item)**
  弹出和返回堆中的最小值再插入一个新的值。堆的大小没有改变。如果堆为空，产生 IndexError。
  这一个操作也比直接使用heappush() 和heappop()的效率更加高，尤其适合使用在固定堆大小不变的情况。
  与上一个函数相比，这个函数返回的值可能要比将要插入到堆的值大。

- **heapq.heapify(x)**
  将一个list转为最小堆，线性时间复杂度，O(n).

## 347  题解：

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root):
            print("进入下沉过程")
            if root < len(arr):
            	left = 2 * root + 1
            	right = 2 * root + 2
            print(str(left)+"  "+str(right))
            if left < len(arr) and right < len(arr) and arr[left][1] <= arr[right][1]   and arr[left][1]  <= arr[root][1] :#左右孩子都在，左孩子是三者中最小的
                arr[left], arr[root] = arr[root], arr[left]
                print("#左右孩子都在，左孩子是三者中最小的")
                sift_down(arr, left)
            elif left < len(arr) and right < len(arr) and arr[left][1]  >= arr[right][1]   and arr[right][1]  <= arr[root][1] :#右孩子最小
                arr[right], arr[root] = arr[root], arr[right]
                print("#左右孩子都在，右孩子是三者中最小的")
                sift_down(arr, right)
            elif left < len(arr) and right >= len(arr) and arr[left][1] <= arr[root][1] :#没有右孩子 左孩子小
                print(arr[left])
                arr[left], arr[root] = arr[root], arr[left]
                sift_down(arr, left)
        def sift_up(arr, child):
            if child > 0:
                parent = int((child - 1) / 2)
                if arr[parent][1]>arr[child][1]:
                    arr[parent], arr[child] = arr[child], arr[parent]
                    sift_up(arr, parent)
            
        stat = collections.Counter(nums)
        stat = list(stat.items())
        print(stat)
        heap = []
        
       	#构建规模为k+1的最小堆，新元素加入堆尾，上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1)#参数是存放堆的list和新加入节点的坐标
        print(heap)
        #维护规模为k+1的堆。如果新元素大于堆顶，下沉
       	for i in range(k, len(stat)):
            print(stat[i])
            if stat[i][1] > heap[0][1]:
                heap[0] = stat[i]
                sift_down(heap, 0)#参数是堆名+开始下沉的位置，
            print(heap)
        return [item[0] for item in heap]
```

stat = collections.Counter(nums)

stat = list(stat.items())

**[collections.Counter（）](https://docs.python.org/2/library/collections.html#collections.Counter)**
计数器是一个将元素存储为字典键的容器，它们的计数存储为字典值。