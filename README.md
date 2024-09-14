# Chelsea FC Squad Web Scraping Project

## Tujuan
Web scraping data tim sepak bola Chelsea menggunakan **BeautifulSoup** dan menyimpan hasilnya dalam bentuk file **CSV**. Data yang diambil mencakup informasi tentang squad chelsea, yang kemudian disimpan ke file CSV.

## Proses
1. **Pengambilan Data**: Saya menggunakan modul `requests` untuk mengambil halaman web dari situs ESPN, kemudian menggunakan `BeautifulSoup` untuk memparsing HTML-nya.
2. **Scraping Tabel**: Saya menemukan dua tabel di halaman yang memiliki elemen dan class yang sama, yaitu `table` dengan class `Table`. Masing-masing tabel berisi data yang berbeda, satu untuk penjaga gawang (goalkeepers) dan satu untuk pemain lapangan (outfield players).
3. **Penyimpanan Data**: Setelah scraping data dari masing-masing tabel, saya menyimpannya ke dalam dua file CSV terpisah, `chelsea_goalkeepers.csv` dan `chelsea_outfield_players.csv`, menggunakan **Pandas**.

## Hasil
- File CSV berhasil dibuat untuk kedua tabel: satu untuk **goalkeepers** dan satu lagi untuk **outfield players**.
- Tabel berisi kolom seperti nama pemain, posisi, usia, tinggi badan, berat badan, kewarganegaraan, dan statistik performa.

## Kendala
Saya masih mengalami kebingungan kenapa isi pada file CSV berada di satu kolom sel saja untuk setiap data pemain.
