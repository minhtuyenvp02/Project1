'''
Bài 10: Đảo ngược thứ tự các phần tử trong mảng ban đầu
'''

MAX = 1000
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
arr.reverse()
print(arr)
