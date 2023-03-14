'''
Bài 21: Nhập n, x tính n căn bậc 2 lồng nhau của x
'''
import math
x = int(input(">> "))
n = int(input(">> "))

S = 0
for i in range(0, n):
    S = math.sqrt(S + x)

print(S)
