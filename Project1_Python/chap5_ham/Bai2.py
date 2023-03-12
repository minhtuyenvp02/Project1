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

def khoang_cach(A:{}, B:{}) -> float:
    return math.sqrt((A["x"] - B["x"])**2 + (A["y"] - B["y"]) ** 2)
def check(a, b, c) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)
AB = khoang_cach(A, B)
AC = khoang_cach(A, C)
BC = khoang_cach(B, C)

if check(AB, AC, BC):
    p = (AB + BC + AC) / 2
    S = math.sqrt(p*(p-AB)*(p-BC)*(p-AC))
    print("Dien tich tam giac la: {:5.2f}".format(S))
else:
    print("Khong phai la tam giac")
