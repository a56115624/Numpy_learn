import numpy as np
# 準備測試資料
arr1 = np.array([
    [1,2,3],
    [4,5,6]
]) #2*3
arr2 = np.array([
    [7,8,9],
    [10,11,12]
])# 2*3
# 合併第一個維度
# result = np.vstack((arr1,arr2))
# print(result)

"""
4x3
[1,2,3]
[4,5,6]
[7,8,9]
[10,11,12]
"""
# 合併第二維度
result2 = np.hstack((arr1,arr2))
print(result2)
""" 
2x6
[1,2,3,7,8,9]
[4,5,6,10,11,12]

"""