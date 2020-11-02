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

| Number | Difficulty | Problem                                                      | ♥    | Date       | Category                                 | Method-TimeComplexity | Remark                                                       | TODO                           |
| :----: | :--------: | ------------------------------------------------------------ | ---- | ---------- | ---------------------------------------- | :-------------------: | ------------------------------------------------------------ | ------------------------------ |
|   17   |   Medium   | [Ceiling of a Number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/) | √    | 2020/11/2  | Backtracking                             |       O(3m×4n)        |                                                              |                                |
|   33   |   Medium   | [Search rotated sorted array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | ⭐    | 2020/11/2  | Binary search                            |        O(logn)        | [33Search rotated sorted array]()                            |                                |
|   34   |   Medium   | [Find the first and last position of an element in a sorted array](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | √    | 2020/11/1  | Binary search                            |       O(log2n)        |                                                              |                                |
|   38   |    Easy    | [Appearance array](https://leetcode-cn.com/problems/count-and-say/) | ⭐    | 2020/10/12 | Regular expression                       |         O(n)          | [regular-expression](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/38%20Appearance_Array.md) | --                             |
|   39   |   Medium   | [Combined sum](https://leetcode-cn.com/problems/combination-sum/) | ⭐    | 2020/10/30 | Backtracking                             |         O(S)          | [39 Combined sum]()                                          |                                |
|   46   |   Medium   | [Full array](https://leetcode-cn.com/problems/permutations/) | ⭐    | 2020/10/27 | Backtracking                             |       O(n * n!)       | [46 Full array]()                                            | 回溯还是有点问题               |
|   51   |    Hard    | [Queen N](https://leetcode-cn.com/problems/n-queens/)        |      | 2020/10/27 | Backtracking                             |                       |                                                              |                                |
|   78   |   Medium   | [Subsets](https://leetcode-cn.com/problems/subsets/)         | ⭐ws  | 2020/11/1  | DFS,Backtracking                         |      O(n * 2^n)       | [78 Subsets]()                                               | ggggreat                       |
|   81   |   Medium   | [Search rotated sorted array Ⅱ](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/) | √    | 2020/11/2  | Binary search                            |        O(logn)        |                                                              | lj题目                         |
|   90   |   Medium   | [Subsets Ⅱ](https://leetcode-cn.com/problems/subsets-ii/)    | √    | 2020/11/2  | DFS,Backtracking                         |      O(n * 2^n)       |                                                              |                                |
|  105   |   Medium   | [Construct a binary tree from preorder and middle order traversal sequence](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | √    | 2020/10/22 | Recursion,Binary tree                    |         O(n)          |                                                              |                                |
|  106   |   Medium   | [Traverse the sequence from the middle order and the post order to construct a binary tree](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | √    | 2020/10/23 | Tree traversal                           |         O(n)          |                                                              |                                |
|  111   |    Easy    | [.二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) | √    | 2020/10/30 | BFS                                      |       BFS,Queue       |                                                              | 讲道理，效率好低               |
|  114   |   Medium   | [Expand the binary tree to a list](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/) | ⭐ws  | 2020/10/16 | Recursion，Stack，Binary tree            |         O(n)          | [114 Expand the binary tree to a list](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/114%20Binary%20tree%20expands%20into%20linked%20list.md) |                                |
|  116   |   Medium   | [Fill the right pointer of the binary tree](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/) | ⭐ws  | 2020/10/19 | BFS, Recursion,Queue                     |         O(n)          | [116 next](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/116%20Fill%20the%20next%20right%20node%20pointer%20of%20each%20node.md) |                                |
|  117   |   Medium   | [Fill the right pointer of the binary treeⅡ](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/) | √    | 2020/10/20 | Same as above, Collections               |         O(n)          |                                                              |                                |
|  215   |   Medium   | [Kth largest element in the array](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | ⭐    | 2020/10/13 | Array,Queue,Divide-and-Conquer Algorithm |         O(n)          | [Partition && Queue](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/215%20Partition%20%26%26%20Queue.md) | 联系二叉树和排序               |
|  226   |    Easy    | [Flip binary tree]()                                         | ⭐    | 2020/10/15 | Recursion，Iteration，Binary tree        |         O(n)          | [226 Interation](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/226%20Iteration.md) | 队列                           |
|  236   |   Medium   | [Nearest common ancestor of binary tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | ⭐ws  | 2020/10/14 | Recursion,Binary tree                    |         O(n)          | [236 Recursion](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/236%20Recursion.md) | 给ws讲出来                     |
|  239   |    Hard    | [Maximum sliding window](https://leetcode-cn.com/problems/sliding-window-maximum/) |      | 2020/10/25 | Heaps                                    |                       |                                                              |                                |
|  295   |   Medium   | [Find the Median of a Number Stream](https://leetcode-cn.com/problems/find-median-from-data-stream/) |      | 2020/10/25 | Two Heaps                                |                       |                                                              |                                |
|  322   |   Medium   | [Change exchange](https://leetcode-cn.com/problems/coin-change/) | ⭐    | 2020/10/26 | DP                                       |         O(n)          | [322 Change exchange(DP)](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/322%20Change%20exchange(DP).md) | 喵喵喵？我的时间复杂度怎么回事 |
|  480   |    Hard    | [Median of sliding window](https://leetcode-cn.com/problems/sliding-window-median/) |      | 2020/10/25 | Two Heaps                                |                       |                                                              |                                |
|  518   |   Medium   | [Change exchange Ⅱ](https://leetcode-cn.com/problems/coin-change-2/) | ⭐    | 2020/10/26 | DP                                       |        O（n）         | [518 Change exchange Ⅱ)]()                                   |                                |
|  652   |   Medium   | [Find duplicate subtrees](https://leetcode-cn.com/problems/find-duplicate-subtrees/) | ⭐    | 2020/10/23 | Recursion,Binary tree                    |         O(n2)         | [652 Find duplicate subtrees ](https://github.com/zmy1103/leetcode_zmy/blob/master/Notes/652%20Find%20duplicate%20subtrees.md) | 效率可以优化                   |
|  654   |    Easy    | [Largest binary tree](https://leetcode-cn.com/problems/maximum-binary-tree/) | √    | 2020/10/21 | Recursion,Binary tree                    |       *O*(*n*2)       |                                                              |                                |
|  704   |    Easy    | [Binary search](https://leetcode-cn.com/problems/binary-search/) | ⭐    | 2020/11/1  | Binary search                            |       O(log*N*)       | [Binary search]()                                            |                                |
|  752   |  So Hard   |                                                              |      |            |                                          |                       |                                                              |                                |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                |
|        |            |                                                              |      |            |                                          |                       |                                                              |                                |

## Notes：

- common functions
  - python 
- algorithm

## Tips:

- 全局变量连续跑会存在没有清空的问题，所以可以在使用之前调用一个构造函数来初始化

## Contests:
