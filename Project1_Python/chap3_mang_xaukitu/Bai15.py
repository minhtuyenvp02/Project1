'''
Bai 15: Cài đặt thuật toán selection sort
'''
MAX = 1000
while True:
    n = int(input("Nhập số phần tử của dãy "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
def selection_sort(arr, n):
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
print("Dãy trước khi sắp xếp là: ")
print(arr)
selection_sort(arr,n)
print("Dãy sau khi sắp xếp là: ")
print(arr)
