'''
BÀi 17: Nhập vào một xâu, đếm số nguyên âm, phụ âm, khoảng trắng
'''

s = str(input("Nhập xâu: "))
a = ["a", "A", "e", "E", "u", "U", "i", "I", "o", "O"]
na = 0
kt = 0
pa = 0
for x in s:
    if x in a:
        na += 1
    elif x == " ":
        kt += 1
    else:
        pa += 1

print(f"Chuỗi s có {na} nguyên âm, {pa} phụ âm, {kt} khoảng trắng")