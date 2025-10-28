import main
from services import db

def add():
    brg_code = input("Kode Barang: ")
    brg_name = input("Nama Barang: ")
    brg_price = int(input("Harga Barang: "))
    brg_stock = int(input("Stok Barang: "))
    
    db.insert_item(brg_code, brg_name, brg_price, brg_stock)
    
def check():
    items = db.fetch_item()
    for item in items:
        brg_code = item[1]
        brg_name = item[2]
        brg_price = item[3]
        brg_stock = item[4]
        
        print(f'''
Code {brg_code}
{brg_name} | Rp {brg_price}
Stok: {brg_stock}
''')

def start():
    while True:
        menu = int(input('Menu: \n\n1. Tambah Barang\n2. Check Barang\n3. Kembali \n\nSilahkan Pilih: '))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
            
if __name__ == '__main__':
    start()