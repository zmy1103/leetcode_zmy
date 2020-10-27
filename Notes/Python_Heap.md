## Python Heap的实现

[TOC]

### 可以用list来表示

```python
parent = int((i-1) / 2)    # 取整
left = 2 * i + 1
right = 2 * i + 2
#其中i表示数组中的索引，如果left、right的值超出了数组的索引，则表示这个节点是不存在的。
```

![img](https://img-blog.csdn.net/20180917194848174)

### 往堆中插入值，sift-up操作：