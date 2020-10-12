## Regular expression

（参照题解

#### 四种方法：

1. 常规解法
   - 递归
   - 迭代
2. 使用正则表达式
   - 元素提取
   - 元素替换

#### 递归（一层一层倒着算

由于每次得到的数据都是来源于上一次的结果，所以我们可以假设得到了上次的结果，继而往后运算。这就运用到了递归。

```python
def countAndSay(self, n: int) -> str:
    if n == 1:
        return '1'#只有一层的时候
    s = self.countAndSay(n-1)#上n-1层的结果                                    
	i, res = 0, ''#res第n层
	for j, c in enumerate(s):对上一层的结果进行遍历
    	if c != s[i]:
        	res += str(j-i) + s[i]#后面使用 j - i 来统计相同元素的个数
        	i = j
	res += str(len(s) - i) + s[-1]  # 最后一堆元素
	return res
```
#### 迭代（就是一层一层正着算

```python
def countAndSay(self, n: int) -> str:
    res = '1'
    for _ in range(n-1):  # 控制循环次数 迭代n-1次
        i, tmp = 0, ''
        for j, c in enumerate(res):#同样的方法遍历某一层获得下一层的表示
            if c != res[i]:
                tmp += str(j-i) + res[i]
                i = j
        res = tmp + str(len(res) - i) + res[-1]
    return res
```

#### 提取元素（写的妙啊）

```python
def countAndSay(self, n: int) -> str:
    if n == 1:
        return '1'
    s = self.countAndSay(n-1)

    p = r'(\d)\1*'
    pattern = re.compile(p)
    res = [_.group() for _ in pattern.finditer(s)]  # 提取结果
    return ''.join(str(len(c)) + c[0] for c in res)  # join 内部的 str(len(c)) + c[0] for c in res 是生成器类型
```

字符串 (\d)\1* 可以用来匹配结果。这里用来提取连在一块的元素， 如 '111221'，提取出的元素是 res = ['111', '22', '1']。
然后再返回我们要组装的字符串。

#### 元素替换

```python
def countAndSay(self, n: int) -> str:
    res = '1'
    p = r'(\d)\1*'
    pattern = re.compile(p)
    for _ in range(n-1):
        res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)  # 替换
    return res
```

对于该句：res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)，还是拿上面的举例，对于 111221 的第一个匹配项 111，其中 group() 匹配的是 111（全局匹配），而 group(1) 匹配到的是 1 (第一个捕获组，三个 1 中的第一个)。
