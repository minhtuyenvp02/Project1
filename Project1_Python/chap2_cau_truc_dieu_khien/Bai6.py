'''
Bài 6:  Viết chương trình tính cước Taxi theo công
thức:
• 1 km đầu tiên có cước là 10000đ,
• 30 km tiếp theo có giá là 8000đ/1km
• Các km sau đó có giá là 6000đ/1km.
'''

so_km = float(input("Số km đã đi được: "))
if so_km <= 1:
    print(f"Số tiền phải trả là {so_km * 10000} vnđ")
elif so_km >= 1 and so_km <= 31:
    print(f"Số tiền phải trả là {10000 + (so_km-1) * 8000} vnđ")
elif so_km >= 31:
    print(f"Số tiền phải trả là {10000 + 30 * 8000 + (so_km - 31) * 6000} vnđ")