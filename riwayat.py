import streamlit as st
import pandas as pd

def riwayat_page():
    st.title("Riwayat Indeks Massa Tubuh (IMT/BMI) Anda")

    imt_bmi = st.session_state.imt_bmi
    riwayat = imt_bmi.riwayat

    if riwayat.empty:
        st.info("Belum ada riwayat yang disimpan.")
    else:
        st.dataframe(riwayat)

        # Opsi untuk menghapus riwayat
    if st.button("Hapus Riwayat"):
        imt_bmi.riwayat = pd.DataFrame(columns=riwayat.columns)
        imt_bmi._save_data()
        st.success("Riwayat berhasil dihapus.")
        st.rerun()