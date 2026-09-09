# Bài 1.1: Khai báo và truy cập
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])      # In phần tử đầu tiên -> Output: 8.5
print(diem_so[-1])     # In phần tử cuối cùng -> Output: 5.5
print(diem_so[1:4])    # Cắt từ vị trí 1 đến trước 4 -> Output: [7.0, 9.2, 6.5]
print(diem_so[::2])    # Lấy cách 1 phần tử (step = 2) -> Output: [8.5, 9.2, 5.5]
print(diem_so[::-1])   # Đảo ngược danh sách -> Output: [5.5, 6.5, 9.2, 7.0, 8.5]

# Bài 1.2: Các phương thức thường dùng
ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")          # Thêm "Dung" vào cuối list
ten_sv.insert(1, "Em")         # Chèn "Em" vào vị trí chỉ số 1
print(ten_sv)

ten_sv.remove("Chi")           # Xóa phần tử có giá trị "Chi"
pop_ra = ten_sv.pop()          # Xóa và lấy ra phần tử cuối cùng ("Dung")
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()                  # Sắp xếp tăng dần theo bảng chữ cái
print(ten_sv)

ten_sv.reverse()               # Đảo ngược thứ tự danh sách hiện tại
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])# Nối thêm danh sách ["Giang", "Hoa"] vào cuối
print(ten_sv)


"""remove(x): Tìm và xóa phần tử đầu tiên trong List có giá trị bằng x.
 Phương thức này không trả về giá trị (trả về None). Nếu giá trị không tồn
 tại trong List, Python sẽ báo lỗi ValueError.

pop(i): Xóa phần tử tại vị trí chỉ số i (mặc định nếu không truyền i thì 
xóa phần tử cuối cùng). Phương thức này trả về giá trị của phần tử vừa bị xóa để có thể gán
vào biến hoặc sử dụng tiếp."""