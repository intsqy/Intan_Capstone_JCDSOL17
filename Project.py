# Intan_Capstone_JCDSOL17

# Data Rumah Sakit "RS SAYANG BUNDA"
# Catatan Medis

# Create Data

pasien = []
appointments = []
dokter = [
    {"Nama": "Dr. Andi Suryanto", "Spesialisasi": "Jantung dan Paru", "Jadwal": "Senin - Kamis", "Pukul": "09:00 - 16:00"},
    {"Nama": "Dr. Budi Santoso", "Spesialisasi": "Umum", "Jadwal": "Jumat - Sabtu", "Pukul": "08:00 - 14:00"},
    {"Nama": "Dr. Cindy Permata", "Spesialisasi": "Gigi Umum", "Jadwal": "Senin & Kamis", "Pukul": "10:00 - 15:00"},
    {"Nama": "Dr. Dina Wulandari", "Spesialisasi": "Kulit dan Kelamin", "Jadwal": "Rabu - Minggu", "Pukul": "11:00 - 17:00"},
    {"Nama": "Dr. Edwin Kurniawan", "Spesialisasi": "Penyakit Dalam", "Jadwal": "Senin - Kamis", "Pukul": "09:00 - 16:00"},
    {"Nama": "Dr. Farida Sari", "Spesialisasi": "Ortopedi", "Jadwal": "Jumat - Sabtu", "Pukul": "08:00 - 13:00"},
    {"Nama": "Dr. Gunawan Prasetyo", "Spesialisasi": "Bedah Gigi", "Jadwal": "Senin & Kamis", "Pukul": "09:00 - 14:00"},
    {"Nama": "Dr. Hana Widodo", "Spesialisasi": "Umum", "Jadwal": "Selasa - Jumat", "Pukul": "08:00 - 15:00"},
    {"Nama": "Dr. Indah Rahma", "Spesialisasi": "Gigi Umum", "Jadwal": "Sabtu - Minggu", "Pukul": "09:00 - 12:00"},
    {"Nama": "Dr. Joko Hartono", "Spesialisasi": "Kulit dan Kelamin", "Jadwal": "Senin - Kamis", "Pukul": "11:00 - 16:00"},
    {"Nama": "Dr. Karina Wijaya", "Spesialisasi": "Jantung dan Paru", "Jadwal": "Jumat - Sabtu", "Pukul": "10:00 - 14:00"}
]

def add_pasien():
    print("\n MENAMBAH PASIEN  \n")
    nama = input("Masukkan nama pasien: ")
    umur = input("Masukkan umur pasien: ")
    keluhan = input("Masukkan keluhan pasien: ")
    pasien.append({"Nama": nama, "Umur" : umur, "Keluhan": keluhan})
    print("Data pasien berhasil diinput.")

# "pasien" = treat as integer
# "p" = treat as string

def record_pasien():
    print("\n CATATAN MEDIS PASIEN \n")
    if not pasien:
         print("Maaf, pasien tidak ditemukan.")
         return
    index = 1
    for p in pasien:
        print(f"{index}. Nama: {p['Nama']}, Umur: {p['Umur']}, Keluhan: {p['Keluhan']}")
        index += 1


def update_pasien():
    print("\n PERBAHARUI PASIEN \n")
    record_pasien()
    index = int(input("Masukkan nomor pasien yang ingin diperbaharui: ")) - 1
    if 0 <= index < len(pasien):
        print(f"Record pasien saaat ini: {pasien[index]}")
        nama = input("Masukkan nama yang baru (jika ingin diganti, lewati jika tidak ingin diganti): ")
        umur = input("Masukkan umur terbaru (lewati jika tidak ingin diganti): ")
        keluhan = input("Tambahkan keluhan terbaru (lewati jika tidak ada penambahan): ")
        if nama:
            pasien[index]["Nama"] = nama
        if umur:
            pasien[index]["Umur"] = umur
        if keluhan:
            pasien[index]["Keluhan"] = keluhan
        print(f"Rekaman medis pasien '{nama}' berhasil diperbaharui!")
    else:
        print("Maaf, nomor yang anda cari tidak ditemukan.")

def delete_pasien():
    print("\n HAPUS DATA PASIEN \n")
    record_pasien()
    index = (int(input("Masukkan nomor pasien untuk dihapus: ")) - 1)
    if 0 <= index < len(pasien):
        hapusData = pasien.pop(index)
        print(f"Pasien {hapusData['Nama']} berhasil dihapus")
    else:
        print("Maaf, tidak ada data pasien untuk dihapus.")

def data_dokter():
    print("\n DATA DOKTER \n")
    index = 1
    for doc in dokter:
        print(f"{index}. Nama: {doc['Nama']}, Spesialisasi: {doc['Spesialisasi']}, Jadwal: {doc['Jadwal']}, Pukul: {doc['Pukul']}")
        index += 1
          
def schedule_appointment():
    print("\n JADWALKAN JANJI \n")
    if not pasien:
        print("Belum ada data pasien. Silahkan daftarkan pasien terlebih dahulu")
        return
    
    print("\n Pilih Pasien: ")
    index = 1
    for p in pasien:
        print(f"{index}. Nama: {p['Nama']}, Keluhan: {p['Keluhan']}")
        index += 1
    
    index_pasien = int(input("Masukkan nomor pasien: "))

    print("\n Pilih dokter: ")
    data_dokter()
    index_dokter = int(input("Masukkan nomor dokter yang ingin dipilih: -")) - 1
    waktu = input("Masukkan waktu janji (contoh: '09:00'): ")

    if 0 <= index_pasien < len(pasien) and 0 <= index_dokter < len(dokter):
        appointments.append({
            "Pasien": pasien[index_pasien]["Nama"],
            "Dokter": dokter[index_dokter]["Nama"],
            "Waktu": waktu
        })
        print("Janji berhasil dijadwalkan.")
    else:
        print("Pilihan pasien atau dokter tidak ditemukan.")
     
def lihat_appointments():
    print("\n DAFTAR JANJI \n")
    if not appointments:
        print("Belum ada janji yang dijadwalkan. \n Silahkan kembali dan buat janji terlebih dahulu")
        return
    index = 1
    for a in appointments:
        print(f"{index}. Pasien: {a['Pasien'], Dokter: {a[Dokter]}, Waktu: {a['waktu']}}")
        index +=1

def delete_appointments():
    print("\n HAPUS JANJI \n")
    lihat_appointments()
    index = int(input("Masukkan nomor janji yang ingin dihapus: ")) - 1
    if 0 <= index < len(appointments):
        deleted = appointments.pop(index)
        print(f"janji untuk pasien {deleted['Pasien']} dengan dokter {deleted['Dokter']} berhasil dihapus.")
    else:
        print("Nomor tidak valid.")

def main_menu():   
    while True:
        print("Selamat datang di RS SAYANG BUNDA!")
        print("\n MENU UTAMA \n")
        print("1. Tambah Pasien")
        print("2. Tinjau Record Pasien")
        print("3. Perbaharui Data Pasien")
        print("4. Menghapus Data Pasien")
        print("5. Tampilkan Data Dokter")
        print("6. Jadwalkan Janji")
        print("7. Lihat Daftar Janji")
        print("8. Hapus Janji")
        print("9. Keluar")
        option = input("Tekan nomor sesuai kebutuhan Anda: ")
        if option == "1":
            add_pasien()
        elif option == "2":
            record_pasien()
        elif option == "3":
            update_pasien()
        elif option == "4":
            delete_pasien()
        elif option == "5":
            data_dokter()
        elif option == "6":
            schedule_appointment()
        elif option == "7":
            lihat_appointments()
        elif option == "8":
            delete_appointments()
        elif option == "9":
            print("Aplikasi akan ditutup.")
            break

if __name__== "__main__":
    print("Memulai program")
    main_menu()