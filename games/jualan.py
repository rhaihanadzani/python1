def start():
   while True:
       pilih_barang = int(input("Masukkan Pilihan 1 - 3: "))

       if pilih_barang == 1:
           print("Barang anda adalah baju")
  

       elif pilih_barang == 2:
           print("Barang anda adalah celana")
     

       elif pilih_barang == 3:
           print("Barang anda adalah celana")
   
       else:
           print("Input yang anda masukkan salah \n Program akan di berhentikan...")
           break

if __name__ == "__main__":
    start()