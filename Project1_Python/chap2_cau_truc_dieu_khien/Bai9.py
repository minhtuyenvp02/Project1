'''
Bài9:  Lập trình đọc tọa độ 4 điểm A,B,C,M rồi kiểm tra
xem điểm M nằm trong, nằm trên cạnh hay nằm
ngoài tam giác ABC.
'''

A = {"x": float(input("Nhập hoành độ điểm A: ")),
     "y": float(input("Nhập tung độ điểm A: "))}
B = {"x": float(input("Nhập hoành độ điểm B: ")),
     "y": float(input("Nhập tung độ điểm B: "))}
C = {"x": float(input("Nhập hoành độ điểm C: ")),
     "y": float(input("Nhập tung độ điểm C: "))}
M = {"x": float(input("Nhập hoành độ điểm M: ")),
     "y": float(input("Nhập tung độ điểm M: "))}


def check_khac_phia(A=None, B=None, C=None, M=None):
    if M is None:
        M = {"x": 0.0, "y": 0.0}
    if B is None:
        B = {"x": 0.0, "y": 0.0}
    if A is None:
        A = {"x": 0.0, "y": 0.0}
    if C is None:
        C = {"x": 0.0, "y": 0.0}
    a = float(B["x"] - A["x"])
    b = float(B["y"] - A["y"])
    if a == 0 and b == 0:
        print("Không là tam giác!")
        return None
    else:
        if not a:
            if (M["x"] - A["x"]) * (C["x"] - A["x"]) == 0: return 0
            elif (M["x"] - A["x"]) * (C["x"] - A["x"]) < 0: return -1
            else: return 1
        elif not b:
            if (M["y"] - A["y"]) * (C["y"] - A["y"]) == 0: return 0
            elif (M["y"] - A["y"]) * (C["y"] - A["y"]) < 0: return -1
            else: return 1
        else:
            fC = float(C["x"] - A["x"]) / a - float(C["y"] - A["y"]) / b
            fM = float(M["x"] - A["x"]) / a - float(M["y"] - A["y"]) / b
            if fC * fM < 0: return -1
            elif fC * fM == 0: return 0
            else: return 1
a = check_khac_phia(B, C, A, M)
b = check_khac_phia(A, C, B, M)
c = check_khac_phia(A, B, C, M)
if a * b * c == 0:
    if not a: print("M nằm trên cạnh BC")
    elif not b: print("M nằm trên cạnh AC")
    else: print("M nằm trên cạnh AB")
elif (a * b < 0) or (b * c < 0) or (a * c < 0): print("M nằm ngoài tam giác ABC")
else: print("M nằm trong tam giác ABC")
