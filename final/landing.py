import streamlit as st
import pandas as pd

def landing_page():
    st.set_page_config(
        page_title="BMI Health Hub",
        page_icon="🧩",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.title("✨ Pentingnya Memahami BMI ✨")
    st.subheader("Body Mass Index bukan sekadar angka, tapi jendela awal menuju pemahaman kesehatan tubuh Anda.")
    st.divider()


    st.write("Indeks Massa Tubuh (IMT) / Body Massa Index (BMI) adalah alat yang sering digunakan sebagai ukuran pengganti " \
    "lemak tubuh, dan dapat mendeteksi obesitas serta risiko kesehatan yang terkait. " \
    "IMT (BMI) dapat dihitung menggunakan kalkulator IMT (BMI) berdasarkan tinggi dan berat badan, " \
    "dan hasilnya dapat dikategorikan ke dalam kelas yang berbeda, mulai dari kurang berat badan hingga obesitas kelas II.")

    col_formula, col_info = st.columns([1, 2])

    with col_formula:
        with st.container(border=True):
            st.markdown("### 🧮 Rumus BMI")
            st.write("Berat (kg) dibagi Tinggi Kuadrat (m²)")
            st.latex(r'''BMI = \frac{Berat (kg)}{Tinggi (m)^2}''')

    with col_info:
        with st.container(border=True):
            st.markdown("### 💡 Tahukah Anda?")
            st.info("BMI adalah metode skrining standar WHO yang paling mudah untuk mendeteksi risiko kesehatan sejak dini. Angka ini membantu menentukan apakah Anda berada di zona: Kekurangan berat, Sehat, atau Berisiko Obesitas.")

    st.header("🍭 Klasifikasi Standar WHO 🍭")

    st.header("**Mengapa IMT (BMI) penting untuk diketahui?**")
    st.write("IMT (BMI) adalah cara yang baik untuk memeriksa risiko penyakit yang terkait dengan lemak tubuh. " \
    "Hidup dengan kelebihan berat badan atau obesitas dikaitkan dengan peningkatan risiko kematian dan penyakit atau kondisi lainnya. " \
    "Secara umum, semakin tinggi IMT (BMI) Anda, semakin besar risiko terkena penyakit kronis terkait obesitas lainnya.")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.write("🥗 Kurang")
            st.metric(label="BMI", value="< 18.5", delta="Butuh Nutrisi", delta_color="off")
            st.info("Kekurangan Berat Badan")

    with c2:
        with st.container(border=True):
            st.write("💪 Normal")
            st.metric(label="BMI", value="18.5 - 24.9", delta="Ideal", delta_color="normal")
            st.success("Berat Badan Sehat & Ideal")

    with c3:
        with st.container(border=True):
            st.write("⚠️ Berat Badan Lebih")
            st.metric(label="BMI", value="25.0 - 29.9", delta="Waspada", delta_color="inverse")
            st.warning("Kelebihan Berat Badan")

    with c4:
        with st.container(border=True):
            st.write("🚨 Obesitas")
            st.metric(label="BMI", value="≥ 30.0", delta="Berisiko", delta_color="inverse")
            st.error("Obesitas Tingkat I-III")

    st.divider()

    col_risk_layout, _ = st.columns([2, 0.1])
    with col_risk_layout:
        st.subheader("🏥 Risiko Kesehatan Obesitas")
        with st.expander("💔 Jantung & Pembuluh Darah", expanded=True):
            st.write("Meningkatkan risiko tekanan darah tinggi (hipertensi) dan penyakit jantung koroner karena beban kerja jantung yang lebih berat.")
        with st.expander("🩸 Diabetes Tipe 2"):
            st.write("Sel lemak yang berlebih, terutama di perut, membuat tubuh resisten terhadap insulin, menyebabkan gula darah naik.")
        with st.expander("🦴 Masalah Persendian (Osteoarthritis)"):
            st.write("Beban tubuh berlebih memberikan tekanan ekstra pada sendi penopang berat badan seperti lutut dan punggung bawah.")

    st.header("**Apa Batasan IMT (BMI)?**")
    st.write("IMT (BMI) adalah pengukuran sederhana dan objektif, tetapi dapat menyesatkan dalam beberapa kasus dan untuk beberapa kelompok orang. " \
    "Penelitian telah menunjukkan bahwa BMI kurang akurat dalam memprediksi risiko penyakit pada orang yang lebih tua, atlet, mereka yang bertubuh tinggi atau pendek, dan mereka dengan tubuh yang lebih berotot. " \
    "Misalnya, atlet elit atau binaragawan memiliki lebih banyak otot dan berat badan lebih besar, yang membuat IMT (BMI) mereka lebih tinggi.")

    # st.divider()
    # st.header("📰 Jurnal Sehat & Berita")

    # tab1, tab2, tab3 = st.tabs(["🏆 Kisah Sukses", "🌍 Data WHO", "🍳 Resep Sehat"])

    # with tab1:
    #     st.subheader("🔥 Transformasi Nyata")
    #     s1, s2 = st.columns(2)
    #     with s1:
    #         with st.container(border=True):
    #             st.caption("Inspirasi Lokal")
    #             st.markdown("### Perjalanan Tya Ariestya")
    #             st.write("Demi program hamil, Tya disiplin jalan kaki 45 menit/hari nonstop dan makan terjadwal (5-6x porsi kecil). Tanpa tepung & santan.")
    #             st.success("Turun 24 Kg")
    #     with s2:
    #         with st.container(border=True):
    #             st.caption("Diet Sehat")
    #             st.markdown("### Sarah Ayu & Jendela Makan")
    #             st.write("Berhasil memangkas berat badan dengan metode Intermittent Fasting. Jendela makan 6 jam, puasa 18 jam, serta minum banyak air putih.")
    #             st.success("Turun 13 Kg")

    # with tab2:
    #     d1, d2 = st.columns(2)
    #     with d1:
    #         with st.container(border=True):
    #             st.markdown("### 📊 Fakta WHO 2024")
    #             st.write("- *1 dari 8 orang* di dunia hidup dengan obesitas.")
    #             st.write("- Kasus obesitas dewasa naik *2x lipat* sejak 1990.")
    #             st.error("Obesitas meningkatkan risiko Kanker & Diabetes.")
    #     with d2:
    #         st.markdown("##### 📈 Tren Kenaikan Global (Juta Orang)")
    #         chart_data = pd.DataFrame({
    #             "Tahun": ["1990", "2000", "2010", "2022", "2030"],
    #             "Juta Orang": [200, 350, 500, 890, 1200]
    #         })
    #         st.bar_chart(chart_data, x="Tahun", y="Juta Orang", color="#ff4b4b")

    # with tab3:
    #     r1, r2 = st.columns(2)
    #     with r1:
    #         st.markdown("### 🏃‍♂️ Tips Gerak")
    #         st.info("Minimal 150 menit olahraga sedang per minggu (Jalan cepat, renang, sepeda).")
    #     with r2:
    #         st.markdown("### 🍲 Ide Menu Lokal")
    #         with st.expander("Pepes Tahu Kemangi"):
    #             st.write("Dikukus tanpa minyak. Tinggi protein nabati dan rendah lemak jenuh.")
    #         with st.expander("Cah Tauge Ikan Asin"):
    #             st.write("Tauge kaya serat dan Vitamin E. Gunakan sedikit minyak saat menumis.")

    # st.divider()
    # st.caption("© 2024 BMI Edukasi Ceria | Data Referensi: WHO & Kemenkes")