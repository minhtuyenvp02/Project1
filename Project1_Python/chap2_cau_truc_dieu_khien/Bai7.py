#Giải phương trình ax^2 + bx + c =0
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0 and c == 0:
        print("Phương trình có vô số nghiệm")
    elif b == 0 and c != 0:
        print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có nghiệm duy nhất: {-c/b}")
else:
    delta = float(b * b - 4 * a * c)
    if(delta < 0):
        print("Phương trình vô nghiệm")
    elif(delta == 0):
        print(f"Phương trình có nghiệm duy nhất = {-b / (2 * a)}")
    else:
        print(f"Phương trình có hai nghiệm phân biệt là x1 = {(-b - math.sqrt(delta)) / (2 * a)}, x2 = {(-b + math.sqrt(delta)) / (2 * a)}")
