'''
Bài1:
Nhập danh sách từ bàn phím các thí sinh dự thi, mỗi thí sinh gồm họ tên, số báo danh, khoa dự thi và điểm thi.
Dữ liệu nhập được ghi vào file ThiSinh.dat.
Kết thúc nhập khi gặp một thí sinh có tên là « *** »
• Đọc từ file ThiSinh.Dat, đưa ra màn hình danh sách các thí sinh.

'''

import pickle

f1 = open("ThiSinh.dat", "ab")
i = 1
while True:
    thi_sinh = {}
    print("Thi sinh {}".format(i))
    print("Nhập dữ liệu cho thí sinh thứ {}".format(i))
    thi_sinh["ten"] = input("Nhập họ và tên thí sinh: ")
    if thi_sinh["ten"] == "***": break
    else: pass
    thi_sinh["sbd"] = int(input("Số báo danh: "))
    thi_sinh["khoa"] = input("Khoa: ")
    thi_sinh["diem"] = float(input("Điểm: "))
    #Ghi file nhị  phân
    pickle.dump(thi_sinh, f1)
    i+=1
f1.close()

print("Danh sách ban đầu: ")
f1 = open("ThiSinh.Dat", "rb")
i = 0
while pickle.load(f1):
    i+=1
    x = pickle.load(f1)
    print("{:<3} {:<5} {:<20} {:<20} {:<5}".format(i, x["sbd"], x["ten"], x["khoa"], x["diem"]))
f1.close()








