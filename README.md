# 🍴 Restaurant Recommendation System - Zomato Hyderabad

> **Đồ án Cơ sở Chuyên ngành Công nghệ Phần mềm**

---

## 👥 Thành viên thực hiện
* **Nguyễn Đắc Tùng** (238066602484)
* **Trang Kiểm Tài** (23806605345)
* **Hồ Văn Tuấn** (2380602438)

---
Tài liệu tham khảo: https://www.sciencedirect.com/science/article/pii/S2666827021000578
## 📌 Giới thiệu dự án
Hệ thống gợi ý nhà hàng sử dụng thuật toán **Content-Based Filtering** để giúp người dùng tìm kiếm các địa điểm ăn uống tương đồng dựa trên sở thích về món ăn tại khu vực Hyderabad.

## 🛠 Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.12.8
* **Giao diện:** Streamlit (Web App)
* **Thư viện chính:** `Pandas`, `Scikit-learn` (TF-IDF, Cosine Similarity), `Matplotlib`, `Seaborn`.

---

## Dataset
Dữ liệu được sử dụng trong dự án là Zomato Restaurant Dataset được lấy từ Kaggle.
** Dataset bao gồm các thông tin về nhà hàng như:
- Tên nhà hàng
- Loại món ăn (Cuisine)
- Đánh giá (Rating)
- Giá trung bình
- Link nhà hàng

---

## Các chức năng đã thực hiện
** Hiện tại dự án đã thực hiện được các chức năng sau:
- Thu thập và tải dataset Zomato từ Kaggle
- Làm sạch và tiền xử lý dữ liệu
- Tạo các đặc trưng (features) từ dữ liệu nhà hàng
- Xây dựng mô hình tính độ tương đồng giữa các nhà hàng bằng TF-IDF và Cosine Similarity
- Xây dựng chức năng gợi ý nhà hàng tương tự
- Tạo giao diện web đơn giản bằng Streamlit để người dùng chọn nhà hàng và nhận gợi ý

## 📂 Cấu trúc thư mục
```text
DoAnCoSo/
├── dataset/            # File dữ liệu gốc (zomato.csv)
├── src/                # Mã nguồn xử lý logic
│   ├── data_loader.py  
│   ├── preprocessing.py
│   └── recommender.py  
├── app.py              # File thực thi giao diện Streamlit
├── requirements.txt    # Danh sách thư viện
└── README.md

