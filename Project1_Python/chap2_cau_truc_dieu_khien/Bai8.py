'''
Viết chương trình nhập vào một ký tự hệ hexa và
đưa ra giá trị hệ 10 tương ứng
'''
sample = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6,"7": 7, "8": 8, "9": 9,
            "A" : 10,"B" : 11, "C" : 12,
            "D" : 13,"E" : 14, "F" : 15}
while 1:
    h = input("Nhập kí tự hexa: ")
    if h in sample.keys():
        print(f"Giá trị thập phân của kí tự {h} là {sample[h]}")
        break
    else:
        print(f"Kí tự {h} không phải là một ký tự hexa! Vui lòng nhậpt lại!")

