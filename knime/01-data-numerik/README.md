# Data Numerik (Interval & Rasio)

**Workflow:** `Data_Numerik.knwf`
**Dataset:** `GlobalLandTemperaturesByCity.csv` (interval), `Salary_Data.csv` (rasio)
**Video:** _(tambahkan link)_

Workflow ini terdiri dari dua cabang, satu untuk tiap skala data.

## Cabang 1: Data Interval (suhu)

```
CSV Reader → String to Date/Time → Date/Time Part Extractor → Row Filter → Missing Value → Numeric Outliers → Statistics
```

| Node | Fungsi |
|------|--------|
| CSV Reader | Membaca data suhu per kota |
| String to Date/Time | Mengubah kolom `dt` dari teks menjadi tanggal |
| Date/Time Part Extractor | Mengambil bagian tanggal (misalnya tahun) sebagai kolom baru |
| Row Filter | Menyaring data kota tertentu (Jakarta) |
| Missing Value | Menangani nilai suhu yang kosong |
| Numeric Outliers | Mengganti pencilan `AverageTemperature` dengan nilai batas terdekat yang masih wajar |
| Statistics | Statistik deskriptif hasil akhir |

## Cabang 2: Data Rasio (gaji)

```
CSV Reader → Missing Value → Numeric Outliers → Math Formula → Statistics / Box Plot
```

| Node | Fungsi |
|------|--------|
| CSV Reader | Membaca data gaji |
| Missing Value | Menangani nilai kosong |
| Numeric Outliers | Mendeteksi dan menangani pencilan |
| Math Formula | Transformasi log: `log($Salary$ + 1)` ke kolom `Salary_Log` |
| Statistics, Box Plot | Statistik deskriptif dan visualisasi distribusi |

Penjelasan lengkap ada di [laporan Pekan 1](../../laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf).
