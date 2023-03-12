'''
Bài 1: Nhập mảng, đưa ra trung bình cộng các số chia hết cho 7
'''

from statistics import mean
n = int(input("Nhập số phần tử của mảng: "))
arr = list(map(int, input("Nhập các phần tử của mảng: ").split()[:n]))

arr_divide_7 = [x for x in arr if x % 7 == 0]
if len(arr_divide_7) != 0:
    print(mean(arr_divide_7))
else:
    print("Không có số nào chia hết cho 7")
