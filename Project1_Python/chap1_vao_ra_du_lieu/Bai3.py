'''
Bài 3: Viết chương trình nhập vào từ bàn phím một giá trị thực.
 Hãy đưa ra diện tích của các hình tròn, vuông,
  tam giác đều có chu vi bằng giá trị vừa nhập.
'''

import math
while 1:
    r = float(input("Nhập gia tri: "))
    if r > 0:
        break
    else:
        print("Gia tri nay phai  > 0")
print(f"Chu vi hinh tron la: {:.2f}".format(2 * a * PI))
print(f"Chu vi tam giac deu la: {:.2f}".format(3 * a))
print(f"Chu vi hinh vuong la: {:.2f}".format(4 * a))
