import math
ESP = 1e-04
x = float(input("Enter x (độ): "))

x = x * math.pi/180;
s = t = luy_thua = x
sign, giai_thua = -1, 1
i = 3
while t > ESP:
    luy_thua *= (x*x)
    giai_thua *= i*(i-1)
    t = luy_thua/giai_thua
    s += sign * t
    i += 2
    sign = -sign
print(f"Sin({x}) = {s} với sai số cho phép {ESP} tính theo code")
print(f"Sin({x}) = {math.sin(x)} tính theo hàm có sẵn")


