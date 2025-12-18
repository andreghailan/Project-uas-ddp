import pandas as pd
from datetime import datetime
import os

class ImtBmi:
    def __init__(self):
        self.riwayat_file = "riwayat_imt_bmi.csv"
        self.riwayat = self._load_data()

    def _load_data(self):
        """Load data jika file ada, kalau tidak buat DataFrame kosong."""
        if os.path.exists(self.riwayat_file):
            return pd.read_csv(self.riwayat_file)
        else:
            return pd.DataFrame(columns=[
                "Tanggal", "Berat (kg)", "Tinggi (cm)", "Umur", "IMT (BMI)", "Klasifikasi"
            ])

    def _save_data(self):
        """Simpan DataFrame ke file CSV."""
        self.riwayat.to_csv(self.riwayat_file, index=False)

    def simpan_riwayat(self, berat, tinggi, umur, imt_ideal, klasifikasi):
        """Simpan satu riwayat baru ke CSV."""
        if berat == None or tinggi == None:
            return False
        new_entry = pd.DataFrame([{
            "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Berat (kg)": berat,
            "Tinggi (cm)": tinggi,
            "Umur": umur,
            "IMT (BMI)": imt_ideal,
            "Klasifikasi": klasifikasi
        }])

        self.riwayat = pd.concat([self.riwayat, new_entry], ignore_index=True)
        self._save_data()

        return True
    