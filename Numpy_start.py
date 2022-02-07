# 載入Numpy套件
import numpy as np
# 根據列表建立ndarray物件
ndarr = np.array([3,4,5])
# 簡單的觀察
# print(ndarr)
# print(ndarr.size) # 資料的數量


# 建立未指定資料的一維陣列
np.empty(3)
# 建立資料都是0的一維陣列
np.zeros(3)
# 建立資料都是1的一維陣列
np.ones(3)
# 建立連續資料的一維陣列
np.arange(10)


# 根據列表建立
np.array([
    [1,2],
    [3,2],
    [5,0]
])

# 建立資料未指定的二維陣列
np.empty([3,2])
# 建立資料都是0的二維陣列
a = np.zeros([3,2])
# 建立資料都是1的二維陣列
np.ones([3,2])



# 根據列表建立三維陣列
np.array([
    [
        [5,2,3],[1,5,8]
    ],[
        [3,5,4],[4,1,3]
    ]
])
# 建立資料未指定的三維陣列
np.empty([2,2,3])
# 建立資料表都是0的三維陣列
np.zeros([2,2,3])
