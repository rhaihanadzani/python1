import random


def start():
    posisiTikus = random.randint(1, 4)
    nama = input("Masukkan Nama Anda: ")

    while nama == "":
        print("Input yang Anda masukkan salah. Harap masukkan nama.")
        nama = input("Masukkan Nama Anda: ")    

    while True:
        print(f"Halo {nama}!\nSilahkan Pilih Nomor Tikus Yang Tersedia")

        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa]*4

        print(goa_kosong)
        print(posisiTikus)
        goa_tikus = goa_kosong.copy()
        goa_tikus[posisiTikus - 1] = "0_0"

        while True:
            try:
                input_user = int(input("Pilih Nomor Tikus 1-4:"))
                if input_user < 1 or input_user > 4:
                    raise ValueError
                break
            except ValueError:
                print("Input yang Anda masukkan salah. Harap masukkan nomor antara 1 dan 4.")

        confirm_answer = input(f"Apakah Anda yakin ingin memilih {input_user}? (y/n): ")
        if confirm_answer == "n":
            break
        elif confirm_answer == "y":
            if posisiTikus == input_user:
                print(f"==Selamat Anda Menang==\nPosisi tikus: {goa_tikus}")
            else:
                print(f"==Maaf Anda Kalah==\nPosisi tikus: {goa_tikus}")


            play_again = input("Apakah ingin melanjutkan? (y/n): ")
            if play_again == "n":
                break
            elif play_again == "y":
                posisiTikus = random.randint(1, 4)
                continue
            else:
                print("Input yang Anda masukkan salah. Harap masukkan y atau n.")
                break
        else:
            print("Silahkan ulangi program")
            break
    print("Program akan di berhentikan")

if __name__ == "__main__":
    start()
