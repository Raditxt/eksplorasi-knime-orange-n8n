# Data Teks

**Workflow:** `Data_Teks.knwf`
**Dataset:** `Tweets.csv` (kolom: `textID`, `text`, `selected_text`, `sentiment`)
**Video:** _(tambahkan link)_
**Ekstensi:** KNIME Textprocessing

## Alur

```
CSV Reader → Strings to Document → Case Converter → Punctuation Erasure → Number Filter
→ Stop Word Filter → Snowball Stemmer → Bag Of Words Creator → TF → GroupBy
```

| Node | Fungsi |
|------|--------|
| Strings to Document | Mengubah kolom teks menjadi tipe *Document* agar bisa diproses node teks |
| Case Converter | Mengubah semua huruf menjadi kecil |
| Punctuation Erasure | Menghapus tanda baca |
| Number Filter | Menghapus angka |
| Stop Word Filter | Menghapus kata umum (the, and, is, ...) |
| Snowball Stemmer | Mengembalikan kata ke bentuk dasarnya |
| Bag Of Words Creator | Memecah dokumen menjadi daftar kata |
| TF | Menghitung frekuensi kata (term frequency) |
| GroupBy | Merangkum kata yang paling sering muncul |

Penjelasan lengkap ada di [laporan Pekan 1](../../laporan/01_Laporan_Pekan1_KNIME_Tipe_Data.pdf).
