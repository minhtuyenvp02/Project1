#Đọc vào từ bàn phím một số nguyên N (1 <= N <=10)
# Đưa ra từ tiếng Anh tương ứng

sample = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

while 1:
    N = int(input("Nhập số N: "))
    if N >= 1 and N <= 10:
        break
    else:
        print("1 <= N <= 10")
print(f"{sample[N - 1]}")