# a) Hàm thêm sách vào danh sách
def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": float(gia),
        "SoLuong": int(soluong)
    }
    danh_sach.append(sach)

# b) Hàm tìm kiếm sách theo tên (không phân biệt hoa/thường)
def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    for sach in danh_sach:
        if tu_khoa.lower() in sach["TenSach"].lower():
            ket_qua.append(sach)
    return ket_qua

# c) Hàm tính tổng giá trị kho sách
def tong_gia_tri_kho_sach(danh_sach):
    tong = 0
    for sach in danh_sach:
        tong += sach["Gia"] * sach["SoLuong"]
    return tong

# d) Chương trình chính hiển thị menu
def main():
    danh_sach_sach = []
    # Dữ liệu mẫu để kiểm thử
    them_sach(danh_sach_sach, "S001", "Lập trình Python cơ bản", 95000, 40)
    them_sach(danh_sach_sach, "S002", "Cấu trúc dữ liệu và giải thuật", 120000, 6)
    them_sach(danh_sach_sach, "S003", "Nhập môn trí tuệ nhân tạo", 150000, 25)

    while True:
        print("\n--- QUẢN LÝ SÁCH THƯ VIỆN ---")
        print("1. Thêm sách")
        print("2. Tìm kiếm theo tên")
        print("3. Xem tổng giá trị kho sách")
        print("4. Thoát chương trình")
        
        chon = input("Nhập lựa chọn của bạn (1-4): ")

        if chon == "1":
            ma = input("Nhập mã sách: ")
            ten = input("Nhập tên sách: ")
            gia = float(input("Nhập giá sách: "))
            soluong = int(input("Nhập số lượng: "))
            them_sach(danh_sach_sach, ma, ten, gia, soluong)
            print("-> Đã thêm sách thành công!")

        elif chon == "2":
            tu_khoa = input("Nhập từ khóa tên sách cần tìm: ")
            ds_tim_thay = tim_kiem_theo_ten(danh_sach_sach, tu_khoa)
            if ds_tim_thay:
                print("-> Kết quả tìm kiếm:")
                for s in ds_tim_thay:
                    print(f"   {s['MaSach']} - {s['TenSach']} - {s['Gia']:.0f}đ - SL: {s['SoLuong']}")
            else:
                print("-> Không tìm thấy sách phù hợp.")

        elif chon == "3":
            tong = tong_gia_tri_kho_sach(danh_sach_sach)
            print(f"-> Tổng giá trị kho sách: {tong:,.0f} VNĐ")

        elif chon == "4":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()