'''
Bài 17: Cài đặt thuật toán mergesort
'''
# Python CODE
MAX = 1000

while True:
    n = int(input("Nhập số phần tử của dãy "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))


def merge(arr1, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr1[l + i]

    for j in range(0, n2):
        R[j] = arr1[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr1[k] = L[i]
            i += 1
        else:
            arr1[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr1[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr1[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr1, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr1, l, m)
        merge_sort(arr1, m + 1, r)
        merge(arr1, l, m, r)

print("Dãy trước khi sắp xếp: ")
print(arr)
# Sort
merge_sort(arr, 0, n - 1)
print("Dãy sau khi được sắp xếp là: ")
print(arr)
