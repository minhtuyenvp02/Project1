'''
Bài 20: Nhập một dãy số cho tới khi gặp số 0 và đếm số max
'''

max = int(2 ** 32 - 1) * -1
cnt = 0
a = int(input("Nhập a: "))
while a != 0:
    a = int(input())
    if a > max:
        max = a
        cnt = 1
    elif a == max:
        cnt += 1
    else:
        pass
print(f"Max = {max}, xuất hiện {cnt} lần")
