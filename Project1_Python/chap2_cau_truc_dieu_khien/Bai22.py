x = float(input("Enter x: "))
eps = float(input("Enter error: "))

s = t = luy_thua = x
sign, giai_thua = -1, 1
i = 3
while t > eps:
    i += 2
    sign = -sign
    t = (luy_thua * x * x) / (giai_thua * i *(i-1))
    s += sign * t

print(f"Sin({x}) = {s} với sai số cho phép {eps}")
