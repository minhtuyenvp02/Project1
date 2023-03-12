'''
Bai 9: Liệt kêt tần suất xuất hiện của các phần tử trong mảng
'''

# CODE PYTHON
import numpy as np
MAX = 1000
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))

cnt = np.zeros(1000000)
for x in arr:
    cnt[x] += 1
arr1 = list(set(arr))
for i in arr1:
    print(f"Phần tử {i} có tần xuất xuất hiện là {int(cnt[i])}")
