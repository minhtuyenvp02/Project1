'''
Bài 13: Cài đặt thuật toán quick sort
'''

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(pi, end = "")
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

n = int(input("Nhập số phần tử n: "))
arr = list(map(int, input("Enter multiple values: ").split()[:n]))

quick_sort(arr, 0, n-1)
print(arr)
