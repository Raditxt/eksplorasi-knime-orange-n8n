# Kompatibilitas dengan Google Colab

| No | Notebook | Isi | Buka |
|----|----------|-----|------|
| 01 | [`01_orange_balancing_di_colab.ipynb`](01_orange_balancing_di_colab.ipynb) | Workflow Orange (Tree + undersampling + SMOTE-NC) dijalankan ulang di Colab tanpa GUI, ditambah eksperimen 15 fitur | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Raditxt/eksplorasi-knime-orange-n8n/blob/main/colab/01_orange_balancing_di_colab.ipynb) |
| 02 | [`02_knime_balancing_di_colab.ipynb`](02_knime_balancing_di_colab.ipynb) | Workflow KNIME Unbalanced ditulis ulang dengan pandas + scikit-learn, ditambah menjalankan model KNIME (PMML) di Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Raditxt/eksplorasi-knime-orange-n8n/blob/main/colab/02_knime_balancing_di_colab.ipynb) |

Dataset dan model dibaca langsung dari repo ini, jadi notebook bisa langsung dijalankan tanpa upload file.

## Temuan Sementara

### Orange: kompatibel ✅

Orange juga library Python (`pip install orange3`). Widget-nya bisa ditulis ulang sebagai kode dan dijalankan di Colab.

| Skenario (7 fitur) | GUI Orange | Notebook di Windows (Python Orange) | Notebook di Colab |
|---|---:|---:|---:|
| A. Tanpa balancing (F1) | 27,1% | 27,1% | 27,1% |
| B. Undersampling acak (F1) | 26,9% | 26,9% | 26,9% |
| C. SMOTE-NC (F1) | 24,7% | 24,7% | 24,3% |

Di lingkungan yang sama (Windows), notebook mereproduksi GUI Orange 100%. Di Colab (Linux), hanya SMOTE-NC yang selisih sekitar 0,4 poin. Penyebabnya bukan versi pustaka atau kode, melainkan perbedaan platform dalam memilih tetangga terdekat yang jaraknya seri.

**Eksperimen tambahan:** dengan 15 fitur (semua kecuali `duration`), SMOTE-NC menjadi skenario terbaik (F1 38,5%, dibanding 32,0% tanpa balancing). Artinya efek balancing sangat bergantung pada kualitas fitur yang dipakai.

### KNIME: tidak bisa dijalankan langsung, tetapi bisa dijembatani ⚠️

KNIME adalah aplikasi desktop berbasis Java, sehingga tidak bisa dijalankan di Colab. Notebook 02 menguji dua cara menjembataninya:

1. **Menulis ulang workflow sebagai kode.** Setiap node punya padanan di pandas, scikit-learn, dan imbalanced-learn. Jumlah data latih dan uji sama persis dengan KNIME (31.647 dan 13.564 baris), tetapi angka evaluasinya tidak identik karena generator acak Java dan Python berbeda, dan algoritma Decision Tree-nya juga berbeda.
2. **Membawa model KNIME ke Colab lewat PMML.** Model Decision Tree dari KNIME ([`knime/06-unbalanced-dataset/pmml/`](../knime/06-unbalanced-dataset/pmml/)) dijalankan langsung di Python.

| Skenario (7 fitur, F1) | KNIME | Colab |
|---|---:|---:|
| A. Tanpa balancing | 28,4% | 25,2% |
| B. Equal Size Sampling | 26,5% | 26,3% |
| C. SMOTE | 14,3% | 22,2% |

**Temuan penting:** hasil SMOTE di KNIME buruk karena **kesalahan workflow**. Data uji tidak ikut melewati *Category to Number*, padahal model dilatih dengan data yang sudah di-encode. Saat model PMML dari KNIME dijalankan di Colab dengan data teks (seperti di workflow), hasilnya sama dengan KNIME (Recall 16,5%, Precision 12,6%, Kappa 0,011, praktis acak). Perbaikannya: tambahkan node *Category to Number (Apply)* sebelum *Decision Tree Predictor (#11)*.

## Perbandingan Singkat

| Aspek | GUI (Orange/KNIME) | Google Colab |
|---|---|---|
| Instalasi | Perlu dipasang di laptop | Tidak perlu, cukup browser |
| Pustaka tambahan (misalnya imbalanced-learn) | Orange: dipasang manual ke Python milik Orange | `pip install` di sel notebook |
| Visualisasi interaktif | Tersedia | Perlu ditulis sendiri (matplotlib/pandas) |
| Berbagi hasil | Kirim file `.ows` / `.knwf` | Kirim link notebook |
| Membawa model | KNIME: *PMML Writer* | Baca PMML di Python, atau ekspor model scikit-learn ke PMML |
| Reproduksibilitas | Bergantung setting widget | Kode dan versi pustaka tercatat di notebook |
