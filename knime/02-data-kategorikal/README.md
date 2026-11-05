# Data Kategorikal (Nominal & Ordinal)

**Workflow:** `Data_Kategorikal.knwf`
**Dataset:** `bank-full.csv` (pemisah `;`)
**Video:** _(tambahkan link)_

## Cabang 1: Data Nominal

```
CSV Reader → String Manipulation (×4) → Missing Value → GroupBy (×4) → Bar Chart (×4)
```

| Node | Fungsi |
|------|--------|
| CSV Reader | Membaca `bank-full.csv` |
| String Manipulation (×4) | Membersihkan teks kategori, misalnya `strip(replace($job$, ".", ""))` |
| Missing Value | Menangani nilai kosong |
| GroupBy (×4) | Menghitung frekuensi tiap kategori (job, marital, dll.) |
| Bar Chart (×4) | Visualisasi frekuensi tiap kategori |

## Cabang 2: Data Ordinal

```
CSV Reader → Rule Engine → Missing Value → GroupBy → Sorter → Bar Chart
```

| Node | Fungsi |
|------|--------|
| Rule Engine | Memberi peringkat pendidikan ke kolom `Education_Rank`: primary = 1, secondary = 2, tertiary = 3, unknown = 0 |
| Missing Value | Menangani nilai kosong |
| GroupBy, Sorter | Menghitung frekuensi lalu mengurutkan sesuai peringkat |
| Bar Chart | Visualisasi distribusi tingkat pendidikan |

Penjelasan lengkap ada di [laporan Pekan 1](../../laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf).
