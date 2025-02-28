try :   
  pembelian = float(input("Masukkan jumlah pembelian: "))
  if pembelian >= 100000:
    print("Diskon dapat digunakan.")
  else:
    print("Diskon tidak dapat digunakan.")
except ValueError:
    print("Input tidak valid! Mohon masukkan angka yang benar.")
