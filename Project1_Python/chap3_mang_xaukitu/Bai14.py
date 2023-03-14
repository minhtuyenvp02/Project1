'''
BÀi 14: Cài đặt thuật toán Insertion sort
'''
MAX = 1000
while True:
    n = int(input("Nhập số phần tử cảu dãy "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Chèn
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
print("Dãy trước khi sắp xếp là: ")
print(arr)
insertion_sort(arr, n)
print("Dãy sau khi sắp xếp: ")
print(arr)
