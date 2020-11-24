# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:57:17 2020
#PAT 1147 Heaps
@author: Wenmo
"""

def is_heap():#根据层次遍历序列 判断是不是个堆 是个啥堆 并且输出结果
    

    print("Max Heap")
    preorder()
    return 1#大顶堆
    return 2#小顶堆
    return 0#不是个堆
def preorder(line):#给定层次遍历序列 返回后序遍历并输出
    return 

#读入数据

#进行判断并读出

data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
num_heap = data[0]#要判断的堆得个数
num_each_heap = data[1]#每个堆的个数
all_heap = [[0 for _ in range(num_each_heap)] for _ in range(num_heap)]
count = 2
for i in range(num_heap):
    for j in range(num_each_heap):
        all_heap[i][j] = data[count]
        count += 1
    is_heap(all_heap[i])#判断是不是堆 并且输出