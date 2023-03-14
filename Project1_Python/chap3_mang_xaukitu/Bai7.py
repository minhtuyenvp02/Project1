'''
Bài 7: Cho mảng 1 chiều các số nguyên.
Hãy viết hàm tìm ước chung lớn nhất
của tất cả các phần tử trong mảng
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

ucln = arr[0]
for x in arr:
    ucln = gcd(ucln, x)
print(ucln)
