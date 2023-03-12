'''
Bài 12: nHập vào mảng số nguyên n phần tử sắp xếp theo thứ tự tăng dần, giảm dần

'''
MAX = 1000
while True:
    n = int(input("Nhập số phần tử cảu dãy "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))

print("Dãy trước khi sắp xếp")
print(arr)
# Sắp xếp tăng dần
arr.sort()
print("Dãy được sắp xếp tăng dần: ")
print(arr)
# Sắp xếp giảm dần
arr.sort(reverse=True)
print("Dãy đưuọc sắp xếp giảm dần: ")
print(arr)


