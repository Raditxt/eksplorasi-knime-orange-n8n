# Dataset

Semua dataset adalah dataset publik. Unduh dari link di bawah, lalu simpan di folder ini dengan nama file seperti pada kolom **Nama file**.

| Dipakai di | Tipe data | Dataset | Nama file | Sumber |
|-----------|-----------|---------|-----------|--------|
| KNIME 01 | Interval | Global Land Temperatures by City (Berkeley Earth) | `GlobalLandTemperaturesByCity.csv` | [Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) |
| KNIME 01 | Rasio | Salary Data (Experience, Age, Gender, Job Title, Education) | `Salary_Data.csv` | [Kaggle](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data) |
| KNIME 02, 06, Orange | Nominal & ordinal | UCI Bank Marketing | `bank-full.csv` | [UCI](https://archive.ics.uci.edu/dataset/222/bank+marketing) / [Kaggle](https://www.kaggle.com/datasets/adityamhaske/bank-marketing-dataset) |
| KNIME 03 | Teks | Twitter Tweets Sentiment Dataset | `Tweets.csv` | [Kaggle](https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset) |
| KNIME 04 | Deret waktu | Daily Climate Time Series Data (Delhi) | `DailyDelhiClimateTest.csv` | [Kaggle](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data) |
| KNIME 05 | Gambar | Intel Image Classification (subset 15–20 gambar dari folder `seg_pred`) | `seg_pred/*.jpg` | [Kaggle](https://www.kaggle.com/datasets/puneet6060/intel-image-classification) |

## Catatan

- `bank-full.csv` memakai pemisah titik koma (`;`), bukan koma.
- `GlobalLandTemperaturesByCity.csv` berukuran ratusan MB sehingga tidak bisa disimpan di GitHub (batas 100 MB per file). File ini tidak ikut di-commit dan perlu diunduh sendiri.
- Untuk data gambar, cukup extract saja file `datasets/seg_pred.zip`, dan pilih beberapa file saja tidak usah seluruh dataset.

Struktur folder yang diharapkan:

```
datasets/
├── bank-full.csv
├── Salary_Data.csv
├── GlobalLandTemperaturesByCity.csv   (tidak di-commit)
├── Tweets.csv
├── DailyDelhiClimateTest.csv
└── seg_pred/
    ├── 11.jpg
    └── ...
```
