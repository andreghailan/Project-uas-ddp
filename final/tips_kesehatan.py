import streamlit as st


def tips_kesehatan():
    st.image(
        "images/tips.jpg",
        use_container_width=True,
        caption="Tips dan Saran Kesehatan"
    )

    st.title("Tips dan Saran untuk Anda")
    st.write(
        "Jika IMT (BMI) Anda menunjukkan bahwa Anda berada dalam rentang kelebihan "
        "berat badan atau obesitas, mungkin saatnya untuk melakukan perubahan agar "
        "Anda dapat memiliki berat badan yang lebih sehat. "
        "Klik pada item di bawah ini untuk melihat apa yang dapat Anda lakukan."
    )

    tips = [
        (
            "🥗 Nutrisi",
            """
        Tidak ada diet yang sempurna untuk menurunkan berat badan. Namun, ada cara makan
        yang telah terbukti secara ilmiah dapat membantu Anda mengelola berat badan.

        Contoh diet:
        1. Diet Mediterania
        2. Diet tinggi serat
        3. Diet vegetarian
        """,
            True
        ),
        (
            "🧩 Kesehatan Mental",
            """
        Berat badan sering kali berkaitan dengan kondisi emosional.
        Emotional eating dan stres dapat meningkatkan risiko obesitas.

        Belajar mengelola stres adalah bagian penting dari manajemen berat badan.
            """,
            False
        ),
        (
            "🏃 Olahraga",
            """
        Olahraga rutin sangat penting untuk menurunkan dan mengelola berat badan.
        Kombinasikan latihan aerobik dan resistensi, serta tingkatkan aktivitas harian Anda.
            """,
            False
        ),
        (
            "🛏️ Kualitas Tidur",
            """
        Kurang tidur memengaruhi hormon dan pola makan.

        Tips tidur sehat:
        1. Buat rutinitas tidur
        2. Relaks sebelum tidur
        3. Ciptakan kamar yang nyaman
            """,
            False
        ),
        (
            "❌ Obesitas dan Risiko Kesehatan",
            """
        IMT adalah langkah awal, namun tidak cukup menggambarkan seluruh risiko kesehatan.

        Risiko obesitas:
        1. Diabetes tipe II
        2. Penyakit kardiovaskular
        3. Stroke
        4. Hipertensi
        5. Infertilitas
            """,
            False
        ),
    ]

    col_risk_layout, _ = st.columns([2, 0.1])

    with col_risk_layout:
        for judul, isi, buka in tips:
            with st.expander(judul, expanded=buka):
                st.write(isi)
