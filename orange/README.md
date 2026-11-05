# Orange Data Mining

**Workflow:** `orange-bank-marketing.ows`
**Dataset:** `../datasets/bank-full.csv` (path relatif, langsung terbaca jika struktur folder repo tidak diubah)
**Video:** _(menyusul)_

Workflow ini berisi dua bagian.

## Bagian 1: Eksplorasi & Perbandingan Model

```
CSV File Import → Data Table → Data Info / Distributions
CSV File Import → Select Columns (16 fitur) → Tree / Naive Bayes / Random Forest → Test and Score → Confusion Matrix
```

Evaluasi memakai cross validation 10 fold, stratified. Detail dan perbandingannya dengan KNIME ada di [laporan Orange](../laporan/04_Laporan_Orange_Data_Mining.pdf).

## Bagian 2: Balancing dengan Python

Orange belum punya widget SMOTE bawaan, jadi balancing dilakukan lewat widget **Python Script** dengan pustaka `imbalanced-learn`.

```
CSV File Import → Select Columns (1) → Data Sampler (70:30, stratified, seed)
   ├─ Data Sample ───────────────────────────────→ Test and Score (3) → Confusion Matrix (3)   tanpa balancing
   ├─ Data Sample → Python Script (undersampling) → Test and Score (1) → Confusion Matrix (1)
   ├─ Data Sample → Python Script (1) (SMOTE-NC) ─→ Test and Score (2) → Confusion Matrix (2)
   └─ Remaining Data ──────────────────────────────→ data uji untuk ketiga Test and Score
```

Kolom yang dipakai sama dengan eksperimen KNIME (age, job, marital, education, balance, housing, loan, y) supaya hasilnya bisa dibandingkan. Model: Tree. Test and Score diatur ke **Test on test data**.

Script Python-nya juga tersedia sebagai file terpisah:
- [`scripts/undersampling_acak.py`](scripts/undersampling_acak.py)
- [`scripts/smote_nc.py`](scripts/smote_nc.py)

### Memasang imbalanced-learn di Orange

Installer Orange (standalone) memakai Python-nya sendiri, jadi pustaka harus dipasang ke interpreter milik Orange:

1. Di widget Python Script, jalankan `import sys; print(sys.executable)` untuk melihat lokasi Python Orange (contoh: `D:\Orange\python.exe`).
2. Buka Command Prompt, lalu jalankan:
   ```
   "D:\Orange\python.exe" -m pip install imbalanced-learn --dry-run
   "D:\Orange\python.exe" -m pip install imbalanced-learn
   ```
   Opsi `--dry-run` dipakai dulu untuk memastikan pemasangan tidak mengubah versi pustaka bawaan Orange.
3. Tutup lalu buka ulang Orange.

### Hasil (kelas positif = `yes`)

| Skenario | Recall | Precision | F1 | Accuracy |
|----------|-------:|----------:|---:|---------:|
| Tanpa balancing | 23,3% | 32,3% | 27,1% | 85,3% |
| Undersampling acak | 58,6% | 17,4% | 26,9% | 62,7% |
| SMOTE-NC | 25,1% | 24,2% | 24,7% | 82,0% |

Polanya mirip dengan hasil di KNIME: undersampling menaikkan recall dengan mengorbankan precision. SMOTE-NC sudah menangani atribut kategorikal dengan benar, tetapi tetap tidak lebih baik dari baseline. Kemungkinan penyebabnya: ketujuh fitur ini (data demografis dan keuangan) kurang bisa membedakan kelas `yes` dan `no`, sehingga sampel sintetis jatuh di daerah yang tumpang tindih.

Analisis lengkap ada di [laporan Orange dengan Python](../laporan/05_Laporan_Orange_dengan_Python.pdf).
