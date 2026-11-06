# Penanganan Unbalanced Dataset

**Workflow:** `Unbalance_Dataset.knwf`
**Dataset:** `bank-full.csv`: 45.211 baris, kelas `no` 88,30% dan `yes` 11,70%
**Video:** _(tambahkan link)_

Workflow ini membandingkan tiga skenario dengan model Decision Tree: tanpa balancing, undersampling (Equal Size Sampling), dan oversampling sintetis (SMOTE).

## Alur

```
                       ┌→ Decision Tree Learner ───────────────────────→ Predictor  (tanpa balancing)
CSV Reader → Table ────┼→ Equal Size Sampling → Decision Tree Learner ──→ Predictor  (undersampling)
             Partitioner└→ Category to Number → SMOTE → Decision Tree Learner → Predictor  (SMOTE)
             (70:30)        data uji (30%) ────────────────────────────→ ketiga Predictor
```

| Node | Pengaturan |
|------|------------|
| CSV Reader | Kolom yang dipakai: age, job, marital, education, balance, housing, loan, y. Kolom `duration` sengaja dibuang karena nilainya baru diketahui setelah telepon selesai (data leakage) |
| Table Partitioner | 70% latih : 30% uji, stratified pada `y`, seed 42 |
| Equal Size Sampling | Kelas `y`, metode Exact, seed 42 |
| Category to Number | Mengubah atribut kategorikal menjadi angka (syarat SMOTE di KNIME) |
| SMOTE | Kelas `y`, k = 5, oversample minoritas sampai seimbang, seed 42 |

Balancing **hanya diterapkan pada data latih**, sedangkan data uji tetap pada distribusi aslinya. Kalau balancing dilakukan sebelum data dibagi, sampel sintetis bisa ikut masuk ke data uji dan hasil evaluasi jadi terlalu optimis.

## Hasil (kelas positif = `yes`, data uji 13.564 baris)

| Skenario | Recall | Precision | F-measure | Accuracy | Kappa |
|----------|-------:|----------:|----------:|---------:|------:|
| Tanpa balancing | 26,47% | 30,55% | 28,36% | 84,36% | 0,196 |
| Equal Size Sampling | 62,19% | 16,81% | 26,46% | 59,55% | 0,099 |
| SMOTE | 16,19% | 12,78% | 14,29% | 77,26% | 0,014 |

**Ringkasan:**
- Undersampling menaikkan recall lebih dari dua kali lipat, tetapi precision dan accuracy turun tajam. Cocok kalau prioritasnya tidak melewatkan nasabah potensial.
- SMOTE justru lebih buruk dari baseline.

> ⚠️ **Catatan koreksi:** hasil SMOTE di atas disebabkan **kesalahan pada workflow**, bukan teknik SMOTE. Model di cabang SMOTE dilatih dengan data hasil *Category to Number* (kolom kategori sudah jadi angka), tetapi data uji yang masuk ke *Decision Tree Predictor (#11)* masih berupa teks. Akibatnya lima dari tujuh kolom tidak terbaca dan model praktis menebak acak (Kappa 0,014).
>
> Hal ini dibuktikan di [notebook Colab 02](../../colab/02_knime_balancing_di_colab.ipynb): model PMML dari KNIME yang diberi data teks menghasilkan angka yang sama dengan Scorer di atas.
>
> **Perbaikan:** tambahkan node **Category to Number (Apply)**. Masukkan port PMML dari *Category to Number (#4)* dan data uji dari *Table Partitioner*, lalu sambungkan output-nya ke *Decision Tree Predictor (#11)*. Setelah itu workflow perlu dijalankan ulang untuk mendapatkan angka SMOTE yang benar.

Untuk data campuran numerik dan kategorikal, varian yang lebih tepat adalah **SMOTE-NC**, yang diuji di [Orange + Python](../../orange/) dan [notebook Colab](../../colab/).

## Model PMML

Folder [`pmml/`](pmml/) berisi model yang diekspor dari workflow ini, untuk dipakai di luar KNIME:

| File | Asal |
|---|---|
| `model_tanpa_balancing.pmml` | Decision Tree Learner (#6) |
| `model_smote.pmml` | Decision Tree Learner (#8) |
| `category_to_number.pmml` | Category to Number (#4) |

Analisis lengkap ada di [laporan Pekan 3](../../laporan/03_Laporan_Pekan3_KNIME_Unbalanced.pdf).
