'''
 Lập trình đọc vào từ bàn phím 2 giá trị a, b rồi
tính y = 15 x2+x+7.2 trong đó:
            x = (a+b)/3 nếu a < b
            x = 1.5172 nếu a = b
            x = (a - b) / (a^2 + b^2) nếu a > b
'''

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

x = 1.5172 if (a == b) else ((a + b) / 3 if a < b else (a-b) / (a * a + b * b))

print(f"y = {15 * x * x + x + 7.2}" )

