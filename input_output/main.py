# 'random' adalah nama library
import random

welcome_message = "CUYPYYY!!!!"
cuypy_position = random.randint(1, 4)


print("************************")
print(f"***** {welcome_message} *****")
print("************************")

nama_user = input("masukkan nama kamu: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
|_|  |_|  |_|  |_|
''')

user_choose = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] : "))

user_confirm = input("Apakah kamu yakin dengan pilihanmu? [Y/N] ")

if user_confirm in ["y", "Y"]:
    if user_choose == cuypy_position:
        print(f"Kamu benar {nama_user}! Posisi CUYPYY ada di goa nomor {cuypy_position}, pilihanmu adalah goa nomor {user_choose}")
    else:
        print(f"Kamu salah {nama_user}!! CUYPY bukan di goa {user_choose}, CUYPY ada di goa nomor {cuypy_position}")
else:
    print("Pilihan batal.")

# print(f"Pilihan kamu adalah {user_choose}" )

