# Eksplorasi Tools Data Mining: KNIME, Orange, Google Colab, dan n8n

Repositori ini berisi hasil magang saya: workflow, dataset, laporan, dan video tutorial untuk eksplorasi tools data mining dan otomasi.

**Penulis:** Raditya Mulya Akbar (425 23 011), S1 Terapan Teknik Komputer dan Jaringan, Politeknik Negeri Ujung Pandang

## Cakupan

| No | Topik | Status | Folder |
|----|-------|--------|--------|
| 1 | KNIME Analytics Platform: data preparation untuk 7 tipe data | ✅ Selesai + video | [`knime/`](knime/) |
| 2 | KNIME: penanganan unbalanced dataset (Equal Size Sampling & SMOTE) | ✅ Selesai + video | [`knime/06-unbalanced-dataset/`](knime/06-unbalanced-dataset/) |
| 3 | Orange Data Mining: eksplorasi fitur dan perbandingan dengan KNIME | ✅ Selesai | [`orange/`](orange/) |
| 4 | Orange + Python: balancing dengan imbalanced-learn | ✅ Selesai | [`orange/`](orange/) |
| 5 | Kompatibilitas dengan Google Colab | 🚧 Berjalan | [`colab/`](colab/) |
| 6 | n8n untuk automation | ⏳ Belum | [`n8n/`](n8n/) |
| 7 | Soulbound Blockchain | ⏳ Belum | – |

## Struktur Repositori

```
.
├── datasets/          Daftar dataset dan link unduhannya
├── knime/             Workflow KNIME (.knwf), satu folder per topik
├── orange/            Workflow Orange (.ows) dan script Python
├── colab/             Notebook Google Colab
├── n8n/               Workflow n8n (.json)
└── laporan/           Laporan pekanan (PDF)
```

## Video Tutorial

| Topik | Link |
|-------|------|
| KNIME: Data Numerik (interval & rasio) | _(tambahkan link)_ |
| KNIME: Data Kategorikal (nominal & ordinal) | _(tambahkan link)_ |
| KNIME: Data Teks | _(tambahkan link)_ |
| KNIME: Data Time Series | _(tambahkan link)_ |
| KNIME: Data Image | _(tambahkan link)_ |
| KNIME: Unbalanced Dataset | _(tambahkan link)_ |
| Orange: Eksplorasi & Balancing dengan Python | _(menyusul)_ |

## Cara Memakai

1. Clone repositori ini:
   ```bash
   git clone https://github.com/<username>/<nama-repo>.git
   ```
2. Unduh dataset sesuai petunjuk di [`datasets/README.md`](datasets/README.md), lalu simpan di folder `datasets/`.
3. **KNIME:** buka KNIME → *File → Import KNIME Workflow…* → pilih file `.knwf`. Setelah itu arahkan ulang path dataset di node *CSV Reader* (detailnya ada di README tiap folder).
4. **Orange:** buka file `.ows` di Orange. Path dataset sudah dibuat relatif terhadap lokasi workflow (`../datasets/bank-full.csv`), jadi selama struktur folder tidak diubah, file langsung terbaca.

## Perangkat yang Digunakan

- KNIME Analytics Platform 5.11, dengan ekstensi *KNIME Textprocessing* (untuk data teks) dan *KNIME Image Processing* (untuk data gambar)
- Orange Data Mining 3, dengan tambahan pustaka `imbalanced-learn` 0.14.2
- Google Colab
- n8n

## Laporan

| File | Isi |
|------|-----|
| [`01_Laporan_Pekan1_KNIME_Tipe_Data.pdf`](laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf) | Data preparation dan preprocessing di KNIME untuk 7 tipe data |
| [`03_Laporan_Pekan3_KNIME_Unbalanced.pdf`](laporan/03_Laporan_Pekan3_KNIME_Unbalanced.pdf) | Penanganan unbalanced dataset dengan Equal Size Sampling dan SMOTE di KNIME |
| [`04_Laporan_Orange_Data_Mining.pdf`](laporan/04_Laporan_Orange_Data_Mining.pdf) | Eksplorasi fitur Orange dan perbandingannya dengan KNIME |
| [`05_Laporan_Orange_dengan_Python.pdf`](laporan/05_Laporan_Orange_dengan_Python.pdf) | Balancing di Orange melalui widget Python Script |
