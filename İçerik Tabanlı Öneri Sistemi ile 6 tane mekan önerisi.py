import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
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

# Özellikleri ölçeklendir
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# Özellikleri yeniden şekillendir ve benzerlik matrisini hesapla
similarity_matrix = cosine_similarity(features_scaled)

# Öneri yapmak için bir mekan seç
mekan_input = input("Bir mekan adı girin: ")
mekan = mekan_input.split(",")[1].strip()  # Mekan adını alırken düzenleme yap

# Seçilen mekanın özelliklerini al
selected_mekan_indices = data[data["mekan_adı"] == mekan].index.values
if len(selected_mekan_indices) == 0:
    print("Hata: Seçilen mekan bulunamadı.")
    exit()

selected_mekan_index = selected_mekan_indices[0]
selected_mekan_similarities = similarity_matrix[selected_mekan_index]

# Benzer mekanları bul
similar_mekan_indices = selected_mekan_similarities.argsort()[::-1]
similar_mekan_indices = [i for i in similar_mekan_indices if i != selected_mekan_index]  # Seçilen mekanı çıkar
random.shuffle(similar_mekan_indices)

# Önerilen mekanları göster (en fazla 6 mekan)
print("Önerilen mekanlar:")
for i in similar_mekan_indices[:6]:
    print(data.iloc[i]["mekan_adı"])
