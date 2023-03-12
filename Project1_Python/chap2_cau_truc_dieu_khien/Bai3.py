'''
Nhập và tính hàm f(x) =
'''
import math

x = float(input("Nhập x: "))
if x < 3:
    print(f"Result = {x * x + math.sin(2 * math.pi * x) + 1}")
elif x == 3:
    print(f"Result = {5}")
else:
    print(f"Result = {math.sqrt(x - 3) + math.log10(x * x -3)}")