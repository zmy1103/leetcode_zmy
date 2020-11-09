# Leetcode刷题笔记

Begin_Date:2020-10-12		——zmy

![](https://tva1.sinaimg.cn/large/005IQUPRly1gjnsqp9xqij30j60arq3h.jpg)

## Practice：

#### Labels：

- Difficulty level:
  - Easy
  - Medium
  - Hard
- Subject with notes:⭐
- One pass: √
- Record it for your boyfriend: ws

#### Question Types:

- Grammar training 
  - Basic exercises
    - Array
    - Queue
    - Binary tree
    - Tree traversal
    - Heaps
  - Math question
  - ingenuity
- Elementary Algorithm
  - Dynamic programming
  - Backtracking
  - Divide-and-Conquer Algorithm
- Sort and find
  - Binary Search

- Advanced algorithm
- Others
  - Regular expression

#### Learning materials：

- https://www.zhihu.com/question/36738189 LeetCode按照怎样的顺序来刷题比较好？
- https://labuladong.gitbook.io/algo/ labuladong 的算法小抄

#### Practice record：

| Number | Difficulty | Problem                                                      | ♥    | Date       | Category                                 | Method-TimeComplexity | Remark                                                       | TODO                                    |
| :----: | :--------: | ------------------------------------------------------------ | ---- | ---------- | ---------------------------------------- | :-------------------: | ------------------------------------------------------------ | --------------------------------------- |
|   17   |   Medium   | [Ceiling of a Number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | √    | 2020/11/2  | Backtracking                             |       O(3m×4n)        |                                                              |                                         |
|   23   |    Hard    | [merge-k-sorted-lists](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | ⭐    | 2020/11/3  | Merge sort,Heap                          |                       |                                                              |                                         |
|   33   |   Medium   | [Search rotated sorted array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | ⭐    | 2020/11/2  | Binary search                            |        O(logn)        | [33Search rotated sorted array](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/33%20Search%20rotated%20sorted%20array.md) |                                         |
|   34   |   Medium   | [Find the first and last position of an element in a sorted array](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | √    | 2020/11/1  | Binary search                            |       O(log2n)        |                                                              |                                         |
|   38   |    Easy    | [Appearance array](https://leetcode-cn.com/problems/count-and-say/) | ⭐    | 2020/10/12 | Regular expression                       |         O(n)          | [regular-expression](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/38%20Appearance_Array.md) | --                                      |
|   39   |   Medium   | [Combined sum](https://leetcode-cn.com/problems/combination-sum/) | ⭐    | 2020/10/30 | Backtracking                             |         O(S)          | [39 Combined sum](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/39%20Combined%20sum.md) |                                         |
|   46   |   Medium   | [Full array](https://leetcode-cn.com/problems/permutations/) | ⭐    | 2020/10/27 | Backtracking                             |       O(n * n!)       | [46 Full array](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/46%20Full%20array.md) | 回溯还是有点问题                        |
|   51   |    Hard    | [Queen N](https://leetcode-cn.com/problems/n-queens/)        |      | 2020/10/27 | Backtracking                             |                       |                                                              |                                         |
|   78   |   Medium   | [Subsets](https://leetcode-cn.com/problems/subsets/)         | ⭐ws  | 2020/11/1  | DFS,Backtracking                         |      O(n * 2^n)       | [78 Subsets](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/78%20Subsets.md) | ggggreat                                |
|   81   |   Medium   | [Search rotated sorted array Ⅱ](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/) | √    | 2020/11/2  | Binary search                            |        O(logn)        |                                                              | lj题目                                  |
|   90   |   Medium   | [Subsets Ⅱ](https://leetcode-cn.com/problems/subsets-ii/)    | √    | 2020/11/2  | DFS,Backtracking                         |      O(n * 2^n)       |                                                              |                                         |
|  102   |    Easy    | [binary-tree-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) | √    | 2020/11/4  | Tree traversal                           |         O(n)          |                                                              |                                         |
|  105   |   Medium   | [Construct a binary tree from preorder and middle order traversal sequence](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | √    | 2020/10/22 | Recursion,Binary tree                    |         O(n)          |                                                              |                                         |
|  106   |   Medium   | [Traverse the sequence from the middle order and the post order to construct a binary tree](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | √    | 2020/10/23 | Tree traversal                           |         O(n)          |                                                              |                                         |
|  111   |    Easy    | [.二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) | √    | 2020/10/30 | BFS                                      |       BFS,Queue       |                                                              | 讲道理，效率好低                        |
|  114   |   Medium   | [Expand the binary tree to a list](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/) | ⭐ws  | 2020/10/16 | Recursion，Stack，Binary tree            |         O(n)          | [114 Expand the binary tree to a list](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/114%20Binary%20tree%20expands%20into%20linked%20list.md) |                                         |
|  116   |   Medium   | [Fill the right pointer of the binary tree](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/) | ⭐ws  | 2020/10/19 | BFS, Recursion,Queue                     |         O(n)          | [116 next](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/116%20Fill%20the%20next%20right%20node%20pointer%20of%20each%20node.md) |                                         |
|  117   |   Medium   | [Fill the right pointer of the binary treeⅡ](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/) | √    | 2020/10/20 | Same as above, Collections               |         O(n)          |                                                              |                                         |
|  215   |   Medium   | [Kth largest element in the array](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | ⭐    | 2020/10/13 | Array,Queue,Divide-and-Conquer Algorithm |         O(n)          | [Partition && Queue](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/215%20Partition%20%26%26%20Queue.md) | 联系二叉树和排序                        |
|  226   |    Easy    | [Flip binary tree]()                                         | ⭐    | 2020/10/15 | Recursion，Iteration，Binary tree        |         O(n)          | [226 Interation](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/226%20Iteration.md) | 队列                                    |
|  236   |   Medium   | [Nearest common ancestor of binary tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | ⭐ws  | 2020/10/14 | Recursion,Binary tree                    |         O(n)          | [236 Recursion](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/236%20Recursion.md) | 给ws讲出来                              |
|  239   |    Hard    | [Maximum sliding window](https://leetcode-cn.com/problems/sliding-window-maximum/) |      | 2020/10/25 | Heaps                                    |                       |                                                              |                                         |
|  295   |    Hard    | [Find the Median of a Number Stream](https://leetcode-cn.com/problems/find-median-from-data-stream/) |      | 2020/10/25 | Two Heaps                                |                       |                                                              |                                         |
|  322   |   Medium   | [Change exchange](https://leetcode-cn.com/problems/coin-change/) | ⭐    | 2020/10/26 | DP                                       |         O(n)          | [322 Change exchange(DP)](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/322%20Change%20exchange(DP).md) | 喵喵喵？我的时间复杂度怎么回事          |
|  347   |   Medium   | [top-k-frequent-elements](https://leetcode-cn.com/problems/top-k-frequent-elements/) | ⭐    | 2020/11/2  | Heaps                                    |       O(nlogk)        | [347 top-k-frequent-elements (Python Heap的实现)](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/347%20top-k-frequent-elements%20(Python%20Heap%E7%9A%84%E5%AE%9E%E7%8E%B0).md) | 终于学会堆了                            |
|  378   |   Medium   | [kth-smallest-element-in-a-sorted-matrix](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/) | √    | 2020/11/3  | Heap, MergeSort                          |       O(nlogk)        |                                                              | 写题解了                                |
|  416   |   Medium   | [partition-equal-subset-sum](https://leetcode-cn.com/problems/partition-equal-subset-sum/) | ⭐    | 2020/11/4  | DP                                       |                       |                                                              |                                         |
|  480   |    Hard    | [Median of sliding window](https://leetcode-cn.com/problems/sliding-window-median/) |      | 2020/10/25 | Two Heaps                                |                       |                                                              |                                         |
|  494   |   Medium   | [target-sum](https://leetcode-cn.com/problems/target-sum/)   | ⭐    | 2020/11/4  | DP, 0/1Package                           |        O（n）         | [494 target-sum]()                                           | 第一个背包问题,回溯的写法可以在注意一下 |
|  518   |   Medium   | [Change exchange Ⅱ](https://leetcode-cn.com/problems/coin-change-2/) | ⭐    | 2020/10/26 | DP                                       |        O（n）         | [518 Change exchange Ⅱ)](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/518%20Change%20exchange%E2%85%A1.md) |                                         |
|  652   |   Medium   | [Find duplicate subtrees](https://leetcode-cn.com/problems/find-duplicate-subtrees/) | ⭐    | 2020/10/23 | Recursion,Binary tree                    |         O(n2)         | [652 Find duplicate subtrees ](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/652%20Find%20duplicate%20subtrees.md) | 效率可以优化                            |
|  654   |    Easy    | [Largest binary tree](https://leetcode-cn.com/problems/maximum-binary-tree/) | √    | 2020/10/21 | Recursion,Binary tree                    |       *O*(*n*2)       |                                                              |                                         |
|  692   |   Medium   | [Top K high frequency words](https://leetcode-cn.com/problems/top-k-frequent-words/) | ⭐    | 2020/11/3  | Heap,Sort                                |       O(nlogn)        | [692  K high frequency words](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/692%20Top%20K%20high%20frequency%20words.md) | 生日快乐                                |
|  704   |    Easy    | [Binary search](https://leetcode-cn.com/problems/binary-search/) | ⭐    | 2020/11/1  | Binary search                            |       O(log*N*)       | [704 Binary search](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/704%20Binary%20Search.md) |                                         |
|  752   |  So Hard   |                                                              |      |            |                                          |                       |                                                              |                                         |
|  973   |   Medium   | [‘K’ Closest Points to the Origin](https://leetcode-cn.com/problems/k-closest-points-to-origin/) | √    | 2020/11/3  | Heap                                     |       O(nlogn)        |                                                              | 我是个小天才                            |
|  997   |    Easy    | [find-the-town-judge](https://leetcode-cn.com/problems/find-the-town-judge/) | √    | 2020/11/5  | Math.Graph                               |         O(n)          |                                                              | 数学题                                  |
|  1636  |    Easy    | [Sort the array in ascending order by frequency](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency/) | √    | 2020/11/3  | Heap,Sort                                |       O(nlogn)        |                                                              |                                         |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                         |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                         |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                         |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                         |

## Notes：

- common functions
  - python 
- algorithm
- [背包问题九讲](https://www.kancloud.cn/kancloud/pack/70124)

## Tips:

- 全局变量连续跑会存在没有清空的问题，所以可以在使用之前调用一个构造函数来初始化
- ![20190624173156.jpg](https://pic.leetcode-cn.com/cde64bf682850738153e6c76dd3f6fb32201ce3c73c23415451da1eead9eb7cb-20190624173156.jpg)

## Contests:

| Contest   | Date     | Result |
| --------- | -------- | ------ |
| 2020/12/5 | PAT 甲级 |        |
|           |          |        |
|           |          |        |

