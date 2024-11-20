# Intan_Capstone_JCDSOL17

# Data Rumah Sakit "RS SAYANG BUNDA"
# Catatan Medis, Riwayat Dokter, dan Appointment

pasien = []
staf = []
janjian = []

# Create Data
def add_pasien():
    print("\n MENAMBAH PASIEN  \n")
    nama = input("Masukkan nama pasien: ")
    umur = input("Masukkan umur pasien: ")
    diagnosa = input("Masukkan diagnosa pasien: ")
    pasien.append({"Nama": nama, "Umur" : umur, "Diagnosa": diagnosa})
    print("Data pasien berhasil diinput.")

# "pasien" = treat as integer
# "pacien" = treat as string

def record_pasien():
    print("\n CATATAN MEDIS PASIEN \n")
    if not pasien:
         print("Maaf, pasien tidak ditemukan.")
         return
    index = 1
    for pacien in pasien:
        print(f"{index}. Nama: {pacien['Nama']}, Umur: {pacien['Umur']}, Diagnosa: {pacien['Diagnosa']}")
        index += 1


def update_pasien():
    print("\n PERBAHARUI PASIEN \n")
    record_pasien()
    index = int(input("Masukkan nomor pasien yang ingin diperbaharui: ")) - 1
    if 0 <= index < len(pasien):
        print(f"Record pasien saaat ini: {pasien[index]}")
        nama = input("Masukkan nama yang baru (jika ingin diganti, lewati jika tidak ingin diganti): ")
        umur = input("Masukkan umur terbaru (lewati jika tidak ingin diganti): ")
        diagnosa = input("Tambahkan diagnosa terbaru (lewati jika tidak ada penambahan): ")
        if nama:
            pasien[index]["Nama"] = nama
        if umur:
            pasien[index]["Umur"] = umur
        if diagnosa:
            pasien[index]["Diagnosa"] = diagnosa
        print(f"Rekaman medis pasien '{nama}' berhasil diperbaharui!")
    else:
        print("Maaf, nomor yang anda cari tidak ditemukan.")

def delete_pasien():
    print("\n HAPUS DATA PASIEN \n")
    record_pasien()
    index = int(input("Masukkan nomor pasien untuk dihapus: ")) - 1
    if 0 <= index < len(pasien):
        hapusData = pasien.pop(index)
        print(f"Pasien {hapusData['Nama']} berhasil dihapus")
    else:
        print("Maaf, tidak ada data pasien untuk dihapus.")
        return
    
def main_menu():
    while True:
        print("\n MENU UTAMA \n")
        print("1. Tambah Pasien")
        print("2. Tinjau Record Pasien")
        print("3. Perbaharui Data Pasien")
        print("4. Menghapus Data Pasien")
        print("5. Keluar")
        option = input("Selamat datang! Tekan nomor sesuai kebutuhan Anda: ")
        
        if option == "1":
            add_pasien()
        elif option == "2":
            record_pasien()
        elif option == "3":
            update_pasien()
        elif option == "4":
            delete_pasien()
        elif option == "5":
            print("Aplikasi akan ditutup.")
            break

    if __name__== "__main__":
        main_menu()