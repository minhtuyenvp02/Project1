'''
Bai 18: Nhập chuỗi cho đến khi ặp kí tự *. Tính tần suất xuất hiện của nguyên âm a

'''
s = ""
sum_a=0
while True:
    s1 = str(input())
    if s1 == "*":
        break
    else if s1 =="a" or s1 == "A":
        sum_a+=1;
    else pass
    
    s += s1
print("Số lần xuất hiện kí tự a là {}".format(sum_a))
