from time import sleep
def welcome_message(title):
    style = "*" * (len(title) + 6)
    print(style)
    print(f"** {title} **")
    print(style)

def exit_program():
    sleep(1)
    print("1...")
    sleep(2)
    print("2...")
    sleep(2)
    print("3...")
    sleep(2)
    print("Program berhenti")
    exit()

if __name__ == "__main__":
    print(__name__)
    welcome_message()
    exit_program()