'''
Nhập vào mt dãy số tìm sỗ chẵn nhỏ nhất của dãy
'''
#Code Python
n = int(input("Nhập số phần tử của dãy: "))
arr = list(map(int, input("Nhập các phần tử của mảng: ").split()[:n]))
min =  1e20
cnt = 0
for x in arr:
    if x % 2 == 0 and x < min:
        cnt += 1
        min = x
if cnt == 0:
    print("Không có số chẵn nào trong dãy")
else:
    print(f"Số chẵn nhỏ nhất trong dãy là {min}")