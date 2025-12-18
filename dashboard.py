import streamlit as st
import pandas as pd
from menu_utama import menu_utama



def dashboard_page():
   
    st.title('Cek Indeks Massa Tubuh Anda dengan Kalkulator IMT (BMI)')

    with st.form('my form'):
        st.write('Temukan IMT (BMI) Anda dan risiko kesehatan')     
        berat, tinggi, umur = st.columns(3)
        with berat:
            berat = st.number_input('Berat Badan ', value=None, min_value=0)

        with tinggi:
            tinggi = st.number_input('Tinggi Badan', value=None, min_value=0)
    
        with umur:
            umur = st.number_input('Usia', value=None, min_value=0)

        hasil = st.form_submit_button("Check Hasil")
            
            


    imt_ideal = None

    if hasil :
        if tinggi == None or berat == None:
            pass
            # st.warning('⚠️ Harap Diperhatikan jangan sampai kosong')
        elif tinggi :
            tinggi_m = tinggi / 100
            tinggi_k = tinggi_m * tinggi_m
            imt_ideal = berat / tinggi_k
            st.success(f"imt (BMI) : {imt_ideal:.1f}")
    else:
        if not hasil :
            st.markdown(':orange-badge[⚠️ Harap Diperhatikan jangan sampai kosong]')

    klasifikasi = None



    if hasil: 
        if tinggi == None or berat == None:
            pass
        elif imt_ideal is not None:
                if imt_ideal < 18.5:
                    klasifikasi = 'Berat badan kurang'
                    st.warning('Klasifikasi : Berat badan kurang')
                    st.info("""
                *Saran Kesehatan:*
                * Tingkatkan asupan kalori dengan makanan bergizi (protein dan lemak sehat).
                * Makan lebih sering dengan porsi kecil.
                * Lakukan latihan beban untuk membangun massa otot.
                """)
                elif 18.5 <= imt_ideal <= 22.9:
                    klasifikasi = 'Berat badan normal'
                    st.success('Klasifikasi : Berat badan normal')
                    st.info("""
                *Saran Kesehatan:*
                * Pertahankan pola makan seimbang saat ini.
                * Tetap aktif bergerak minimal 30 menit sehari.
                * Pastikan hidrasi tubuh tercukupi.
                """)
                elif 23 <= imt_ideal <= 24.9:
                    klasifikasi = 'Berat badan lebih'
                    st.info('Klasifikasi : Berat badan lebih')
                    st.info("""
                *Saran Kesehatan:*
                * Kurangi konsumsi gula dan karbohidrat olahan.
                * Tingkatkan aktivitas fisik (kardio seperti jalan cepat atau bersepeda).
                * Perhatikan kontrol porsi makan.
                """)
                elif 25 <= imt_ideal <= 29.9:
                    klasifikasi = 'Obesitas I'
                    st.error('Klasifikasi : Obesitas I')
                    st.info("""
                *Saran Kesehatan:*
                * Sangat disarankan berkonsultasi dengan ahli gizi atau dokter.
                * Mulai rutin berolahraga secara bertahap.
                * Fokus pada makanan utuh (whole foods) dan hindari makanan cepat saji.
                """)
                else:
                    klasifikasi = 'Obesitas II'
                    st.error('Klasifikasi : Obesitas II')
                    st.info("""
                *Saran Kesehatan:*
                * Sangat disarankan berkonsultasi dengan ahli gizi atau dokter.
                * Mulai rutin berolahraga secara bertahap.
                * Fokus pada makanan utuh (whole foods) dan hindari makanan cepat saji.
                """)

        if st.session_state.imt_bmi.simpan_riwayat(berat, tinggi, umur, imt_ideal, klasifikasi):
            # st.success("Riwayat berhasil disimpan!")
            pass
        else:
            st.error("Harap isi semua kolom dengan benar.")
        
        # st.button("Home", on_click=menu_utama)
        
            



    confusion_matrix = pd.DataFrame(
    {
        "IMT (BMI)": ["Di bawah 18.5", "18.5 - 22.9", "23 - 24.9", "25 - 29.9", "30 dan ke atas"]
    },
    index=["Berat badan kurang", "Berat badan normal", "Berat badan lebih", "Obesitas I", "Obesitas II"],
    )
    confusion_matrix.index.name = "Klasifikasi"
    st.table(confusion_matrix)  
