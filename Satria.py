# Sistem Manajemen Reservasi Hotel

# Data penyimpanan sementara
hotel_rooms = {101: "Available", 102: "Available", 103: "Available", 104: "Available"}
reservations = {}

# Fungsi untuk menampilkan kamar yang tersedia
def show_available_rooms():
    print("\nKamar yang tersedia:")
    for room, status in hotel_rooms.items():
        if status == "Available":
            print(f"Kamar {room}")

# Fungsi untuk melakukan reservasi
def make_reservation():
    name = input("\nMasukkan nama Anda: ")
    show_available_rooms()
    try:
        room_number = int(input("Masukkan nomor kamar yang ingin dipesan: "))
        if hotel_rooms.get(room_number) == "Available":
            hotel_rooms[room_number] = "Reserved"
            reservations[room_number] = name
            print(f"Kamar {room_number} berhasil dipesan oleh {name}.")
        else:
            print("Maaf, kamar tidak tersedia atau sudah dipesan.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor kamar dengan benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk membatalkan reservasi
def cancel_reservation():
    try:
        room_number = int(input("\nMasukkan nomor kamar yang ingin dibatalkan: "))
        if reservations.get(room_number):
            name = reservations.pop(room_number)
            hotel_rooms[room_number] = "Available"
            print(f"Reservasi kamar {room_number} atas nama {name} telah dibatalkan.")
        else:
            print("Tidak ada reservasi untuk kamar ini.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor kamar dengan benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk melihat daftar reservasi
def view_reservations():
    print("\nDaftar Reservasi:")
    if reservations:
        for room, name in reservations.items():
            print(f"Kamar {room}: {name}")
    else:
        print("Tidak ada reservasi saat ini.")

# Menu utama
def main_menu():
    while True:
        print("\nSistem Manajemen Reservasi Hotel")
        print("1. Tampilkan kamar yang tersedia")
        print("2. Pesan kamar")
        print("3. Batalkan reservasi")
        print("4. Lihat daftar reservasi")
        print("5. Keluar")
        
        try:
            choice = int(input("Pilih opsi (1-5): "))
            if choice == 1:
                show_available_rooms()
            elif choice == 2:
                make_reservation()
            elif choice == 3:
                cancel_reservation()
            elif choice == 4:
                view_reservations()
            elif choice == 5:
                print("Terima kasih telah menggunakan sistem manajemen reservasi hotel!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-5.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Menjalankan program
if __name__ == "__main__":
    main_menu()
