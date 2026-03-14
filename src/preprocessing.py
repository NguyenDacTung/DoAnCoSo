import pandas as pd

def clean_data(df):

    # chọn các cột cần thiết từ dataset
    df = df[['names', 'cuisine', 'ratings', 'price for one']]

    # bỏ dữ liệu bị thiếu
    df = df.dropna()

    # chuyển cuisine thành chữ thường
    df['cuisine'] = df['cuisine'].str.lower()

    # đảm bảo ratings là số
    df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

    df = df.dropna()

    return df


def create_features(df):

    # tạo feature text cho machine learning
    df['features'] = df['cuisine'] + " " + df['ratings'].astype(str)

    return df