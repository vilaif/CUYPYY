from libs import welcome_message, exit_program
from games import cuypy
from tools import warung

def menu():
    user_option = int(input(f'silahkan pilih menu programnya:\n1. Games CUYPY\n2. Warung Mini\n\nsilahkan pilih: '))
    
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start()
    else:
        print("Hanya boleh pilih yang tersedia!")
    
    return user_option

def main():
    welcome_message()
    menu()
    exit_program()
    
if __name__ == '__main__':
    main()






