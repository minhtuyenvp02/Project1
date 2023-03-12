'''
Bài 20: Nhập câu và đưa ra dưới dạng cột
'''
my_str = input("Nhập xâu: ")
my_str = my_str.strip() # Xoá khoảng trắng đầu dãy
while "  " in my_str:
    my_str = my_str.replace("  ", " ") # Các hàm xử lí string trong python trả về một xâu mới
    # Khi 2 khoảng trắng liên tiếp còn trong dãy thì thay thế bằng 1 khaowngr trắng
my_list = list(my_str.split(" "))
for i in range(0, len(my_list)):
    print(my_list[i])
