'''
Bài 3: Viết chương trình nhập vào từ bàn phím một dãy số (<100)
phần tử. Đưa ra số bé nhất và vị trí các số bằng số bé nhất
'''

n = int(input("Nhập số phần tử của dãy: "))
arr = list(map(int, input("Nhập các phần tử của mảng: ").split()[:n]))

x = min(arr)
print(f"Phần tử bé nhất của dãy là: {x}")
print("VỊ trí các phần tử có giá trị = x là: ")
for i in range(0, len(arr)):
    if arr[i] == x:
        print(f"{i} ", end="")
