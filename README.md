# persenputihfoto

Program dalam Python ini menghitung derajat putih dari suatu gambar. Format gambar berekstensi BMP. Cara kerjanya adalah mengubah gambar menjadi grayscale kemudian dicari jumlah titik yang memiliki tingkat kecerahan dengan nilai pembeda adalah 128. Jika tingkat kecerahan < 128 dihitung sebagai gelap, sedangkan untuk >= 128 dianggap putih. Kemudian nilai prosentase kecerahan warna putih dihitung dengan membagi jumlah titik dilaikan 100.

Program penghitung prosentase titik warna gelap dan warna putih.
Program dibuat dalam rangka Pengabdian Kepada Masyarakat dana Internal
Universitas Negeri Malang 2022 dengan judul:
PENINGKATAN MUTU DAN KAPASITAS PRODUKSI MELALUI
UPGRADE POLISHER DENGAN ENERGI SURYA DI INDUSTRI KECIL
ANDROMEDA SUPPLIER” KOTA MALANG
Tim pelaksana: Yoyok Adisetio Laksono, Cahyo Aji Hapsoro, Hanif Izzuddin
Zaky, Sulistyo Gunawan

Cara penggunaan:
python wp.py namafile.bmp

namafile.bmp adalah foto beras yang akan diperiksa.
