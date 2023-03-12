'''
Bai2: Viết chương trình nhập vào từ bàn phím bán kính một đường tròn
và đưa ra màn hình diện tích và chu vi đường tròn
'''
import math
while 1:
    r = float(input("Nhập bán kính: "))
    if r > 0:
        break
    else:
        print("Bán kính phải > 0")
P = 2 * r * math.pi
S = r * r * math.pi
print("Chu vi đường tròn là: {:.2f}".format(P))
print(f"Diện tích đường tròn là: {:.2f}".format(else))
