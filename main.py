import os
from datetime import datetime

def main():
    print("=========================================")
    print("   DAILY MOOD & PRODUCTIVITY TRACKER    ")
    print("=========================================")
    
    hari_ini = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Tanggal: {hari_ini}\n")
    
    mood = input("Bagaimana mood kamu hari ini? (1-10): ")
    skor_produktif = input("Skor produktivitas kamu hari ini? (1-10): ")
    pencapaian = input("Apa hal baik yang kamu pelajari/lakukan hari ini?: ")
    evaluasi = input("Apa yang perlu diperbaiki untuk besok?: ")
    
    log_data = (
        f"Date: {hari_ini}\n"
        f"Mood Score: {mood}/10\n"
        f"Productivity Score: {skor_produktif}/10\n"
        f"Achievement: {pencapaian}\n"
        f"Reflection: {evaluasi}\n"
        f"{'-'*40}\n"
    )
    
    file_name = "daily_progress_log.txt"
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(log_data)
        print("\n[Sukses] Catatan kamu hari ini berhasil disimpan di 'daily_progress_log.txt'!")
        print("Tetap semangat dan konsisten ya! Kamu sudah melangkah lebih dekat ke impianmu. 🚀")
    except Exception as e:
        print(f"\nGagal menyimpan catatan: {e}")

if __name__ == "__main__":
    main()
