from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_model(df):

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(df['features'])

    similarity = cosine_similarity(tfidf_matrix)

    return similarity


def recommend(df, similarity, restaurant_name):

    idx = df[df['names'] == restaurant_name].index[0]

    scores = list(enumerate(similarity[idx]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    scores = scores[1:6]

    restaurant_indices = [i[0] for i in scores]

    results = df['names'].iloc[restaurant_indices].tolist()

    return results