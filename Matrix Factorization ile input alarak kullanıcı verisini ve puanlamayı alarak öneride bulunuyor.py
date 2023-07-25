import sys
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.preprocessing import MinMaxScaler
import random
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds

# Veri setini yükle veya oluştur
data = pd.read_csv(r"C:\Users\akcol\Desktop\Nomatto\gezilecek_mekanlar_kullanıcılı.csv")

# Gereksiz sütunları kaldır veya önemli olanları seç
data = data.drop(["sıra"], axis=1)

# NaN değerleri kaldır veya uygun bir şekilde ele al
data = data.dropna()

# Kullanılacak öznitelikleri seç (örneğin "puanlama" sütunu)
features = data[["puanlama"]]

# Özellikleri ölçeklendir
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# Kullanıcı-Mekan matrisini oluştur
user_mekan_matrix = pd.pivot_table(data, values='puanlama', index='kullanıcı', columns='mekan_adı', fill_value=0)
user_mekan_matrix = lil_matrix(user_mekan_matrix.values)

# SVD ile Matrix Factorization uygula
k = min(user_mekan_matrix.shape) - 1
U, S, Vt = svds(user_mekan_matrix, k=k)

S_diag_matrix = np.diag(S)
user_mekan_matrix_pred = np.dot(np.dot(U, S_diag_matrix), Vt)

# Kullanıcı bilgisi al
kullanici = int(input("Kullanıcı ID'sini girin: "))
mekan_adı = input("Mekan adını girin: ")
puanlama = float(input("Puanlamayı girin: "))
location = input("Konumu girin: ")

# Kullanıcı bilgisi oluştur
kullanici_bilgisi = {
    "kullanıcı": kullanici,
    "mekan_adı": mekan_adı,
    "puanlama": puanlama,
    "Location": location
}

# Veri setine kullanıcıyı ekle
data = data.append(kullanici_bilgisi, ignore_index=True)

# Seçilen kullanıcının mekan tahminlerini al
selected_user_indices = data[data["kullanıcı"] == kullanici_bilgisi["kullanıcı"]].index.values
if len(selected_user_indices) == 0:
    print("Hata: Seçilen kullanıcı bulunamadı.")
    sys.exit()

selected_user_index = selected_user_indices[0]
if selected_user_index >= user_mekan_matrix_pred.shape[0]:
    print("Hata: Seçilen kullanıcı indeksi geçerli değil.")
    sys.exit()

selected_user_predictions = user_mekan_matrix_pred[selected_user_index, :]

# Benzer mekanları bul
similar_mekan_indices = pairwise_distances([selected_user_predictions], user_mekan_matrix_pred, metric='cosine')[0].argsort()
random.shuffle(similar_mekan_indices)

# Önerilen mekanları göster (en fazla 6 mekan)
print("Önerilen mekanlar:")
for i in similar_mekan_indices[:6]:
    print(data.iloc[i]["mekan_adı"])  # Mekan adını alırken sütun adını kullan
