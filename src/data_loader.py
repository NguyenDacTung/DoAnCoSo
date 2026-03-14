import pandas as pd

def load_data():

    df = pd.read_csv("dataset/zomato.csv")

    print("Dataset shape:", df.shape)
    print(df.head())

    return df