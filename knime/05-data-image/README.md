# Data Gambar (Image)

**Workflow:** `Data_Image.knwf`
**Dataset:** subset 15–20 gambar dari folder `seg_pred` (Intel Image Classification)
**Video:** _(tambahkan link)_
**Ekstensi:** KNIME Image Processing

## Alur

```
Image Reader → Image Resizer → Projector → Image Normalizer
```

| Node | Fungsi |
|------|--------|
| Image Reader | Membaca file gambar `.jpg` |
| Image Resizer | Menyeragamkan ukuran gambar menjadi 150 × 150 piksel (linear interpolation) |
| Projector | Mengubah gambar berwarna (RGB) menjadi grayscale dengan merata-ratakan kanal warna (Projection Mean, arah Channel) |
| Image Normalizer | Menormalkan nilai piksel ke rentang 0–1 |

> Path gambar di node Image Reader masih mengarah ke `D:\seg_pred\seg_pred\`. Setelah mengunduh dataset, pilih ulang file gambar dari `datasets/seg_pred/`.

Penjelasan lengkap ada di [laporan Pekan 1](../../laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf).
