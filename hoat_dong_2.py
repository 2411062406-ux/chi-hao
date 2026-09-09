# Bài 2.1: Duyệt list bằng vòng lặp for
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))

# Bài 2.2: List lồng nhau (Ma trận)
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo từng hàng
for hang in ma_tran:
    print(hang)

# In ra từng phần tử, duyệt theo hàng rồi theo cột
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
# code tính tổng các phần tử trong ma trận
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)
