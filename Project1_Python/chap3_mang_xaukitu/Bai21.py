'''
Bài 21: Đếm số lần xuất hiện chữ cái trong xâu
'''
my_str = input("Nhập xâu: ")
my_set = set(my_str)
count = {}
for x in my_set:
    count[x] = int(0)
for x in my_str:
    count[x] += 1

for x in count.keys():
    print(f"Tần suất xuất hiện của kí tự {x} là {count[x]}")
