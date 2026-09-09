#Hoạt động 5: Vận dụng Tuple & Yêu cầu tính khoảng cách tới (0,0)
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

# Tính khoảng cách của từng điểm trong danh sách so với gốc tọa độ (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    # Khoảng cách từ (x, y) đến (0, 0) là sqrt(x^2 + y^2)
    kc_goc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu diem {diem} den goc toa do (0, 0) la: {round(kc_goc, 2)}")