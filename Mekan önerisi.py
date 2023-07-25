import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import random

# Veri setini yükle veya oluştur
data = pd.read_csv(r"C:\Users\akcol\Desktop\Nomatto\gezilecek_mekanlar.csv")

# Gereksiz sütunları kaldır veya önemli olanları seç
data = data.drop(["sıra"], axis=1)

# NaN değerleri kaldır veya uygun bir şekilde ele al
data = data.dropna()

# Kullanılacak öznitelikleri seç (örneğin "puanlama" sütunu)
features = data[["puanlama"]]

# Konumu temsil eden kategorik özniteliği dönüştür
location_encoded = pd.get_dummies(data["Location"])
data_encoded = pd.concat([data, location_encoded], axis=1)
data_encoded = data_encoded.drop(["Location"], axis=1)

# Özellikleri ölçeklendir
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# features_scaled'i yeniden şekillendir
features_scaled = features_scaled.reshape(-1, 1)

# K-NN modelini oluştur
k = 9  # Komşu sayısı
knn_model = NearestNeighbors(n_neighbors=k, algorithm="brute")
knn_model.fit(features_scaled)

# Öneri yapmak için bir mekan seç
mekan_input = input("Bir mekan adı girin: ")
mekan = mekan_input.split(",")[1].strip()  # Mekan adını alırken düzenleme yap

# Seçilen mekanın özelliklerini al
selected_mekan_index = data_encoded[data_encoded["mekan_adı"] == mekan].index.values[0]
selected_mekan_features = features_scaled[selected_mekan_index].reshape(1, -1)

# En yakın komşuları bul
distances, indices = knn_model.kneighbors(selected_mekan_features)

# Önerilen mekanları rastgele bir sırayla göster
print("Önerilen mekanlar:")
recommendations = indices[0]
recommendations = [i for i in recommendations if i != selected_mekan_index]  # Seçilen mekanı çıkar
random.shuffle(recommendations)
for i in recommendations:
    print(data_encoded.iloc[i]["mekan_adı"])
