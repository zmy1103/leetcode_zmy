## 1462 course-schedule-iv

终于蹲到了直接使用图的代码了

```python
class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
		self.graph = collections.defaultdict(list)
        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])
        return [self.dfs(query[0], query[1] for query in queries)]
    def dfs(self, start, end):
        if start == end:
            return True
        return any(self.dfs(nxt, end) for nxt in self.graph[start])
```

