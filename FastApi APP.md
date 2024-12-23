# 🔥 FastAPI ML Model Prediction API 🔥

Proyek ini menggunakan **FastAPI** untuk klasifikasi gambar dengan model pembelajaran mesin yang telah dilatih sebelumnya. API ini memungkinkan pengguna mengunggah gambar, memprediksi kelasnya, dan mendapatkan hasil prediksi beserta tingkat akurasinya.

---

## Fitur Utama

### 🔗 **Unggah Gambar**
Kirim gambar melalui endpoint untuk diklasifikasikan oleh model.

### 🕊️ **Pra-pemrosesan Gambar**
Gambar diubah ukurannya menjadi dimensi yang sesuai dan dinormalisasi untuk prediksi.

### 🧐 **Prediksi Cerdas**
Model **MobileNetV2** yang sudah dilatih digunakan untuk menentukan kelas gambar dengan akurasi tinggi.

### 🔒 **Dukungan CORS**
Dikonfigurasi untuk mendukung permintaan lintas asal, mempermudah integrasi dengan frontend.

---

## Persyaratan Sistem

- Python 3.8 atau lebih baru
- Framework: **FastAPI**
- Library ML: **TensorFlow/Keras**
- Utility: **OpenCV**, **NumPy**
- Server: **Uvicorn**

---

## Langkah Instalasi

1. **Kloning Repositori**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

3. **Tambahkan Model**
   Pastikan file model terlatih seperti `model_MNV2.h5` atau `model_resnet50.h5` berada di direktori `Model`.

---

## Cara Penggunaan

### 🔄 Menjalankan Server

1. Pindah ke direktori `api`:
   ```bash
   cd api
   ```

2. Jalankan aplikasi:
   ```bash
   python app.py
   ```
   Server akan aktif di **`http://127.0.0.1:8000`**.

---

### Endpoint API

#### 🔎 **POST /predict**
Unggah gambar untuk mendapatkan prediksi klasifikasi.

**Permintaan:**
- **Parameter**: `image` (file gambar)

**Respon:**
- Objek JSON yang berisi hasil prediksi kelas dan tingkat akurasi.

**Contoh Respon:**
```json
{
  "class": "LED",
  "confidence": 0.97
}
```

---

## Penggunaan API

Gunakan endpoint prediksi sebagai berikut:

```http
POST http://127.0.0.1:8000/predict
```

| Parameter | Tipe    | Deskripsi                             |
|-----------|---------|---------------------------------------|
| `image`   | `file`  | **Wajib.** Gambar yang akan diprediksi |

---

## Fungsi Internal

### 🕎 `preprocess_image(image_path: Path) -> np.ndarray`
Mengubah ukuran gambar menjadi **224x224 piksel** dan menormalisasi nilai piksel sebelum prediksi.

### 🕊️ `predict_class(image_path: Path) -> dict`
Menggunakan model MobileNetV2 atau ResNet50 untuk memprediksi kelas gambar. Mengembalikan hasil dalam bentuk dictionary.

---

## Middleware

Aplikasi menggunakan **`CORSMiddleware`** untuk mendukung integrasi frontend. Middleware ini memungkinkan permintaan lintas asal untuk memperluas fungsionalitas API.

---

## Penanganan Kesalahan

- **400 Bad Request**: Jika gambar yang diunggah tidak valid atau formatnya tidak didukung.
- **500 Internal Server Error**: Jika terjadi kesalahan server saat memproses permintaan.

---

## Kelas yang Didukung Model

Model mendukung prediksi untuk kategori berikut:

- Electrolytic-capacitor
- LED
- Armature
- Attenuator
- Cartridge-fuse
- Clip-lead
- Filament
- Heat-sink
- Jumper-cable
- Limiter-clipper
- Memory-chip
- Microchip
- Microprocessor
- Potentiometer
- Pulse-generator
- Semiconductor-diode
- Solenoid
- Step-down-transformer
---
## Dokumentasi Tambahan

Untuk informasi lebih lanjut tentang proyek ini, termasuk bagaimana model diterapkan dan hasil evaluasinya, lihat [README UAP Klasifikasi Otomatis Electronic Components](https://github.com/taufik234/UAP-Machine-Learning/blob/b52072d029410cc5ba5f67a784f19fe34f65db38/README.md).

## Author 👨‍💻

- [@taufik234](https://github.com/taufik234)
