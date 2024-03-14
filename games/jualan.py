from services import db
import os
def add():
    kode_barang = input("Masukkan Kode Barang : ")
    nama_barang = input("Masukkan Nama Barang : ")
    harga_barang = int(input("Masukkan Harga Barang : "))
    stok_barang = int(input("Masukkan Stok Barang : "))
    
    db.insert_item(kode_barang,nama_barang,harga_barang,stok_barang)

def check():
    items = db.fetch_item()
    for item in items:
        kode_barang =item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
kode barang : {kode_barang}
nama barang : {nama_barang} | Rp.{harga_barang}
stok barang : {stok_barang}
              ''')  

             
def start():
    
   while True:
       pilih_barang = int(input("Masukkan Pilihan 1 - 3:\n\n 1. Tambah Barang \n 2. Cek Barang \n 3. Exit \n"))
       os.system("clear")

       if pilih_barang == 1:
          add()
  

       elif pilih_barang == 2:
           check()
     

       elif pilih_barang == 3:
           print("Program akan di berhentikan...")
           break
   
       else:
           print("Input yang anda masukkan salah \n Program akan di berhentikan...")
           break

if __name__ == "__main__":
    start()