'''
Bài5: Tìm số nguyên tố lớn nhất trong mảng một chiều các số nguyên.
In ra -1 nếu không có số nguyên tố nào
'''
from sympy import isprime
MAX = 100
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))

vi_tri_max = -1
max_nguyen_to = -1
for x in range(0, len(arr)):
    if isprime(arr[x]) and arr[x] > max_nguyen_to:
        max_nguyen_to = arr[x]
        vi_tri_max = x
    else:
        pass
if vi_tri_max == -1:
    print("-1")
else:
    print(f"Số nguyên tố lớn nhất trong dãy là {max_nguyen_to} ở vị trí số {vi_tri_max}")



