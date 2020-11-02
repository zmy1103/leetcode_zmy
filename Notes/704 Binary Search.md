## 704 Binary Search

### 二分查找框架

```java
int binarySearch(int[] nums, int target)
{
	int left = 0, right = ....;
	while(...){
	int mid = left + (right - left) / 2;
    if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        } 
	}
}
```

计算 mid 时需要防止溢出，代码中 `left + (right - left) / 2` 就和 `(left + right) / 2` 的结果相同，但是有效防止了 `left` 和 `right` 太大直接相加导致溢出。

### 梳理一下这些细节差异的因果逻辑：

**第一个，最基本的二分查找算法**：

```python
因为我们初始化 right = nums.length - 1
所以决定了我们的「搜索区间」是 [left, right]
所以决定了 while (left <= right)
同时也决定了 left = mid+1 和 right = mid-1
因为我们只需找到一个 target 的索引即可
所以当 nums[mid] == target 时可以立即返回
```

**第二个，寻找左侧边界的二分查找**：

```python
因为我们初始化 right = nums.length
所以决定了我们的「搜索区间」是 [left, right)
所以决定了 while (left < right)
同时也决定了 left = mid + 1 和 right = mid
因为我们需找到 target 的最左侧索引
所以当 nums[mid] == target 时不要立即返回而要收紧右侧边界以锁定左侧边界
```

**第三个，寻找右侧边界的二分查找**：

```python
因为我们初始化 right = nums.length
所以决定了我们的「搜索区间」是 [left, right)
所以决定了 while (left < right)
同时也决定了 left = mid + 1 和 right = mid
因为我们需找到 target 的最右侧索引
所以当 nums[mid] == target 时不要立即返回而要收紧左侧边界以锁定右侧边界
又因为收紧左侧边界时必须 left = mid + 1所以最后无论返回 left 还是 right，必须减一
```