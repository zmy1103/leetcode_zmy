## 207  course-schedule

精妙绝伦图代码

```python
from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #入度为0 先学习
        #建立入度和后继节点的标记
        in_degree = [0 for _ in range(numCourses)]#入度数组
        adj = [set() for _ in range(numCourses)]#邻接表
        for two, one in prerequisites:
            in_degree[two] += 1
            adj[one].append(two)
        queue = deque()
        for i in range(numCourse):
            if in_degree[i] == 0:
                queue.append(i)
        counter = 0
       	while queue:
            top = queue.popleft()
            counter += 1
            for j in adj[top]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
       return counter == numCourses
```

