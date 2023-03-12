'''
Bài 5: Cho mảng 1 chiều các số nguyên.
Hãy viết hàm tìm giá trị lớn nhất trong mảng có dạng 5^k.
Nếu mảng khong tồn tại giá trị 5^k thì hàm sẽ trả về 0
'''

MAX = 100
while True:
    n = int(input("Nhập số phần tử của dãy: "))
    if n <= 0 or n > MAX:
        print("Số phần tử không hợp lệ vui lòng nhật lại!")
    else:
        break
arr = list(map(int, input("Nhập dãy số: ").split()[:n]))
max = 0
def kiem_tra_dang5k(n):
    if n <= 1:
        return True
    else:
        while n > 1:
            if n % 5:
                return False
            else:
                n /= 5
        return True

for x in arr:
    if kiem_tra_dang5k(x) and x > max:
        max = x
if max == 0:
    print("Không có số nào có dạng 5^k")
else:
    print(f"Số lớn nhất có dạng 5^k trong dãy là {max}")
