import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'mini_market'
)

def insert_item(brg_code, brg_name, brg_price, brg_stock):
    cursor = db.cursor() #eksekusi penamaan
    # insert = cursor.execute(
    #     "INSERT INTO barang (brg_code, brg_name, brg_stock) VALUES(%s, %s, %s)", 
    #     (brg_code, brg_name, brg_stock))
    cursor.execute(
        "INSERT INTO barang (brg_code, brg_name, brg_price, brg_stock) VALUES(%s, %s, %s, %s)", 
        (brg_code, brg_name, brg_price, brg_stock))
    db.commit() #Ini untuk INSERT, UPDATE, DELETE
    
    if cursor.rowcount > 0:
        print("\nData berhasil disimpan")
    else:
        print("\nData gagal dimasukkan")
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM barang")
    return cursor.fetchall()