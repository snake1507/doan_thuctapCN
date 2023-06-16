import streamlit as st
import pickle
import numpy as np

load = pickle.load(open('model_Random_Forest.sav','rb'))

def main():
      # Mảng lựa chọn
   quanhuyen = ['Nam Từ Liêm', 'Tây Hồ', 'Cầu Giấy', 'Hoàng Mai', 'Hà Đông',
         'Hoàn Kiếm', 'Ba Đình', 'Long Biên', 'Đống Đa', 'Thanh Xuân',
         'Bắc Từ Liêm', 'Hai Bà Trưng', 'Thanh Trì', 'Đông Anh', 'Hoài Đức',
         'Gia Lâm', 'Mê Linh', 'Chương Mỹ','trung tam thanh pho']
   xaphuong = ['Mỹ Đình 1', 'Quảng An', 'Nghĩa Đô', 'Trung Hòa', 'Mai Dịch',
         'Đại Kim', 'Phúc La', 'Tân Mai', 'Trần Hưng Đạo', 'Cầu Diễn',
         'Thanh Trì', 'Kim Mã', 'Mỗ Lao', 'Mễ Trì', 'Xuân Phương',
         'Đức Giang', 'Đội Cấn', 'Thành Công', 'Trung Phụng',
         'Liễu Giai', 'Vĩnh Phúc', 'Nhân Chính', 'Xuân La', 'Cổ Nhuế 2',
         'Dịch Vọng Hậu', 'Quan Hoa', 'Yên Hòa', 'Minh Khai', 'Vĩnh Tuy',
         'Mỹ Đình 2', 'Phạm Đình Hổ', 'Tây Mỗ', 'Phú Thượng', 'Tân Triều',
         'Ngọc Khánh', 'Dịch Vọng', 'Bùi Thị Xuân', 'Dương Nội',
         'Giáp Bát', 'Hoàng Liệt', 'Ngọc Hà', 'Giảng Võ', 'Khương Mai',
         'Ô Chợ Dừa', 'Yên Phụ', 'Láng Hạ', 'Hàng Bột',
         'Phan Chu Trinh', 'Trương Định', 'Hoàng Văn Thụ', 'Thạch Bàn',
         'Trung Liệt', 'Trung Tự', 'Đại Mạch', 'Đồng Tâm', 'Cổ Nhuế 1',
         'Vạn Phúc', 'Đồng Nhân', 'Khương Trung', 'Hạ Đình', 'Cửa Đông',
         'Điện Biên', 'Phú La', 'Yên Nghĩa', 'Thanh Xuân Nam',
         'Thanh Xuân Bắc', 'Thanh Xuân Trung', 'Văn Quán', 'Hàng Bài',
         'Tứ Liên', 'Khương Đình', 'Láng Thượng', 'Nghĩa Tân',
         'Cát Linh', 'Bạch Đằng', 'An Khánh', 'La Khê',
         'Quốc Tử Giám', 'Khương Thượng', 'Hà Cầu', 'Đông Ngạc',
         'Cống Vị', 'Nhật Tân', 'Đống Mác', 'Thụy Khuê', 'Phương Mai',
         'Kim Liên', 'Trung Văn', 'Đại Mỗ', 'Nam Đồng', 'Ngã Tư Sở',
         'Việt Hưng', 'Phúc Đồng', 'Tương Mai', 'Cửa Nam', 'Long Biên',
         'Thịnh Liệt', 'Bưởi', 'Khâm Thiên', 'Sài Đồng', 'Ngọc Thụy',
         'Xuân Đỉnh', 'Định Công', 'Lê Đại Hành', 'Hàng Mã',
         'Nguyễn Du', 'Phúc Xá', 'Gia Thụy', 'Thanh Liệt', 'Tứ Hiệp',
         'Phúc Lợi', ' Việt Hưng', 'Phương Liên', 'Tả Thanh Oai', 'Bồ Đề',
         'Thanh Lương', 'Văn Chương', 'Thượng Đình', 'Vĩnh Hưng',
         'Lĩnh Nam', 'Đông Anh', 'Nguyễn Trãi', 'Kim Giang', 'Hàng Bồ',
         'Mai Động', 'Giang Biên', 'Ngọc Lâm', 'Quang Trung', 'Trúc Bạch',
         'Quỳnh Lôi', 'Thịnh Quang', 'Phương Canh', 'Quán Thánh',
         'Hàng Bông', 'Vân Nội', 'Phú Lãm', 'Thanh Nhàn', 'Văn Miếu',
         'Phố Huế', 'Bạch Mai', 'Phương Liệt', 'Hàng Buồm', 'Phú Diễn',
         'Yên Sở', 'Thượng Thanh', 'Phú Đô', 'Dương Quang', 'Xuân Tảo',
         'Quang Minh', 'Chương Dương Độ', 'Kiến Hưng', 'Trâu Quỳ',
         'Phúc Diễn', 'Bách Khoa', 'Uy Nỗ', 'Thuỷ Xuân Tiên', 'Biên Giang',
         'Đại Thịnh', 'Mai Lâm', 'Hàng Trống','trung tam thanh pho']
   duongpho = ['Nguyễn Hoàng', 'Xóm Chùa', 'Võ Chí Công', 'Mạc Thái Tông',
         'Trung Kính', 'Nguyễn Chánh', 'Nguyễn Xiển', 'Bà Triệu',
         'Nguyễn Cảnh Dị', 'Tân Mai', 'Ngô Thì Nhậm', 'Hàm Nghi',
         'Nguyễn Khoái', 'Kim Mã', 'Nguyễn Văn Lộc', 'Mễ Trì', 'Mỹ Đình',
         'Trịnh Văn Bô', 'Đức Giang', 'Nguyễn Thị Định', 'Đội Cấn',
         'Huỳnh Thúc Kháng', 'Hoàng Ngân', 'Xã Đàn', 'Vạn Bảo', 'Trần Bình',
         'Nam Trung Yên', 'Nguyễn Tuân', 'Lạc Long Quân', 'Cổ Nhuế',
         'Phạm Tuấn Tài', 'Thiên Hiền', 'Hoàng Quốc Việt', 'Phạm Hùng',
         'Vũ Phạm Hàm', 'Đặng Thai Mai', 'Đỗ Đức Dục', 'Trung Yên',
         'Minh Khai', 'Nguyễn Văn Huyên', 'Nguyễn Khánh Toàn', 'Vĩnh Tuy',
         'Hoàng Hoa Thám', 'Trần Phú', 'Hàng Chuối', 'Miêu Nha',
         'An Dương Vương', 'Yên Xá', 'Đào Tấn', 'Phúc Diễn',
         'Trương Công Giai', 'Xuân Thủy', 'Nguyễn Quốc Trị', 'Nguyễn Du',
         'Phan Kế Bính', 'Lê Đức Thọ', 'Văn Cao', 'Tố Hữu', 'Giải Phóng',
         'Bằng A', 'La Thành', 'Hoàng Văn Thái', 'Nguyễn Ngọc Vũ', 'Tây Hồ',
         'Ngọc Khánh', 'Mai Anh Tuấn', 'Nghi Tàm', 'Tôn Đức Thắng',
         'Nghiêm Xuân Yêm', 'Đặng Thái Thân', 'Thái Thịnh', 'Quốc Tử Giám',
         'Đình Thôn', 'Đồng Me', 'Hào Nam', 'Lê Trọng Tấn', 'Lê Thánh Tông',
         'Giảng Võ', 'Dịch Vọng Hậu', 'Trương Định', 'Trần Kim Xuyến',
         'Tam Trinh', 'Mễ Trì Thượng', 'Bát Khối', 'Trung Liệt',
         'Đặng Văn Ngữ', 'Cự Lộc', 'Nguyên Hồng', 'Đại Đồng', 'Thái Hà',
         'Phố Vọng', 'Phạm Văn Đồng', 'Lò Đúc', 'Vũ Trọng Phụng',
         'Phan Chu Trinh', 'Cửa Đông', 'Nguyễn Khang', 'Xuân Đỉnh',
         'Trần Duy Hưng', 'Quốc lộ 6', 'Trung Hòa', 'Hoàng Cầu',
         'Nguyễn Trãi', 'Linh Đàm', 'Âu Cơ', 'Xa La', 'Văn Phú',
         'Triều Khúc', 'Trần Hưng Đạo', 'Trần Vỹ', 'Nguyễn Khuyến',
         'Tứ Liên', 'Đê La Thành', 'Vạn Phúc', 'Nguyễn Ngọc Nại',
         'Chùa Láng', 'Liễu Giai', 'Yên Lãng', 'Quan Hoa', 'Đầm Trấu',
         'Nguyễn Chí Thanh', 'Đại lộ Thăng Long', 'Văn Miếu', 'Chùa Bộc',
         'Xuân Phương', 'Dương Khuê', 'Trường Lâm', '19/5',
         'Nguyễn Thị Thập', 'Đại Từ', 'Mạc Thái Tổ', 'Tô Ngọc Vân',
         'Cầu Bươu', 'Đông Ngạc', 'Vũ Hữu', 'Lê Hồng Phong', 'Xuân Diệu',
         'Vương Thừa Vũ', 'Linh Lang', 'Thụy Khuê', 'Trường Chinh',
         'Trung Văn', 'Đại Mỗ', 'Trung Yên 3', 'Lê Văn Lương',
         'Trung Yên 11', 'Trung Yên 10', 'Phạm Ngọc Thạch',
         'Khuất Duy Tiến', 'Yên Lộ', 'Ô Cách', 'Nguyệt Quế', 'Cát Linh',
         'Tân Thụy', 'Nguyễn Đức Cảnh', 'Phạm Đình Hổ', 'Cầu Giấy',
         'Quang Tiến', 'Vạn Kiếp', 'Thanh Liệt', 'Nguyễn Sơn', 'Giáp Nhị',
         'Pháo Đài Láng', 'Trung Phụng', 'An Trường', 'Nguyễn Văn Linh',
         'Ngọc Thụy', 'Trần Xuân Soạn', 'Lương Thế Vinh',
         'Định Công Thượng', 'Mai Hắc Đế', 'Trần Tử Bình', 'Tân Mỹ',
         'Xuân La', 'Dương Văn Bé', 'Lê Duẩn', 'Võ Văn Dũng', 'Nghĩa Dũng',
         'Nguyễn Văn Cừ', 'Nguyễn Lam', 'Vũ Thạnh', 'Định Công',
         'Kim Giang', 'Thạch Bàn', 'Quang Trung', 'Đỗ Quang',
         'Nguyễn Huy Tưởng', 'Thành Công', 'Cổ Điển A', 'Mễ Trì Hạ',
         'Thành Thái', 'Hoa Lan', 'Hoa Sữa', 'Trần Quang Diệu',
         'Tả Thanh Oai', 'Bồ Đề', 'Thọ Lão', 'Phùng Khoang', 'Lạc Trung',
         'Vũ Xuân Thiều', 'Ba La', 'Trần Quý Cáp', 'Hoàng Tăng Bí',
         'Khương Hạ', 'Vĩnh Hưng', 'Lưu Hữu Phước', 'Văn Khê', 'Ngô Gia Tự',
         'Nam Dư', '3', '70A', 'Võng Thị', 'Kim Đồng', 'Bùi Xương Trạch',
         'Cổ Linh', 'Phú Viên', 'Ô Chợ Dừa', 'Phan Phù Tiên', 'Mỹ Đình 1',
         'Từ Hoa', 'Trần Quốc Hoàn', 'Ngọc Hà', 'Hoàng Tích Trí',
         'Dã Tượng', 'Hàng Bồ', 'Thể Giao', 'Phạm Ngũ Lão', 'Điện Biên Phủ',
         '32', 'Lĩnh Nam', 'Tây Kết', 'Phạm Khắc Quảng', 'Trần Thánh Tông',
         'Trần Nhân Tông', 'Trần Cung', 'Quán Thánh', 'Nghĩa Tân',
         'Việt Hưng', 'Đại La', 'Hạ Đình', 'Thanh Nhàn', 'Khương Trung',
         'An Dương', 'Thịnh Quang', 'Phương Canh', 'Sơn Tây', 'Khương Đình',
         'Tô Hiệu', 'Hàng Bông', 'Văn Quán', 'Trần Khát Chân', 'Vân Trì',
         'Đoàn Thị Điểm', 'Hoàng Mai', 'Thanh Lãm', 'Lý Nam Đế', 'Kim Ngưu',
         'Tân Triều', 'Bùi Ngọc Dương', 'Quan Nhân', 'Nguyễn Văn Tuyết',
         'Tây Sơn', 'Nguyễn Thanh Bình', 'Đông Quan', 'Phố Huế', 'Bạch Mai',
         'Nguyễn Lân', 'Hồ Tùng Mậu', 'Hoàng Minh Đạo', 'Trạm',
         'Khâm Thiên', 'Tôn Thất Tùng', 'Bằng B', 'Lê Lai', 'Nguyễn Siêu',
         'Trần Thái Tông', 'Kẻ Vẽ', 'Hàng Bài', 'Tây Mỗ',
         'Nguyễn Đình Chiểu', 'Chiến Thắng', 'Cầu Diễn', 'Nguyễn Cơ Thạch',
         'Mai Động', 'Nguyễn Phúc Lai', 'Trích Sài', 'Yên Lạc', 'Hoa Bằng',
         'Mai Dịch', 'Nguyễn Đổng Chi', 'Định Công Hạ', 'Thanh Am',
         'Phạm Thận Duật', 'Lê Quang Đạo', 'Dương Quang',
         'Nguyễn Đình Hoàn', 'Vũ Miện', 'Phùng Chí Kiên', 'Trúc Khê',
         'Phạm Nhật Duật', 'Nhân Mỹ', 'Đông Các', 'Đê Trần Khát Chân',
         'Hồ Đắc Di', 'Hữu Hưng', 'Phú Xá', 'Trung Yên 6', 'Lý Thường Kiệt',
         'Cao Lỗ', 'Chùa Liên', 'Văn Hương', 'Quang Minh', ' Đê Tô Hoàng',
         'Trần Hữu Dực', 'Ngụy Như Kon Tum', 'Láng', 'Đội Nhân',
         'Trần Quốc Vượng', 'Cầu Đất', 'Mậu Lương', 'Ngọc Trì',
         'Đặng Tiến Đông', 'An Lạc', 'Nguyễn Khả Trạc', 'Trần Đăng Ninh',
         'Nghĩa Lộ', 'Kẻ Tạnh', 'Nghĩa Đô', 'Láng Hạ', 'Ô Đồng Lâm',
         'Bắc Cầu', 'Võ Văn Kiệt', 'Phú Đô', 'Phúc La - Văn Phú',
         'Giang Văn Minh', 'Lê Thanh Nghị', 'Nguyễn Viết Xuân', 'Anh Đào 8',
         'Pháp Vân', 'Xuân Mai', 'An Thắng', '23B', 'Quốc lộ 3', 'Lý Sơn',
         'Trần Quốc Toản','z115']

   # Mảng mã
   code_quanhuyen = [12, 15,  3,  8,  9,  7,  0, 10, 17, 14,  1,  5, 13, 16,  6,  4, 11,
         2]
   code_xaphuong = [ 58,  95,  63, 112,  52, 154,  80, 121, 119,  14, 100,  43,  57,
         56, 139, 159, 153, 104, 114,  48, 129,  70, 138,  16,  20,  89,
         142,  55, 130,  59,  87, 123,  77, 122,  65,  19,   6,  17,  24,
         32,  64,  23,  37, 146, 144,  46,  29,  72, 120,  33, 109, 113,
         115, 155, 151,  15, 137, 150,  39,  35,  13, 147,  75, 143, 102,
         101, 103, 135,  25, 127,  40,  47,  62,   9,   4,   1,  45,  94,
         38,  34, 149,  11,  71, 152, 111,  86,  42, 116, 156,  60,  61,
         131,  82, 124,  12,  49, 110,   7,  36,  96,  69, 141, 158,  50,
         30,  66,  73,  21,  97, 126,  81,   0,  84, 125,   8,  98, 133,
         108, 136,  51, 148,  67,  41,  28,  54,  22,  68,  91, 117,  93,
         105,  83,  92,  27, 132,  76,  99, 134,  88,   3,  85,  26,  74,
         145, 107,  78,  18, 140,  90,  10,  44, 118,  79,   2, 128, 106,
            5, 157,  53,  31]
   code_duongpho = [132, 308, 279, 110, 223, 127, 158,  13, 130, 260, 165,  59, 135,
         75, 156, 113, 116, 259, 344, 149, 342,  58,  53, 307, 297, 239,
         119, 151, 102,  33, 191, 211,  54, 185, 293, 332, 341, 227, 108,
         154, 137, 290,  50, 247,  63, 109,   7, 312, 319, 182, 234, 305,
         144, 131, 173,  94, 283, 273,  44,  19,  80,  57, 142, 264, 167,
         104, 120, 271, 121, 333, 215, 202, 322, 339,  64,  92,  91,  45,
         41, 235, 245, 206, 115,  14, 224, 335,  36, 126, 330, 214, 195,
         192,  95, 294, 172,  35, 134, 306, 241, 204, 222,  49, 150,  82,
         313, 300, 287, 221, 242, 256, 136, 274, 320, 299, 141,  26,  83,
         309, 196, 331, 128, 329, 286,  24, 304,  38, 237,   1, 148, 328,
         111, 269,  28, 324, 291,  87, 301, 296,  81, 220, 236, 226, 327,
         230,  93, 229, 228, 188,  69, 311, 315, 163,  27, 262, 162, 193,
         30, 199, 298, 208, 146,  43, 175, 225,  10, 155, 168, 257, 101,
         338, 106, 255, 261, 302,  40,  86, 280, 122, 153, 139, 277, 336,
         74, 216, 200, 340, 133, 212,  34, 114, 213,  47,  48, 248, 272,
         21, 219, 178, 103, 295,  12, 249,  56,  71, 289, 100, 285, 164,
         118,   3,   5, 282,  77,  16,  32, 179, 314, 174, 117, 275, 250,
         166,  55,  37,  62, 217, 187, 317,   4,  99, 265, 186, 254, 246,
         240, 201, 124, 276, 326,  65, 210,  72,   6, 218, 184, 205,  73,
         268,  61, 288, 244, 278, 318,  51, 209,  96,  76, 263,  15, 197,
         157, 267, 147, 325, 194,  17, 140,  66,  52, 238,  70, 270,  20,
         88, 145, 253,  79,  60, 266, 159,  23,  29, 129, 107, 143, 232,
         310,  46, 105, 161, 337, 207, 190,  89,  39, 160, 292, 177, 233,
         189, 171, 323, 321,  67,  68, 180, 231,  98,  22,  25, 284, 198,
            0, 243, 170,  84, 343, 252,  31, 112, 169, 334,   8, 138, 258,
         123,  78, 125,  85, 316,  18, 281, 181, 183,  42,  90, 152,  11,
         176, 303,   9,   2, 203,  97, 251]
   # Tạo từ điển từ hai mảng
   quanhuyen_dict = dict(zip(quanhuyen, code_quanhuyen))
   xaphuong_dict = dict(zip(xaphuong, code_xaphuong))
   duongpho_dict = dict(zip(duongpho, code_duongpho))

   # Tạo select box
   selected_quanhuyen = st.selectbox("Chọn Quận(Huyện):", quanhuyen)
   selected_xaphuong = st.selectbox("Chọn Xã(Phường, Thị Trấn):", xaphuong)
   selected_duongpho = st.selectbox("Chọn Đường(Phố):", duongpho)

   # Chuyển đổi lựa chọn thành mã
   change_code_quanhuyen = quanhuyen_dict[selected_quanhuyen]
   change_code_xaphuong = xaphuong_dict[selected_xaphuong]
   change_code_duongpho = duongpho_dict[selected_duongpho]

   # lựa chọn số tầng
   sotang = ["{}".format(i) for i in range(1,10)]
   luachontang = st.selectbox("Số tầng:", sotang)

   # Nhập diện tích
   text_dientich = st.number_input("Diện tích:", value=0, step=1)
   text_sophong = st.number_input("Số phòng:", value=0, step=1)
   text_sotoilet = st.number_input("Số Toilet:", value=0, step=1)


   
   button = st.button('Gửi')
   if button:
      data = np.array([change_code_duongpho,change_code_xaphuong,change_code_quanhuyen,text_dientich,luachontang,text_sophong,text_sotoilet]).reshape(1,-1)
      predict = load.predict(data)
      st.write('Giá dự đoán: '+str(predict))
   pass

if __name__ == '__main__':
    main()


#%%
