'''
Bài 16: Cài đặt thuật toán BUBLE SORT
'''

MAX = 1000

while True:
    n = int(input("Nhập số phần tử của dãy "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))

def buble_sort(arr, n):
    for i in range(0,n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[i]
                swapped = True
        if not swapped:
            break

print("Dãy trước khi sắp xếp là: ")
print(arr)
buble_sort(arr, n)
print('Dãy sau khi sắp xếp :')
print(arr)
