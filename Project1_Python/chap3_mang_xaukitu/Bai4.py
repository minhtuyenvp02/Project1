'''
Bài 4: Viết hàm đếm số lượng số nguyên tố nhỏ hơn 100 trong mảng
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
cnt = 0
for x in arr:
    if isprime(x) and x < 100:
        cnt += 1
print(f"Có {cnt} số nguyên tố < 100 trong dãy")
