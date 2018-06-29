## 分析二分查找的边界

我们需要在数组shorter中找到一个切分点，使数组分为两部分（允许长度为零），
如竖线的位置：
```
|0|
|0|1|2|3|
```
可知切分点的个数为数组长度加一：``len(shorter)+1``

令切分点左侧元素的下标为``SLI``，右侧元素的下标为``SRI``。
当选择的切分点在数组最左侧，``SLI``为``-1``，``SRI``为``0``。
当选择的分割点在数组左右侧，``SLI``等于数组长度减一(``SLI = len(shorter)-1``)，
``SRI``等于数组长度(``SRI = len(shorter)``)

保障如上取值范围，二分查找``SLI``，则应在闭区间``[-1, len(shorter)-1]``中查找。
在闭区间执行二分查找，则退出条件为``Low > High``。取得``SLI``后，加``1``得到``SRI``

如此，不如在闭区间``[0, len(shorter)]``中二分查找``SRI``，然后减``1``得到``SLI``。
退出条件为``Low > High``。

## 分析两个数组的切分情况
```
LLI|LRI  ---|LRI  ---|LRI  LLI|LRI  LLI|---  LLI|LRI  LLI|---
SLI|SRI  SLI|---  SLI|SRI  SLI|---  ---|SRI  ---|SRI  SLI|SRI

LLI|---  ---|LRI
SLI|---  ---|SRI
```
证明最后两种情况不会出现。

```
# 设shorter长度为n，longer则最少为n。
LenOfShorter = n
LenOfLonger = n + x >= n
LenOfSum = LenOfShorter + LenOfLonger >= 2 * n
LenOfLeft = floor(LenOfSum / 2) >= n

#当切分shorter，使得所有shorter元素在右侧。
SLI = 0
LLI = LenOfLeft - (SLI + 1) - 1
# 所以 0 < LLI < LenOfLeft <= n
```
