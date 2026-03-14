import streamlit as st
from src.data_loader import load_data
from src.preprocessing import clean_data, create_features
from src.recommender import build_model, recommend

# Cấu hình trang - Thêm favicon là biểu tượng đồ ăn
st.set_page_config(page_title="FoodieSuggest", page_icon="🍴", layout="wide")

# Tùy chỉnh CSS để giao diện trông "xịn" hơn
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .restaurant-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PHẦN DATA ENGINE (Giữ nguyên logic cũ) ---
@st.cache_data
def get_base_data():
    df = load_data()
    df = clean_data(df)
    df = create_features(df)
    similarity = build_model(df)
    return df, similarity

df, similarity = get_base_data()

# --- SIDEBAR: Thông tin nhóm ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1996/1996055.png", width=100)
    st.title("Nhóm Đồ Án Cơ Sở")
    st.info("**Chuyên ngành:** Công nghệ phần mềm")
    st.success("✅ Mô hình: Cosine Similarity")
    st.write("---")
    st.write("💡 *Mẹo: Chọn quán bạn hay ăn nhất để nhận gợi ý chính xác!*")

# --- MAIN UI ---
st.title("🍴 Hệ thống Gợi ý Nhà hàng thông minh")
st.subheader("Khám phá hương vị mới dựa trên sở thích của bạn")

# Bố cục hàng ngang cho phần tìm kiếm
col_search, col_empty = st.columns([2, 2])

with col_search:
    selected_restaurant = st.selectbox(
        "🔍 Bạn thích ăn ở nhà hàng nào?",
        df['names'].values,
        index=0
    )
    search_btn = st.button('Tìm nhà hàng tương tự')

st.write("---")

# --- HIỂN THỊ KẾ QUẢ ---
if search_btn:
    with st.spinner('🚀 Đang phân tích dữ liệu...'):
        try:
            results = recommend(df, similarity, selected_restaurant)
            recs = df[df['names'].isin(results)]
            
            st.success(f"Dưới đây là 5 nhà hàng có phong cách giống với **{selected_restaurant}**:")
            
            # Hiển thị dạng cột (3 cột mỗi hàng)
            cols = st.columns(3)
            
            for i, (idx, row) in enumerate(recs.iterrows()):
                with cols[i % 3]:
                    # Dùng HTML để tạo "thẻ" nhà hàng đẹp mắt
                    st.markdown(f"""
                        <div class="restaurant-card">
                            <h3 style="color: #1f1f1f; margin-bottom: 5px;">📍 {row['names']}</h3>
                            <p style="color: #666; font-size: 14px;">🍲 {row['cuisine']}</p>
                            <span style="background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 5px;">
                                ⭐ {row['ratings']}
                            </span>
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("") # Tạo khoảng cách
                    
        except Exception as e:
            st.error(f"⚠️ Không tìm thấy kết quả. Hãy thử nhà hàng khác nhé!")