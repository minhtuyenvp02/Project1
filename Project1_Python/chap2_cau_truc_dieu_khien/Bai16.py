'''
Bài 16: Tìm số tự nhiên lớn nhất thoả mãn: 3n^5 - 317n < 5
'''
n = 0
while(3 * (n**5) - 317*n < 5) :
    n += 1
print(n-1)