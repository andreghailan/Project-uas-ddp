import streamlit as st
from imt_bmi import ImtBmi
from streamlit_option_menu import option_menu 
from dashboard import dashboard_page
from menu_utama import menu_utama
from tentang_kami import tentang_kami
from riwayat import riwayat_page
from tips_kesehatan import tips_kesehatan

if "imt_bmi" not in st.session_state:
    st.session_state.imt_bmi = ImtBmi()


with st.sidebar:
    st.title("Aplikasi Kalkulator Indeks Massa Tubuh (BMI)")
    menu = option_menu(
        "Menu",
        ['Dashboard', "Indeks Masa Tubuh (IBM)", "Tips Kesehatan", 
         "Riwayat", "Tentang Kami"],
         icons=["house", "calculator", "lightbulb", "clock-history", "info-circle"],
        menu_icon="list",
        default_index=0,
    )      

if menu == 'Dashboard':
    menu_utama() 
elif menu == "Indeks Masa Tubuh (IBM)":
    dashboard_page() 
elif menu == "Tips Kesehatan":
    tips_kesehatan()
elif menu == "Riwayat":
    riwayat_page()
elif menu == "Tentang Kami":
    tentang_kami()

