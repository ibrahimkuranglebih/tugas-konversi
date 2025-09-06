from utils import konversi_suhu

print("=== Konversi Suhu ===")

try :
    nilai = float(input("Masukkan nilai suhu : "))
    dari = input("Dari (C/F/K) : ")
    ke = input("Dari (C/F/K) : ")

    hasil = konversi_suhu(nilai, dari, ke)
    
    if isinstance(hasil, str):  # Jika error
        print(hasil)
    else:
        print(f"Hasil: {nilai}°{dari} = {hasil:.2f}°{ke}")

except :
    print("Error: Input nilai suhu harus berupa angka.")
