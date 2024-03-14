import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="warung_py"
)

def insert_item(kode_barang,nama_barang,harga_barang,stok_barang):
    cursor =db.cursor()
    cursor.execute("INSERT INTO inventory (kode_barang,nama_barang,harga_barang,stok_barang) VALUES (%s,%s,%s,%s) ",(kode_barang,nama_barang,harga_barang,stok_barang))
    db.commit()
    if cursor.rowcount > 0 :
        return print("data tersimpan")
    else :
        return print("data gagal tersimpan")

def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()
        
    
    
    

    