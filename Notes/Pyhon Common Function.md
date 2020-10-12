## Pyhon Common Function

- #### enumerate() 函数

  - 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

  - ```
    enumerate(sequence, [start=0])
    ```

  - sequence -- 一个序列、迭代器或其他支持迭代对象。

  - start -- 下标起始位置。

  - 返回 enumerate(枚举) 对象。

  - ```python
    >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    
    >>>seq = ['one', 'two', 'three']
    >>> for i, element in enumerate(seq):
    ...     print i, element
    ```

    