'''
Bai2: NHập vào một danh sách (<100) sinh viên gồm họ tên, năm sinh>
Kết thúc nhập khi gặp sinh viên có tên là rỗng
    _ Đưa ra danh sách vừa nhập ra màn hình
    _ Đưa ra màn hình sinh viên lớn tuổi nhất
'''

print('Nhập danh sách sinh viên: ')
DS = {}
while True:
    Ten = input("Nhập tên sinh viên: ")
    if len(Ten) == 0:
        break
    else:
        NS = int(input("Năm sinh: "))
        DS[Ten] = NS
i,_min = 0,1000000
print("{:^26}{:^10}".format("Họ Tên", "Năm Sinh"))
for x in DS:
    i+=1
    _min = min(_min, int(DS[x]))

    print("{:<6}{:<20}{:^8}".format(i, x, DS[x]))
print("Sinh viên lớn tuổi nhất là:")
for x in DS:
    if int(DS[x]) == _min:
        print("{:^20}{:^8}".format(x, DS[x]))
    else: pass
