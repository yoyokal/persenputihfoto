# Program penghitung prosentase titik warna gelap dan warna putih.
# Program dibuat dalam rangka Pengabdian Kepada Masyarakat dana Internal
# Universitas Negeri Malang 2022 dengan judul:
# PENINGKATAN MUTU DAN KAPASITAS PRODUKSI MELALUI
# UPGRADE POLISHER DENGAN ENERGI SURYA DI INDUSTRI KECIL
# ANDROMEDA SUPPLIER” KOTA MALANG
# Tim pelaksana: Yoyok Adisetio Laksono, Cahyo Aji Hapsoro, Hanif Izzuddin
# Zaky, Sulistyo Gunawan
#
# penggunaan:
# python wp.py namafile.bmp
#
# namafile.bmp adalah foto beras yang akan diperiksa.

import cv2 as cv
import numpy as np
import sys

# fungsi penghitung persentase putih
def persenPutih(namafile):
    RGB = cv.imread(namafile)
    grayscale = cv.cvtColor(RGB, cv.COLOR_BGR2GRAY)
    
    jumlahTotalTitik = grayscale.shape[1-1] * grayscale.shape[2-1]
    jumlahTotalTitikHitam = np.count_nonzero(grayscale < 128)
    jumlahTotalTitikPutih = np.count_nonzero(grayscale >= 128)
    
    # Hitung prosentase
    prosenTitikPutih = jumlahTotalTitikPutih / jumlahTotalTitik * 100
    if (jumlahTotalTitikHitam + jumlahTotalTitikPutih) != jumlahTotalTitik:
        return -1
    else:
        return(prosenTitikPutih)

# ambil nama file yang akan diperiksa
namafile = str(sys.argv[1])
# hitung prosentase
psn = persenPutih(namafile)
if psn == -1:
    print("Error!")
else:
    print("Persentase putih = %5.2f%%" % psn)