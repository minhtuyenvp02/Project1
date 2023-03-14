'''
Bai 9: Liệt kêt tần suất xuất hiện của các phần tử trong mảng
'''

# CODE PYTHON
MAX = 1000
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
my_set = set(arr)
for x in my_set:
    print(f"Phần tử {x} xuất hiện {arr.count(x)}")