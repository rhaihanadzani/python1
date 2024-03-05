from games import tikus,jualan
from libs import welcome_message,exit_program

def menu():
    user_menu = int(input("Silahkan pilih game yang ingin anda mainkan : \n 1.jualan \n 2. tikus \n 3. exit \n"))
    while True:
        if user_menu < 1 or user_menu > 3:
            print("!!! input yang anda masukkan salah !!!")
            user_menu=int(input("Silahkan pilih game yang ingin anda mainkan : \n 1.jualan \n 2. tikus \n 3. exit \n"))
         
        else:
            if user_menu == 1:
                welcome_message("Tebak Tebak Jualan")
                jualan.start()
                exit_program()
      
            elif user_menu == 2:
                welcome_message("Tebak Tebak Tikus")
                tikus.start()
                exit_program()
          
            elif user_menu == 3:
                print("Program akan di berhentikan...")
                exit_program()



def main():
    menu()
 
if __name__ == "__main__":
    main()