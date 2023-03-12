'''
Bài5: Trong một năm các tháng có 30 ngày là 4, 6,
9, 11 còn các tháng có 31 ngày là 1, 3, 5, 7, 8, 10,
12. Riêng tháng hai có thể có 28 hoặc 29 ngày. Hãy
viết chương trình nhập vào năm và một tháng bất kì, sau đó đưa ra
kết luận tháng đó có bao nhiêu ngày
'''

sample = [31 , 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
n = int(input("Nhập năm: "))

while 1:
    t = int(input("Nhập tháng: "))
    if 1 <= t and t <= 12:
        break
    else:
        print("Tháng nằm trong khoảng từ 1 -> 12")
if t != 2:
    print(f"Tháng {t} co {sample[t-1]} ngày")
elif (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)) :
    print(f"Tháng {t} co 29 ngày")
else:
    print(f"Tháng {t} có 28 ngày")