## Partition && Queue（哭了 好多坑 sort不香吗）

### partition算法：

- 首先从无序数组中选出枢轴点 pivot，然后通过一趟扫描，以 pivot 为分界线将数组中其他元素分为两部分，使得左边部分的数小于等于枢轴，右边部分的数大于等于枢轴（左部分或者右部分都可能为空），最后返回枢轴在新的数组中的位置。

- ```python
  #简单实现，相当于快排
  def partition(L, first, last):
      pivot = L[first]
      while first < last:
          while first < last and L[last] >= pivot:
              last -= 1
          L[first] = L[last]
          while first < last and L[first] <= pivot:
              first += 1
          L[last] = L[first]
      L[first] = pivot
      return first
  ```
```
  
- partition应用：快排

- ```python
  def Quicksort(L, first, last):
      if first >= last-1:
          return
     	pos = partition(L, first, last)
  	Quicksort(L, first, pos)
  	Quicksort(L, pos+1, last)
```

  ### partition()函数

- 用来根据指定的分隔符将字符串进行分割。

  如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

- ```python
  str.partition(str)
  
  eg:
  str = "www.runoob.com"
  print str.partition(".")
  
  ('www', '.', 'runoob.com')
  ```

  ### patrition应用进阶

- 将一个数组按照某个target值分为三部分，使得左边部分的值小于 target，中间部分等于 target，右边部分大于 target

- 用**三个指针**将数组分为四个部分，通过一次扫描最终将数组分为 <，=，> 的三部分

- ```python
  def three_way_partition(L, target):
      small, scan, big = 0, 0, len(L)-1
      while scan < big:
          if L[scan] < target:
              L[small], L[scan] = L[scan], L[small]
              small += 1
              scan += 1
  		elif L[scan] < target:
              L[big], L[scan] = L[scan], L[big]
              big -= 1
              scan += 1
          else:
              scan += 1
  ```

- 图

![](https://tvax1.sinaimg.cn/large/005IQUPRly1gjp0tdcp25j310i0ki0sv.jpg)

### Queue方法解决这个题

- 优先队列的思路是很朴素的。因为第 K 大元素，其实就是整个数组排序以后后半部分最小的那个元素。因此，我们可以维护一个有 K 个元素的最小堆：

  1、如果当前堆不满，直接添加；

  2、堆满的时候，如果新读到的数小于等于堆顶，肯定不是我们要找的元素，只有新都到的数大于堆顶的时候，才将堆顶拿出，然后放入新读到的数，进而让堆自己去调整内部结构。

  

  优先队列的写法就很多了:

  假设数组有 len 个元素。

  思路1：把 len 个元素都放入一个最小堆中，然后再 pop() 出 len - k 个元素，此时最小堆只剩下 k 个元素，堆顶元素就是数组中的第 k 个最大元素。

  思路2：把 len 个元素都放入一个最大堆中，然后再 pop() 出 k - 1 个元素，因为前 k - 1 大的元素都被弹出了，此时最大堆的堆顶元素就是数组中的第 k 个最大元素。

- ```python
  from typing import List
  import heapq
  
  class Solution:
      # 使用容量为 k 的小顶堆
      # 元素个数小于 k 的时候，放进去就是了
      # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换
  
      def findKthLargest(self, nums: List[int], k: int) -> int:
          size = len(nums)
          if k > size:
              raise Exception('程序出错')
          L = []
          for index in range(k):
              # heapq 默认就是小顶堆
              heapq.heappush(L, nums[index])#L就是堆的实现
  
          for index in range(k, size):
              top = L[0]
              if nums[index] > top:
                  # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
                  heapq.heapreplace(L, nums[index])
          # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
          return L[0]
  ```

  

  ### Python中的heapq模块

  这个模块提供了的堆是一个最小堆，索引值从0开始.
  Python中创建一个堆可以直接使用list的创建方式H = [], 或者使用heapify()函数将一个存在的列表转为堆。

  这个模块提供了下面几种堆的操作：

  ```python
  heapq.heappush(heap, item)
  ```

  往堆中插入一个值，同时要保持为最小堆。

  ```python
  heapq.heappop(heap)
  ```


  返回堆中的最小值，并把它从堆中删除，同时保持为最小堆；如果堆为空，发生 IndexError。直接通过heap[0]可以获取最小值并不从堆中把它删除。

  ```python
  heapq.heappushpop(heap, item)
  ```


  向堆中插入值后再弹出堆中的最小值，这个函数的速度比直接使用heappush() 和heappop()的效率更加高。

  ```python
  heapq.heapreplace(heap, item)
  ```

  弹出和返回堆中的最小值再插入一个新的值。堆的大小没有改变。如果堆为空，产生 IndexError。
  这一个操作也比直接使用heappush() 和heappop()的效率更加高，尤其适合使用在固定堆大小不变的情况。
  与上一个函数相比，这个函数返回的值可能要比将要插入到堆的值大。

  ```python
  heapq.heapify(x)
  ```


  将一个list转为最小堆，线性时间复杂度，O(n).

