'''
Bài 8: Tìm BCNN của mảng số nguyên
'''
from math import gcd
MAX = 100
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
def BCNN(a ,b):

    return int(a / gcd(a,b)) * b
bcnn = BCNN(arr[0], arr[1])
for x in arr:
    bcnn = BCNN(bcnn, x)

print(f"Bội chung nhỏ nhất của các phần tử trong dãy là {bcnn}")
