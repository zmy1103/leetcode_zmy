## Python Common Function

### enumerate() 函数

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


### combinations和permutations函数

![img](https://img-blog.csdn.net/20160909125902241?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![img](https://img-blog.csdn.net/20160909130004434?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

combinations方法重点在组合，permutations方法重在排列。

还有就是，combinations和permutations返回的是对象地址，原因是在python3里面，返回值已经不再是list,而是iterators（迭代器）, 所以想要使用，只用将iterator 转换成list 即可， 还有其他一些函数返回的也是一个对象，需要list转换，比如 list(map())等 。