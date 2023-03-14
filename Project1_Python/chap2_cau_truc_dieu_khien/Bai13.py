# Bài 13: Nhập n và tính tổng S = 1+1/2+..+1/n
n = int(input("Nhập n: "))
list_number = [1 / x for x in range(1, n+1)]
print(sum(list_number))