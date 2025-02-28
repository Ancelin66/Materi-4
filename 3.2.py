try :
 nilai_akhir = float(input("Masukkan nilai akhir: "))
    if nilai_akhir > 70:
        print("Anda lulus dan mendapatkan sertifikat kelulusan!")
except ValueError:
    print("Input tidak valid! Mohon masukkan nilai yang benar.")
