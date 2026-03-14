from src.data_loader import load_data
from src.preprocessing import clean_data, create_features
from src.recommender import build_model, recommend

# load dataset
df = load_data()

# clean dataset
df = clean_data(df)

# create features
df = create_features(df)

# build model
similarity = build_model(df)

restaurant = df['names'].iloc[0]

print("\nSelected Restaurant:", restaurant)

recommendations = recommend(df, similarity, restaurant)

print("\nRecommended Restaurants:\n")

for r in recommendations:
    print("-", r)