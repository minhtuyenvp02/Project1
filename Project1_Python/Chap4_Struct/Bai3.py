'''
Bai3:
    Nhập danh sách có N (N < 100, nhập từ bàn phím) thí sinh gồm họ tên, số báo danh,
    khoa dự thi và điểm thi
• Đưa ra DSSV đã sắp xếp theo kết quả thi
• Đưa ra danh sách sinh viên dự thi khoa CNTT có điểm thi từ 22.5 trở lên
• Nhập vào một số báo danh và in ra họ tên, điểm thi và khoa đăng ký
 của thí sinh nếu tìm thấy. Nếu không tìm thấy thí sinh thì
 đưa ra thông báo « không tìm thấy »
'''

MAX = 100
DS = []
n = int(input("Nhập số lượng thí sinh "))
for i in range(0,n):
    thi_sinh = {}
    print("Nhập dữ liệu cho thí sinh thứ {}".format(i+1))
    thi_sinh["sbd"] = int(input("Số báo danh: "))
    thi_sinh["ten"] = input("Nhập họ và tên thí sinh: ")
    thi_sinh["khoa_dang_ki"] = input("Nhập khoa đăng ký: ")
    thi_sinh["ket_qua_thi"] = float(input("Nhập kết quả thi: "))
    DS.append(thi_sinh)
# Sắp xếp danh sách theo điểm thi
def comp(item) -> float:
    return float((item["ket_qua_thi"]))
DS.sort(key = comp, reverse=True)
i = 0

for x in DS:
   i+=1
   print("{:<3} BKA-{} {:^24} {:^6} {:^6.1f} \n".format(i,x["sbd"], x["ten"],x["khoa_dang_ki"], x["ket_qua_thi"]))



