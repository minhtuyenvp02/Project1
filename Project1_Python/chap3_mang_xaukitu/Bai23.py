'''
Bài 23: Nhập dãy (<100) xâu cho tới khi gặp xâu “***”.
Đưa ra màn hình xâu có độ dài lớn nhất
'''

max = -1
list_str = []
print("Nhập xâu: ")
while True:
    stri = input()
    if stri == "***":
        break
    else:
        list_str.append(stri)
        if len(stri) > max:
            max = len(stri)
        else:
            pass
for x in list_str:
    if len(x) == max:
        print(x)
    else:
        pass
