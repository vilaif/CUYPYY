# 'random' adalah nama library
import random
from libs import welcome_message

# variable
while True:
    cuypy_position = random.randint(1, 4)

    welcome_message("SELAMAT DATANG DI CUYPY")

    nama_user = input("masukkan nama kamu: ")

    while nama_user == "":
        nama_user = input("isi dulu nama anda: ")

    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 # INI TETEP HARUS KOSONG

    goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
    goa[cuypy_position - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)
    # goa = goa_kosong


    print(f'''
    Halo {nama_user}! Coba perhatikan goa dibawah ini
    {goa_kosong}
    ''')

    # input output
    user_choose = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] : "))

    while user_choose == "":
        user_choose = int(input("Pilih dulu nomornya"))

    user_confirm = input(f"Apakah kamu yakin jawabannya adalah {user_choose}? [Y/N] ")

    # condition

    if user_confirm == "n":
        print("program dihentikan!")
        exit()
    elif user_confirm == "y":
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
    else:
        print("Ulangi Program")
        exit()
        
    play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break
    
print("Program Selesai!")

# if user_confirm in ["y", "Y"]:
#     if user_choose == cuypy_position:
#         print(f"Kamu benar {nama_user}! Posisi CUYPYY ada di goa nomor {cuypy_position}, pilihanmu adalah goa nomor {user_choose}")
#     else:
#         print(f"Kamu salah {nama_user}!! CUYPY bukan di goa {user_choose}, CUYPY ada di goa nomor {cuypy_position}")
# else:
#     print("Pilihan batal.")

# print(f"Pilihan kamu adalah {user_choose}" )

