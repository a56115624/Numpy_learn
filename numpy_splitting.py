import re
import numpy as np 
#準備測試資料
arr = np.array([
    [2,4,6,8,10,12],
    [1,3,5,7,9,11]
]) # 2x6




# 根據第一個維度切割
# result = np.vsplit(arr,2)
# print(result)
""" 
1x6
[2,4,6,8,10,12]
1x6
[1,3,5,7,9,11]
"""
# 根據第二個維度切割
result = np.hsplit(arr,2)
print(result)
""" 
    2x3
    [[2,4,6],[1,3,5]]
    2x3
    [8,10,12],[7,9,11]
"""