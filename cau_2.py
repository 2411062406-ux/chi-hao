import tkinter as tk
from tkinter import messagebox

danh_sach_sach = []

def hien_thi_danh_sach(ds):
    listbox_sach.delete(0, tk.END)  # Xóa kết quả cũ trước khi hiển thị mới
    for s in ds:
        chuoi_hien_thi = f"{s['MaSach']} - {s['TenSach']} - {s['Gia']:.0f}đ - SL: {s['SoLuong']}"
        listbox_sach.insert(tk.END, chuoi_hien_thi)

def xu_ly_them_sach():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia_str = entry_gia.get().strip()
    soluong_str = entry_soluong.get().strip()

    # d) Kiểm tra dữ liệu nhập
    if not ma or not ten:
        messagebox.showerror("Lỗi nhập liệu", "Mã sách và Tên sách không được để trống!")
        return

    try:
        gia = float(gia_str)
        soluong = int(soluong_str)
        if gia < 0 or soluong < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Giá và Số lượng phải là số hợp lệ (không âm)!")
        return

    # b) Thêm vào danh sách và cập nhật giao diện
    sach_moi = {"MaSach": ma, "TenSach": ten, "Gia": gia, "SoLuong": soluong}
    danh_sach_sach.append(sach_moi)
    hien_thi_danh_sach(danh_sach_sach)

    # Xóa trắng các ô nhập sau khi thêm
    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_soluong.delete(0, tk.END)

def xu_ly_tim_kiem():
    # c) Chức năng tìm kiếm
    tu_khoa = entry_timkiem.get().strip().lower()
    if not tu_khoa:
        hien_thi_danh_sach(danh_sach_sach)
        return
    
    ket_qua = [s for s in danh_sach_sach if tu_khoa in s["TenSach"].lower()]
    hien_thi_danh_sach(ket_qua)

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý sách thư viện")
root.geometry("450x480")

# a) Form nhập liệu các thuộc tính của sách
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill=tk.X)

tk.Label(frame_form, text="Mã sách:").grid(row=0, column=0, sticky="w", pady=5)
entry_ma = tk.Entry(frame_form, width=35)
entry_ma.grid(row=0, column=1, pady=5)

tk.Label(frame_form, text="Tên sách:").grid(row=1, column=0, sticky="w", pady=5)
entry_ten = tk.Entry(frame_form, width=35)
entry_ten.grid(row=1, column=1, pady=5)

tk.Label(frame_form, text="Giá sách:").grid(row=2, column=0, sticky="w", pady=5)
entry_gia = tk.Entry(frame_form, width=35)
entry_gia.grid(row=2, column=1, pady=5)

tk.Label(frame_form, text="Số lượng:").grid(row=3, column=0, sticky="w", pady=5)
entry_soluong = tk.Entry(frame_form, width=35)
entry_soluong.grid(row=3, column=1, pady=5)

btn_them = tk.Button(frame_form, text="Thêm sách", command=xu_ly_them_sach, bg="#4CAF50", fg="white", width=15)
btn_them.grid(row=4, column=1, sticky="w", pady=10)

# Khung tìm kiếm
frame_search = tk.Frame(root, padx=10, pady=5)
frame_search.pack(fill=tk.X)

tk.Label(frame_search, text="Tìm tên sách:").pack(side=tk.LEFT)
entry_timkiem = tk.Entry(frame_search, width=25)
entry_timkiem.pack(side=tk.LEFT, padx=5)
btn_tim = tk.Button(frame_search, text="Tìm kiếm", command=xu_ly_tim_kiem)
btn_tim.pack(side=tk.LEFT)

# Vùng hiển thị danh sách sách
frame_list = tk.Frame(root, padx=10, pady=10)
frame_list.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_list, text="Danh sách sách:").pack(anchor="w")
listbox_sach = tk.Listbox(frame_list, width=60, height=12)
listbox_sach.pack(fill=tk.BOTH, expand=True, pady=5)

root.mainloop()