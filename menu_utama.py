import streamlit as st
import pandas as pd

def menu_utama():
    st.title("Selamat Datang di Aplikasi Kalkulator Indeks Massa Tubuh")
    st.image("images/bmi.png", use_container_width=True, caption="Aplikasi Kalkulator IMT (BMI)")
    st.title("Cek IMT (BMI) Anda dengan Kalkulator IMT (BMI)")
    st.write("Indeks Massa Tubuh (IMT) / Body Massa Index (BMI) adalah alat yang sering digunakan sebagai ukuran pengganti " \
    "lemak tubuh, dan dapat mendeteksi obesitas serta risiko kesehatan yang terkait. " \
    "IMT (BMI) dapat dihitung menggunakan kalkulator IMT (BMI) berdasarkan tinggi dan berat badan, " \
    "dan hasilnya dapat dikategorikan ke dalam kelas yang berbeda, mulai dari kurang berat badan hingga obesitas kelas II.")

    st.header("**Mengapa IMT (BMI) penting untuk diketahui?**")
    st.write("IMT (BMI) adalah cara yang baik untuk memeriksa risiko penyakit yang terkait dengan lemak tubuh. " \
    "Hidup dengan kelebihan berat badan atau obesitas dikaitkan dengan peningkatan risiko kematian dan penyakit atau kondisi lainnya. " \
    "Secara umum, semakin tinggi IMT (BMI) Anda, semakin besar risiko terkena penyakit kronis terkait obesitas lainnya, termasuk:")

    st.write(""" 
    1. Diabetes tipe II
    2. Tekanan darah tinggi
    3. Penyakit jantung koroner
    4. Penyakit batu empedu
    5. Infertilitas
    """)

    st.header("**Apa Batasan IMT (BMI)?**")
    st.write("IMT (BMI) adalah pengukuran sederhana dan objektif, tetapi dapat menyesatkan dalam beberapa kasus dan untuk beberapa kelompok orang. " \
    "Penelitian telah menunjukkan bahwa BMI kurang akurat dalam memprediksi risiko penyakit pada orang yang lebih tua, atlet, mereka yang bertubuh tinggi atau pendek, dan mereka dengan tubuh yang lebih berotot. " \
    "Misalnya, atlet elit atau binaragawan memiliki lebih banyak otot dan berat badan lebih besar, yang membuat IMT (BMI) mereka lebih tinggi.")