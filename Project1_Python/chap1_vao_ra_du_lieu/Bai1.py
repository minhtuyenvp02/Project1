'''
Bài 1: Đọc tọa độ 3 điểm A,B,C và đưa ra diện tích tam giác ABC
'''

import math
A = {"x": float(input("Nhập hoành độ điểm A: ")),
        "y": float(input("Nhập tung độ điểm A: "))}
B = {"x": float(input("Nhập hoành độ điểm B: ")),
        "y": float(input("Nhập tung độ điểm B: "))}
C = {"x": float(input("Nhập hoành độ điểm C: ")),
        "y": float(input("Nhập tung độ điểm C: "))}
AB = math.sqrt((A["x"] - B["x"])**2 + (A["y"] - B["y"]) ** 2)
BC = math.sqrt((C["x"] - B["x"])**2 + (C["y"] - B["y"]) ** 2)
AC = math.sqrt((A["x"] - C["x"])**2 + (A["y"] - C["y"]) ** 2)

if (AB + BC > AC) and (AB + AC > BC) and (AC + BC > AB):
    p = (AB + BC + AC) / 2
    S = math.sqrt(p*(p-AB)*(p-BC)*(p-AC))
    print(f"Dien tich tam giac la: {S}")
else:
    print("Khong phai la tam giac")
