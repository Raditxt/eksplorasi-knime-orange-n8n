# KNIME Analytics Platform

Workflow KNIME untuk data preparation tiap tipe data dan penanganan unbalanced dataset. Dibuat dengan KNIME Analytics Platform 5.11.

| Folder | Topik | Dataset |
|--------|-------|---------|
| [`01-data-numerik`](01-data-numerik/) | Data interval & rasio | Global Land Temperatures, Salary Data |
| [`02-data-kategorikal`](02-data-kategorikal/) | Data nominal & ordinal | Bank Marketing |
| [`03-data-teks`](03-data-teks/) | Data teks | Twitter Tweets Sentiment |
| [`04-data-time-series`](04-data-time-series/) | Data deret waktu | Daily Delhi Climate |
| [`05-data-image`](05-data-image/) | Data gambar | Intel Image Classification |
| [`06-unbalanced-dataset`](06-unbalanced-dataset/) | Balancing: Equal Size Sampling & SMOTE | Bank Marketing |

## Cara Membuka Workflow

1. Buka KNIME → **File → Import KNIME Workflow…** → pilih file `.knwf`.
2. Dataset di workflow masih mengarah ke path lokal laptop saya (misalnya `D:\bank-full.csv\bank-full.csv`). Buka node **CSV Reader** (atau **Image Reader**), lalu arahkan ke file di folder `datasets/` repo ini.
   - Supaya tidak perlu diatur ulang di komputer lain, pilih mode **Relative to → Current workflow** lalu isi path seperti `../../datasets/bank-full.csv`.
3. Jalankan workflow dengan **Execute All** (Shift+F7).

## Ekstensi yang Dibutuhkan

- **KNIME Textprocessing**: untuk workflow `03-data-teks`
- **KNIME Image Processing**: untuk workflow `05-data-image`

KNIME biasanya menawarkan untuk memasang ekstensi yang kurang secara otomatis saat workflow dibuka.
