'''
Bài1: Giải phương trình f(x)=0 trên đoạn [a,b]
f(x) = x^3 - x - 1
'''
import math
def f(x:float) -> float:
    return x ** 3 - x - 1
a,b,eps = 1.0,2.0,1.0e-6

while True:
    c = (a+b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    if math.fabs(b-a) < eps:
        break
    else: pass
print("Nghiệm là: {:.6f}".format((b+a)/2))
