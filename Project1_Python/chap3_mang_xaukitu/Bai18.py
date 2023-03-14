'''
Bài 18: Viết chương trình nhập vào một ma trận vuông,
các phần tử nguyên, sau đó
• Đưa ra ma trận tam giác duới
• Đưa ra ma trận tam giác trên
'''
import numpy as np

MAX = 1000
while True:
    n = int(input("Nhập kích thước một chiều ma trận N x N: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = np.array(list(map(int, input("Nhập các phần tử của ma trận: ").split()[:n*n]))).reshape((n,n))

print("Ma trận ban đầu")
print(arr)
print("Ma trận tam giác trên")
print(np.triu(arr,k = 0))
print("Ma trận tam giác dưới: ")
print(np.tril(arr,k = 0))
