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
- SMOTE justru lebih buruk dari baseline. Penyebab paling mungkin: *Category to Number* memberi angka acak pada kategori nominal, lalu SMOTE menginterpolasi angka tersebut sehingga terbentuk kategori sintetis yang tidak bermakna. Varian yang tepat untuk data campuran adalah **SMOTE-NC**, yang diuji di [Orange + Python](../../orange/).

Analisis lengkap ada di [laporan Pekan 3](../../laporan/03_Laporan_Pekan3_KNIME_Unbalanced.pdf).
