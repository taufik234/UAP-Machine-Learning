# FastAPI ML Model Prediction API

Proyek ini menggunakan FastAPI untuk klasifikasi gambar dengan model pembelajaran mesin yang sudah dilatih sebelumnya. API ini memproses gambar yang diunggah, memprediksi kelasnya, dan mengembalikan kelas tersebut beserta tingkat kepercayaan.

---

## Fitur

- **Unggah Gambar:** Mengunggah gambar untuk diklasifikasikan.
- **Pra-pemrosesan Gambar:** Menyiapkan gambar untuk prediksi dengan mengubah ukuran dan normalisasi.
- **Prediksi Model:** Menggunakan model MobileNetV2 yang telah dilatih untuk mengklasifikasikan gambar.
- **Dukungan CORS:** Dikonfigurasi untuk memungkinkan permintaan lintas asal.

---

## Persyaratan

- Python 3.8+
- FastAPI
- TensorFlow/Keras
- OpenCV
- NumPy
- Uvicorn

---

## Instalasi

1. Klon repositori:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```


2. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

3. Pastikan file model yang sudah dilatih (`model_MNV2.h5`) atau (`model_resnet50.h5`) ditempatkan di direktori `Model`.

---

## Penggunaan

### Jalankan Server

1. Masuk Ke folder api:

   ```bash
   cd api
   ```


2. Jalankan aplikasi menggunakan Python:

```bash
python app.py
```

API akan tersedia di `http://127.0.0.1:8000`.

### Endpoint API

#### **POST /predict**

Unggah gambar untuk diklasifikasikan.

**Permintaan:**
- `image` (file): File gambar yang akan diunggah untuk prediksi.

**Respon:**
- Objek JSON yang berisi kelas yang diprediksi dan confident.

**Contoh Respon:**
```json
{
  "class": "LED",
  "confidence": 0.97
}
```

---

## Penggunaan API

### Endpoint Prediksi

```http
POST http://127.0.0.1:8000/predict
```

| Parameter | Tipe | Deskripsi |
|-----------|------|-----------|
| `image` | `string` | **Wajib**. ID gambar yang akan diprediksi |


## Fungsi Internal

### `preprocess_image(image_path: Path) -> np.ndarray`

Menyiapkan gambar untuk prediksi dengan mengubah ukurannya menjadi 224x224 piksel dan menormalisasi nilai pikselnya.

### `predict_class(image_path: Path) -> Union[dict, None]`

Memprediksi kelas gambar menggunakan model MobileNetV2 atau ResNet50 yang telah dilatih. Mengembalikan dictionary yang berisi kelas yang diprediksi dan confident.

---

## Middleware

Aplikasi menggunakan `CORSMiddleware` untuk mengizinkan permintaan dari asal mana pun. Hal ini sangat berguna untuk integrasi frontend.

---

## Penanganan Kesalahan

- Unggahan gambar tidak valid atau format yang tidak didukung akan mengembalikan `400 Bad Request`.
- Masalah server internal akan mengembalikan `500 Internal Server Error`.

---

## Informasi Tambahan

Model mendukung klasifikasi kelas berikut:

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
