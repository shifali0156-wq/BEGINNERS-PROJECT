import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Transform dataset ---
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'movie.csv')
data = pd.read_csv(csv_path)

counter=CountVectorizer(max_features=4000, stop_words='english')
vectors=counter.fit_transform(data.tags).toarray()
similarity=cosine_similarity(vectors)

indexed_list=[]
for i in similarity:
  movie=[]
  for index,j in enumerate(i):
    movie.append((index,float(j)))
  indexed_list.append(movie)

# --- Recommendation logic ---
def recommend(movie):
    movie_index=data[data.title_x==movie].index[0]
    distances=indexed_list[movie_index]
    movies_list=sorted(distances,reverse=True,key=lambda x:x[1])[1:11]
    movies_names=[]
    for i in movies_list:
        movies_names.append(data.iloc[i[0]].title_x)
    return movies_names


# --- Streamlit UI ---
st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Select a movie to get recommendations:", data.title_x)

if st.button("Show Recommendations"):
    results = recommend(selected_movie)
    for row in results:
        st.subheader(row)

 

