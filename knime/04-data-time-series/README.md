# Data Deret Waktu (Time Series)

**Workflow:** `Data_Time_Series.knwf`
**Dataset:** `DailyDelhiClimateTest.csv`
**Video:** _(tambahkan link)_

## Alur

```
CSV Reader → String to Date/Time → Sorter → Missing Value → Date/Time Part Extractor
→ Numeric Outliers → Date/Time to legacy Date/Time → Line Chart (JFreeChart)
```

| Node | Fungsi |
|------|--------|
| String to Date/Time | Mengubah kolom tanggal dari teks menjadi tipe tanggal |
| Sorter | Mengurutkan data berdasarkan tanggal (wajib untuk deret waktu) |
| Missing Value | Menangani tanggal atau nilai yang kosong |
| Date/Time Part Extractor | Mengambil bagian tanggal (bulan, hari, dll.) |
| Numeric Outliers | Mendeteksi dan menangani pencilan |
| Date/Time to legacy Date/Time | Mengubah format tanggal agar bisa dibaca node Line Chart |
| Line Chart (JFreeChart) | Visualisasi tren dari waktu ke waktu |

Penjelasan lengkap ada di [laporan Pekan 1](../../laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf).
