## 127 Word Laddar

经过提点，发现比较像图的广度优先遍历

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

### 我的错误写法:

```python
        queue = deque()
        all_word = []
        all_word.append(beginWord)
        queue.appendleft(beginWord)
        length = 1
        while queue:
            length += 1
            tmp = queue.pop()
            for i in wordList:
                if com(tmp,i) and i not in all_word:
                    if i == endWord:
                        return length
                    all_word.append(i)
                    queue.appendleft(i)
        return 0
```

这样会忽略掉 已存在的两个节点之间没出现过的边

错误改正：每次添加新边要把整个队列排空

### 改进点:

1. 每个单词去和其他单词比较是否只差一个字符时间复杂度O(N*wordLen)
2. 给每个单词建立一个哈希表的时间复杂度O(26*wordLen)           

### 双向BFS:

![image.png](https://pic.leetcode-cn.com/38dc5897de2b554ea606a92c5eada14b0e0030195334e9fd65943ed6d0f77c1d-image.png)

```python
from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        
        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)
        
		word_len = len(beginWord)
        step = 1
		while begin_visited:
            if len(begin_visited) > len(end_visited):#?????
                begin_visited, end_visited = end_visited, begin_visited
			next_level_visited = set()
            for word in begin_visited:
                word_list = list(word)
			for j in range(word_len):
                    origin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                return step + 1
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited
            step += 1
        return 0
```

