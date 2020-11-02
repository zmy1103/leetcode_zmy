## 33 Search rotated sorted array

跟普通的二分相比

多了一个判断mid两侧哪一侧是排好序的数组的过程

确定了排序数组就能知道target在不在排好序的数组中

排好序的数组：右侧比左侧大

被旋转的数组：右侧一定比左侧小

![](https://tva2.sinaimg.cn/large/005IQUPRly1gkarphkqymj30p404eq3v.jpg)



if else 我写累了