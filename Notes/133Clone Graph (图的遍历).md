## 133Clone Graph (图的遍历)

图的遍历无非BFS，DFS

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        def dfs(node):
            #print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))         
            return clone
        return dfs(node)
```

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        lookup = {} 
        def bfs(node):
            if not node: return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone
        return bfs(node)
```

