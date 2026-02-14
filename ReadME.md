# Tugas Kecil 1 IF2211 Strategi Algoritma Semester II tahun 2025/2026 
## Penyelesaian Permainan *Queens LinkedIn*

## a. Penjelasan Singkat Program

Program ini merupakan implementasi algoritma brute force untuk menyelesaikan permainan *Queens LinkedIn* melalui kombinasi posisi Queen di setiap wilayah.

Program terdiri dari:
- `queens.py` di folder `src/` sebagai program utama
- File input `input.txt` di folder `test/` sebagai masukkan permainan *Queens LinkedIn* yang kosong
- File output `output.txt` di folder `test/` untuk menyimpan hasil yang paling baru

Program akan:
- Menampilkan live update kombinasi brute force di CLI setiap 0.3 detik agar tidak memenuhi layar terminal
- Menampilkan hasil akhir (solusi ditemukan atau tidak)
- Menampilkan total kombinasi yang dicek
- Menampilkan waktu pencarian program
- Membuat atau memperbarui `output.txt` di folder `test/` hanya jika solusi ditemukan

## b. Requirement Program

Program dibuat menggunakan:

- Python 3.14.3

Library yang digunakan (bawaan Python):
- `collections` (untuk mengelola dictionary)
- `itertools` (untuk menghasilkan kombinasi)
- `time` (untuk menghitung waktu pencarian)
- `sys` (untuk membaca file input)

## c. Cara Mengkompilasi Program

Program tidak perlu dikompilasi karena menggunakan bahasa Python (interpreted language).

## d. Cara Menjalankan dan Menggunakan Program

1. Pastikan terminal berada pada direktori utama project.
2. Jalankan program dengan format berikut

```
python src/queens.py test/input.txt
```
Setelah dijalankan, program akan:

- Menampilkan kombinasi yang sedang diuji setiap 0.3 detik
- Menampilkan hasil akhir (solusi ditemukan atau tidak)
- Menampilkan total kombinasi yang telah diperiksa
- Menampilkan waktu pencarian program
- Membuat atau memperbarui `output.txt` di folder `test/` jika solusi ditemukan

## e. Author

Nama: Reynard Anderson Wijaya  
NIM: 13524111
