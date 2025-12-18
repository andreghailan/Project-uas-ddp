import streamlit as st
from imt_bmi import ImtBmi
from dashboard import dashboard_page
from tentang_kami import tentang_kami
from riwayat import riwayat_page
from tips_kesehatan import tips_kesehatan
from landing import landing_page

if "imt_bmi" not in st.session_state:
    st.session_state.imt_bmi = ImtBmi()


with st.sidebar:
    st.title("Aplikasi Kalkulator Indeks Massa Tubuh (BMI)")
    menu = st.selectbox(
    "Menu",
    [
        "Halaman Utama",
        "Kalkulator Indeks Masa Tubuh (IBM)",
        "Tips Kesehatan",
        "Riwayat",
        "Tentang Kami"
    ]
)  

if menu == "Halaman Utama":
    landing_page()   
elif menu == "Kalkulator Indeks Masa Tubuh (IBM)":
    dashboard_page() 
elif menu == "Tips Kesehatan":
    tips_kesehatan()
elif menu == "Riwayat":
    riwayat_page()
elif menu == "Tentang Kami":
    tentang_kami()

