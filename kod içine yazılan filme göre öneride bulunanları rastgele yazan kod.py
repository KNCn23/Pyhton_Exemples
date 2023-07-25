import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import random

# Veri setini yükle
data = pd.read_csv(r"C:\Users\akcol\Desktop\Nomatto\moives.csv")

# Gereksiz sütunları kaldır (örneğin "rank" ve "year")
data = data.drop(["rank", "year"], axis=1)

# NaN değerleri kaldır
data = data.dropna()

# Kullanılacak öznitelikleri seç (örneğin "rating" sütunu)
features = data[["rating"]]

# Özellikleri ölçeklendir
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# features_scaled'i yeniden şekillendir
features_scaled = features_scaled.reshape(-1, 1)

# K-NN modelini oluştur
k = 9  # Komşu sayısı
knn_model = NearestNeighbors(n_neighbors=k, algorithm="brute")
knn_model.fit(features_scaled)

# Öneri yapmak için bir film seç
film_input = "85,Toy Story 3,8.3,2010"
film = film_input.split(",")[1].strip()  # Film adını alırken düzenleme yap

# Seçilen filmin özelliklerini al
selected_film_index = data[data["moive_name"] == film].index.values[0]
selected_film_features = features_scaled[selected_film_index].reshape(1, -1)

# En yakın komşuları bul
distances, indices = knn_model.kneighbors(selected_film_features)

# Önerilen filmleri rastgele bir sırayla göster
print("Önerilen filmler:")
recommendations = indices[0]
recommendations = [i for i in recommendations if i != selected_film_index]  # Seçilen filmi çıkar
random.shuffle(recommendations)
for i in recommendations:
    print(data.iloc[i]["moive_name"])
