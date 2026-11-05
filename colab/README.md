# Kompatibilitas dengan Google Colab

| No | Notebook | Isi | Buka |
|----|----------|-----|------|
| 01 | [`01_orange_balancing_di_colab.ipynb`](01_orange_balancing_di_colab.ipynb) | Workflow Orange (Tree + undersampling + SMOTE-NC) dijalankan ulang di Colab tanpa GUI, ditambah eksperimen 15 fitur | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Raditxt/eksplorasi-knime-orange-n8n/blob/main/colab/01_orange_balancing_di_colab.ipynb) |
| 02 | _(menyusul)_ | Versi notebook dari workflow KNIME (pandas + scikit-learn) | – |

Dataset dibaca langsung dari folder `datasets/` di repo ini, jadi notebook bisa langsung dijalankan tanpa upload file.

## Temuan Sementara

### Orange: kompatibel ✅

Orange juga library Python (`pip install orange3`). Widget-nya bisa ditulis ulang sebagai kode dan dijalankan di Colab.

| Skenario (7 fitur) | GUI Orange (F1) | Colab (F1) |
|---|---:|---:|
| A. Tanpa balancing | 27,1% | 27,1% |
| B. Undersampling acak | 26,9% | 26,9% |
| C. SMOTE-NC | 24,7% | 24,3% |

Skenario A dan B identik. Selisih kecil di SMOTE-NC bukan karena versi scikit-learn (sudah diuji dengan versi yang sama, 1.5.2). Dugaan yang tersisa: perbedaan sistem operasi dalam memilih tetangga terdekat yang jaraknya seri, atau perbedaan cara membaca CSV. Penjelasannya ada di notebook.

**Eksperimen tambahan:** dengan 15 fitur (semua kecuali `duration`), SMOTE-NC menjadi skenario terbaik (F1 38,5%, dibanding 32,0% tanpa balancing). Artinya efek balancing sangat bergantung pada kualitas fitur yang dipakai.

### KNIME: tidak bisa dijalankan langsung ⚠️

KNIME adalah aplikasi desktop berbasis Java, sehingga tidak bisa dijalankan di Colab. Pilihannya:
- menulis ulang workflow sebagai notebook (pandas + scikit-learn), atau
- bertukar data dan model antara KNIME dan Colab (CSV, PMML, ONNX).

Ini akan diuji di notebook 02.

## Perbandingan Singkat

| Aspek | GUI (Orange/KNIME) | Google Colab |
|---|---|---|
| Instalasi | Perlu dipasang di laptop | Tidak perlu, cukup browser |
| Pustaka tambahan (misalnya imbalanced-learn) | Orange: dipasang manual ke Python milik Orange | `pip install` di sel notebook |
| Visualisasi interaktif | Tersedia | Perlu ditulis sendiri (matplotlib/pandas) |
| Berbagi hasil | Kirim file `.ows` / `.knwf` | Kirim link notebook |
| Reproduksibilitas | Bergantung setting widget | Kode dan versi pustaka tercatat di notebook |
