'''
bài 14: Tìm số có 3 chữ số abc thoả mãn abc = a^3 + b^3 + c^3
'''

for x in range(100, 1000, 1):
    a = int(x / 100)
    b = int(int(x % 100) / 10)
    c = x % 100 % 10
    if a * a * a + b * b * b + c * c * c == x:
        print(x)