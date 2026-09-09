# Bài 3.1 - Lọc số chẵn/lẻ
day_so = list(range(1, 21))

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)

# Bài 3.2 - Biến đổi phần tử
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Diem cong:", diem_cong)