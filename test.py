ten = "Lam"
tuoi = 14
chieu_cao = 1.7
dang_di_hoc = True

print(type(ten))
print(type(tuoi))
print(type(chieu_cao))
print(type(dang_di_hoc))

# Giải thích lý do đặt tên biến:
# - 2diem: SAI (Bắt đầu bằng chữ số). Sửa: hai_diem hoặc diem_2
# - ho_ten: ĐÚNG (Tuân thủ snake_case)
# - tong tien: SAI (Chứa khoảng trắng). Sửa: tong_tien
# - class: SAI (Trùng từ khóa của Python). Sửa: lop hoặc class_name
# - diemTB: HỢP LỆ
# - so-luong: SAI (Chứa ký tự '-' bị hiểu nhầm là phép trừ). Sửa: so_luong

# Đoạn code sửa lại các tên biến đúng quy tắc:
#hai_diem
#ho_ten
#tong_tien
#lop
#diem_tb
#so_luong

a = 17
b = 5

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

so = int(input("Nhập một số nguyên: "))
if so % 2 == 0:
    print(f"Số {so} là số chẵn.")
else:
    print(f"Số {so} là số lẻ.")




print("a", "b", "c", sep="-")
print("Xin chào!", end="")
print("Tạm biệt!")
print(2025, 10, 25, sep="/")



ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi của bạn: "))
print(f"Xin chào {ten}! Sang năm bạn {tuoi + 1} tuổi.")

dai = float(input("Nhập chiều dài hình chữ nhật: "))
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
chu_vi = (dai + rong) * 2
dien_tich = dai * rong
print(f"Chu vi = {chu_vi}, Diện tích = {dien_tich}")




chuoi = "Python"

# Ký tự đầu và ký tự cuối
print("Ký tự đầu và cuối:", chuoi[0], chuoi[-1])

# 3 ký tự đầu
print("3 ký tự đầu:", chuoi[:3])

# Chuỗi đảo ngược
print("Chuỗi đảo ngược:", chuoi[::-1])

# Chuỗi lặp lại 3 lần, ngăn cách bằng dấu gạch ngang
print(chuoi, chuoi, chuoi, sep="-")




toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))

print("Cả hai môn đều >= 5:", toan >= 5 and van >= 5)
print("Ít nhất một môn >= 8:", toan >= 8 or van >= 8)
print("Có bị điểm liệt (< 3):", toan < 3 or van < 3)

dtb = (toan + van) / 2
hs_gioi = dtb >= 8 and toan >= 6 and van >= 6
print("Đạt Học sinh giỏi:", hs_gioi)


ho_ten_nhap = input("Nhập họ tên (ví dụ: ' nguyễn văn an '): ")
ho_ten = ho_ten_nhap.strip()

print("Chữ hoa:", ho_ten.upper())
print("Chữ thường:", ho_ten.lower())
print("Số ký tự:", len(ho_ten))
print(f'Họ tên "{ho_ten.upper()}" có {len(ho_ten)} ký tự.')




import random

ho_ten = input("Nhập họ và tên đầy đủ: ")
cac_tu = ho_ten.strip().split()

ho = cac_tu[0]
ten = cac_tu[-1]

so = random.randint(10, 99)
username = f"{ho[:3].lower()}{ten[::-1].lower()}{so}"

print(f"Tên đăng nhập của bạn là: {username}")




import random
import string

chu_thuong = string.ascii_lowercase
chu_hoa = string.ascii_uppercase
chu_so = string.digits
ky_tu_dac_biet = "!@#$%&*"

do_dai = int(input("Nhập độ dài mật khẩu (tối thiểu 8): "))

if do_dai < 8:
    print("Lỗi: Độ dài mật khẩu tối thiểu phải là 8!")
else:
    # Lấy ít nhất 1 ký tự từ mỗi nhóm
    p_thuong = random.choice(chu_thuong)
    p_hoa = random.choice(chu_hoa)
    p_so = random.choice(chu_so)
    p_dac_biet = random.choice(ky_tu_dac_biet)

    # Các ký tự còn lại lấy ngẫu nhiên từ tổng kho
    tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
    phan_con_lai = [random.choice(tat_ca) for _ in range(do_dai - 4)]

    # Ghép và xáo trộn ngẫu nhiên
    danh_sach = [p_thuong, p_hoa, p_so, p_dac_biet] + phan_con_lai
    random.shuffle(danh_sach)

    mat_khau = "".join(danh_sach)
    print(f"Mật khẩu của bạn ({do_dai} ký tự): {mat_khau}")