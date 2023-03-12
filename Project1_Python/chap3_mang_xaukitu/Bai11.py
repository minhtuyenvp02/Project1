'''
Bai 11: Tìm số lớn nhất trong ma trận hai chiều

'''

import numpy as np

MAX = 1000
while True:
    n = int(input("Nhập kích thước ma trận N x N: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = np.array(list(map(int, input("Nhập dãy số: ").split()[:n*n]))).reshape((n,n))

_max = max(arr[0])
for i in range(1,n):
    _max = max(_max, max(arr[i]))
print(arr)
print(f"Gia tri lon nhat tron ma tran la: {_max}")


