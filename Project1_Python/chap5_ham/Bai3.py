'''
Bai3:
Cho hàm f(x) được định nghĩa như sau
𝑓 𝑥 = sqrt(𝒆𝟐𝒙+𝟏 + 𝟏) + 7  khi  |x| <=2
    𝑥5+5𝑥3+𝑥+1 𝑘h𝑖 𝑥 >2
Hãy viết chương trình thực hiện các công việc sau
• Viết chương trình con tính hàm trên
• Nhậpvàotừbànphím2sốthựcx,y,tínhvàđưaramàn hình (f(x)+f(y))2
• Đưa ra màn hình theo dòng các cặp <x, f(x)> (định dạng đưa ra là các số thực tĩnh có 2 chữ số sau dấu chấm) trong đó giá trị của x lần lượt là -5.0; -4.9; -4.8;.....2.8; 2.9; 3.0.
'''
import math
def f(x):
    if math.fabs(x) <= 2:
        return math.sqrt(math.e ** (2*x+1)) + 7
    else:
        return x**5 + 5*x**3 + x + 1
x = float(input("X = "))
y = float(input("Y = "))
print("{:0.2f}".format((f(x) + f(y)) ** 2))
x = -5.0
while x <= 3.0:
    print("<{:0.2f}, {:0.2f}>".format(x, f(x)))
    x += 0.1