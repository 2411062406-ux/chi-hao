# Bài 4.1 - Khai báo & tính bất biến
toa_do = (3, 5)
print(toa_do, type(toa_do))

# Thử gán lại sẽ gây ra lỗi TypeError vì tuple là dữ liệu bất biến (immutable)
# toa_do[0] = 10 

# Bài 4.2 - Unpacking tuple
x, y = toa_do
print("x =", x, "- y =", y)

# Đổi giá trị 2 biến bằng unpacking (không cần biến tạm)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

# Bài 4.3 - Trả về nhiều giá trị từ một biểu thức
c, d = 17, 5
thuong_du = divmod(c, d)     # divmod trả về tuple (thuong, du)
thuong, du = thuong_du       # unpacking kết quả
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

