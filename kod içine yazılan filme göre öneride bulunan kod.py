import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

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
film_input = "54,Memento,8.4,2000"
film = film_input.split(",")[1].strip()  # Film adını alırken düzenleme yap

# Seçilen filmin özelliklerini al
selected_film_index = data[data["moive_name"] == film].index.values[0]
selected_film_features = features_scaled[selected_film_index].reshape(1, -1)

# En yakın komşuları bul
distances, indices = knn_model.kneighbors(selected_film_features)

# Önerilen filmleri göster
print("Önerilen filmler:")
for i in indices[0]:
    print(data.iloc[i]["moive_name"])
