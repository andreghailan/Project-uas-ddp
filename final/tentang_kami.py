import streamlit as st

def tentang_kami():
    st.header("Tentang Kami")
    st.subheader("Aplikasi Kalkulator Indeks Massa Tubuh (IMT / BMI)")
    st.write("""
    Aplikasi Kalkulator Indeks Massa Tubuh (IMT / BMI) bertujuan untuk memudahkan pengguna menghitung dan memahami status berat badan mereka secara cepat — apakah kekurangan, normal, kelebihan, atau obesitas. 
    Aplikasi ini dirancang untuk memberikan hasil yang akurat, penjelasan singkat tentang risiko kesehatan terkait, serta rekomendasi tindakan sederhana untuk gaya hidup sehat, 
    sehingga akses informasi kesehatan menjadi transparan dan mudah dipahami oleh semua pengguna.
    
    **Fitur Utama:**
    - **Dashboard:** Menampilkan ringkasan cepat seperti berat badan terakhir, hasil IMT, serta kategori kesehatan pengguna dalam satu layar.
    - **Indeks Massa Tubuh (IMT):** Menghitung IMT secara akurat berdasarkan berat dan tinggi badan, lengkap dengan kategori kesehatan.
    - **Tips Kesehatan:** Memberikan saran praktis terkait pola makan, aktivitas fisik, dan gaya hidup sehat sesuai kategori IMT.
    - **Riwayat:** Menyimpan catatan perhitungan IMT sebelumnya sehingga pengguna dapat memantau perubahan dari waktu ke waktu.
    - **Tentang Kami:** Berisi informasi singkat mengenai tujuan aplikasi dan tim pengembang.
    """)

    st.subheader("Visi dan Misi")
    st.write("""
    **Visi :** 
   Mewujudkan masyarakat yang lebih sadar kesehatan dengan menyediakan akses informasi IMT yang akurat, mudah digunakan, dan membantu pengguna mengambil keputusan yang lebih sehat dalam kehidupan sehari-hari.

    **Misi**:
    1. Menyediakan perhitungan IMT yang cepat, akurat, dan mudah dipahami oleh semua kalangan.
    2. Membantu pengguna memantau perubahan kesehatan melalui fitur riwayat dan pencatatan berkala.
    3. Memberikan edukasi kesehatan berupa tips dan rekomendasi yang relevan sesuai kategori IMT pengguna.
    4. Mendorong kebiasaan hidup sehat dengan informasi yang sederhana namun berbasis data.
    5. Menghadirkan antarmuka yang ramah pengguna sehingga akses terhadap informasi kesehatan menjadi lebih inklusif dan terbuka untuk semua.
    """)

    st.subheader("Tim Kami")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("final/images/agung.jpg", caption="Agung Kurniawan", width=150)
        st.write("Anggota - 0110124136")
    with col2:
        st.image("final/images/aziz.jpg", caption="Abdul Aziz", width=150)
        st.write("Anggota - 0110124095")
    with col3:
        st.image("final/images/andre.jpg", caption="Andre Ghailan Pratama", width=150)
        st.write("Ketua - 0110124136")
    with col4:
        st.image("final/images/ridho.jpg", caption="Abdul Aziz", width=150)
        st.write("Anggota - 0110124095")
