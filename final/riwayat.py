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
    
    if 'data_updated' not in st.session_state:
        st.session_state.data_updated = False

    def update_data():
        st.session_state.data_updated = True
        st.rerun()

        # ini untuk hapus riwayat guys
    if st.button("Hapus Riwayat", on_click=update_data):
        imt_bmi.riwayat = pd.DataFrame(columns=riwayat.columns)
        imt_bmi._save_data()
        st.success("Riwayat berhasil dihapus.")
        st.rerun()