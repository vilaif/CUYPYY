import random
import main 

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4 # INI TETEP HARUS KOSONG

        cuypy_position = random.randint(1, 4)

        goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
        goa[cuypy_position - 1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        
        print(f"Coba perhatikan goa dibawah ini \n\n{goa_kosong}")

        # input output
        user_choose = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] : "))

        while user_choose == "":
            user_choose = int(input("Pilih dulu nomornya"))

        if user_choose == cuypy_position:
            print(f'''Jawaban kamu benar!
            \n {goa}, 
            \n Cuypy berada di posisi : {cuypy_position} 
            \n Selamat Kamu Menang!''')
        else:
            print(f'''Jawaban Kamu Salah
            \n {goa},
            \n Cuypy berada di posisi : {cuypy_position} 
            \n Maaf kamu kalah''')
            
        play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]")
        if play_again == "n":
            main.menu()

if __name__ == '__main__':
    start()