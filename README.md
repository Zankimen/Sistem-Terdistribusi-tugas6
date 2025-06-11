# Sistem-Terdistribusi-tugas6
API server yang merspons berbagai bentuk file html atau txt (10kb, 100kb, 1mb)

Langkah-langkah untuk menjalankan:

1. Menjalankan `API.py` (Flask API), pastikan sudah punya Python 3 dan Flask.

    A. Install Flask

        Jika belum:

        pip install flask

    B. Jalankan API.py

        Lalu jalankan API-nya:

        python3 API.py


2. Menjalankan Load Testing dengan K6

    A. Pastikan K6 terinstal, cek dengan:

        k6 version

        Jika belum terinstal, instal dengan:

        brew install k6

    B. Jalankan Skenario `test.js`

    C. Jalankan dengan perintah:

        k6 run test.js


