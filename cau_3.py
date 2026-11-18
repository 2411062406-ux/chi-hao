import matplotlib.pyplot as plt
import pandas as pd

# a) Đọc dữ liệu sách từ file sach.csv
df = pd.read_csv('sach.csv')
print('--- DỮ LIỆU SÁCH ---')
print(df)
print('-' * 30)

# b) Tính và in ra: tổng số đầu sách, giá trung bình, tên sách có giá cao nhất
tong_dau_sach = len(df)
gia_trung_binh = df['Gia'].mean()
sach_gia_cao_nhat = df.loc[df['Gia'].idxmax(), 'TenSach']

print(f'Tổng số đầu sách: {tong_dau_sach}')
print(f'Giá trung bình của các sách: {gia_trung_binh:,.0f} VNĐ')
print(f'Tên sách có giá cao nhất: {sach_gia_cao_nhat}')

# c) Vẽ biểu đồ cột thể hiện SoLuong tồn kho và lưu thành bieudo.png[cite: 1]
plt.figure(figsize=(8, 5))
plt.bar(df['MaSach'], df['SoLuong'], color='skyblue', edgecolor='black')
plt.title('Số lượng tồn kho của từng cuốn sách')
plt.xlabel('Mã Sách')
plt.ylabel('Số Lượng')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Lưu biểu đồ ra file mà không cần gọi plt.show()[cite: 1]
plt.savefig('bieudo.png')
plt.close()
print('Đã lưu biểu đồ thành công vào file bieudo.png')

# d) Lọc các sách có SoLuong < 10 và xuất ra file canh_bao_sach.csv[cite: 1]
sach_sap_het = df[df['SoLuong'] < 10]
sach_sap_het.to_csv('canh_bao_sach.csv', index=False)
print('Đã xuất danh sách cảnh báo ra file canh_bao_sach.csv')
# d) Lọc các sách có SoLuong < 10 và xuất ra file canh_bao_sach.csv[cite: 1]
sach_sap_het = df[df['SoLuong'] < 10]
sach_sap_het.to_csv('canh_bao_sach.csv', index=False)

print('\n--- DANH SÁCH CẢNH BÁO SÁCH SẮP HẾT ---')
print(sach_sap_het.to_string(index=False))