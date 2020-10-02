[Numpy](https://numpy.org/)  
[Runoob-numpy-tutorial](https://www.runoob.com/numpy/numpy-tutorial.html)
***
### Ndarray  
```
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```  

### 數據類型對象(dtype)
用來描述與數據對應的內存運用
```
numpy.dtype(object, align, copy)
```  
### 基本屬性
ndarray.ndim 返回維度數  
ndarray.shape 行列數  
ndarray.size 元素總個數，shape 中n*m 的值  
ndarray.dtype 元素類型  
ndarray.itemsize 每個元素的大小  
ndarray.flags 返回內存信息  
***  
### 創建數組
創建指定形狀未初始化數組  
```
numpy.empty(shape, dtype = float, order = 'C')
```  
創建指定大小數組，以0填充元素  
```
numpy.zeros(shape, dtype = float, order = 'C')
```  
創建指定大小數組，以1填充元素  
```
numpy.ones(shape, dtype = None, order = 'C')
```  
從已有數組創建數組  
```
numpy.asarray(a, dtype = None, order = None)
```  
實現動態數組，接受buffer 輸入參數  
```
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```  
*buffer 是字符串時，Python3默認str是Unicode類型，所以要轉成bytestring要在str前加上b*

從iterable物件建立ndarray物件，返回一維數組
numpy.fromiter(iterable, dtype, count=-1)

從數值範圍創建數組
根據start 與 stop 的指定範圍及step設步長，生成ndarray
numpy.arange(start, stop, step, dtype)

創建一個等差數列的一維數組。
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

創建一個等比數列的一維數組。
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
----------------------------------------------------------------------
Numpy 切片和索引
跟python list 相似
 +整數數組索引/布爾索引/花式索引
----------------------------------------------------------------------
Broadcast
指numpy 對不同型狀的數組進行數值計算的方式，
a.shape==b.shape時，a*b為a,b對應位相乘，
形狀不同時則觸發broadcast 機制。
----------------------------------------------------------------------
疊代數組
numpy.nditer 提供訪問一或多個數組元素的方式。
nditer(a,  order =  'F', op_flags=['readwrite'])
默認疊代 traversal 是 read-only，如果有要修改，可用 op_flags 參數設為 read-write。
-----------------------------------------------------------------------
數組操作

#修改數組形狀
numpy.reshape 不改變數據下修改形狀
numpy.ndarray.flat 數組元素疊代器
numpy.ndarray.flatten 返回一份數組拷貝(一維)，對拷貝進行修改不會影響原始數據。
numpy.ravel 返回一份數組view，修改會影響原始數組。

#翻轉數組
numpy.transpose 轉置
numpy.ndarray.T 轉置
numpy.rollaxis(arr, axis, start) 將軸移動到一個特定位置
numpy.swapaxes(arr, axis1, axis2) 交換數組兩個軸

#修改數組維度
numpy.broadcast 返回一個broadcast後的物件
numpy.broadcast_to(array, shape, subok) 將數組廣播到新形狀上
numpy.expand_dims(arr, axis) 在指定位置插入新的軸來擴張數組形狀
numpy.squeeze(arr, axis) 從數組形狀刪除一維

#連接數組
numpy.concatenate((a1, a2, ...), axis) 沿指定軸連接多個相同形狀數組。
numpy.stack(arrays, axis) 沿新軸連接數組序列。
numpy.hstack stack變體，水平堆疊
numpy.vstack stack變體，垂直堆疊

#分割數組
numpy.split(ary, indices_or_sections, axis) 沿特定軸將數組分割為子數組。
numpy.hsplit 水平分割
numpy.vsplit 垂直分割

#數組元素的添加與刪除
numpy.resize(arr, shape) 返回指定大小的新數組，如果新數組大於原始數組，則包含原始數組中的元素拷貝。
numpy.append(arr, values, axis=None) 在數組末尾添加值
numpy.insert(arr, obj, values, axis)  沿給定軸在數組中插入值，如果未提供軸，則數組會被展開。
Numpy.delete(arr, obj, axis) 返回從輸入數組刪除指定子數組的新數組，如未提供軸，輸入數組將展開。
numpy.unique(arr, return_index, return_inverse, return_counts) 去除數組中重複元素
-----------------------------------------------------------------------
位運算
bitwise_and 二進位取and
bitwise_or 二進位取or
invert 二進位取反
left_shift 二進位向左移位，後面補0
right_shift 二進位向右移位，前面補0
*也可用 '&', '~', '|', '^' 進行計算
-----------------------------------------------------------------------
#string function
numpy.char.add() 依次對兩個數組的元素進行字符串連接。
numpy.char.multiply() 多重連接
numpy.char.center(str , width,fillchar) 將字符串居中，並使用特定字符在左右側填充
numpy.char.capitalize() 將字符串第一個字母轉換為大寫
numpy.char.title() 將字符串的每個單詞的第一個字母轉換為大寫
numpy.char.lower() 將數組每個元素轉為小寫，對每個元素調用str.lower
numpy.char.upper() 將數組每個元素轉為大寫，對每個元素調用str.upper
numpy.char.split() 使用指定分割符將字串進行分割，並返回數組，默認為空格
numpy.char.splitlines() 以換行符作為分割符來分割字符串，並返回數組，'\n', '\r', '\r\n'都可做為換行符
numpy.char.strip() 移除開頭或結尾處的特定字符
numpy.char.join() 用指定分割符來連接數組中的元素或字符串
numpy.char.replace() 使用新字符串替換字符串中的所有子字符串
numpy.char.encode() 對數組中每個元素調用str.encode，默認編碼為utf-8
numpy.char.decode() 對encode元素進行str.decode()解碼
------------------------------------------------------------------
數學function
numpy.around(a,decimals) 四捨五入
numpy.floor() 返回小於或等於之最大整數
numpy.ceil() 返回大於或等於之最小整數
------------------------------------------------------------------
算術function
np.add(), np.subtract(), np.multiply(), np.divide() 
numpy.reciprocal() 返回倒數
numpy.power() 冪
numpy.mod()/numpy.remainder() 取餘數
------------------------------------------------------------------
統計function
numpy.amin() 數組中沿指定軸的最小值
numpy.amax() 數組中沿指定軸的最大值
numpy.ptp() 數組中最大與最小值之差
numpy.percentile(a, q, axis)  指定百分位數
numpy.median() 中位數
numpy.mean() 算術平均數
numpy.average() 加權平均數
numpy.std() 標準差 std = sqrt(mean((x - x.mean())**2))
numpy.var() 方差 mean((x - x.mean())** 2)
------------------------------------------------------------
排序
numpy.sort(a, axis, kind, order)
kind默認為'quicksort'，可換'mergesort', 'heapsort'
numpy.argsort() 返回數組值從小到大的索引值
numpy.lexsort() 多序列排序
numpy.argmax()/numpy.argmin() 返回最小最大的索引值
numpy.nonzero() 返回數組中非零元素索引
numpy.where() 返回滿足指定條件元素索引
numpy.extract() 返回滿足條件的元素
-----------------------------------------------------------
view/copy
直接賦值不會創建copy，取用原始id()訪問，值跟形狀都會一起受影響。
view 數據的引用，對其進行修改，也會影響到原有值，但不影響形狀，內存為同一位置
1.numpy slice 返回view
2.調用ndarray 的view()
copy 是製作一份拷貝，對其修改，不會影響到原有值，內存位置不同
1.python slice 調用deepCopy()
2.調用ndarray的()
-----------------------------------------------------------
矩陣庫(Matrix)
numpy.matlib.empty(shape, dtype, order)
numpy.matlib.zeros()
numpy.matlib.ones()
numpy.matlib.eye()
numpy.matlib.identity()
numpy.matlib.rand()
----------------------------------------------------------
線性代數
numpy.dot()  =>dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
numpy.vdot()
numpy.inner()
numpy.matmul
numpy.linalg.det()
numpy.linalg.solve()
numpy.linalg.inv()
