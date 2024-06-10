import numpy as np

# Histogram verilerini oluşturun
histogram_data = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42,
    108: 32, 109: 16, 110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40,
    145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}

# Başlangıç eşik değeri
T0 = 100
threshold = 1

# Histogram verilerinden yoğunluk ve piksel sayılarını ayrı listelerde tutalım
intensity_values = np.array(list(histogram_data.keys()))
pixel_counts = np.array(list(histogram_data.values()))

# Eşikleme algoritması
while True:
    # G1 ve G2 gruplarını oluşturma
    G1_mask = intensity_values > T0
    G2_mask = ~G1_mask

    G1 = intensity_values[G1_mask]
    G2 = intensity_values[G2_mask]

    G1_counts = pixel_counts[G1_mask]
    G2_counts = pixel_counts[G2_mask]

    # G1 ve G2 ortalamalarını hesaplama
    m1 = np.sum(G1 * G1_counts) / np.sum(G1_counts) if np.sum(G1_counts) != 0 else 0
    m2 = np.sum(G2 * G2_counts) / np.sum(G2_counts) if np.sum(G2_counts) != 0 else 0

    # Yeni eşik değeri hesaplama
    T1 = (m1 + m2) / 2

    # Eşik değeri değişimini kontrol et
    if abs(T1 - T0) < threshold:
        break

    # T0'ı yeni eşik değeri olarak güncelle
    T0 = T1

# Optimum eşik değerini yazdır
print(f"Optimum Eşik Değeri: {T1}")
