#Password Manager program by Melissa Eder 8027788   09/08/2024 

#import getpass to mask user password details
import getpass

# Declare global variable for quit option
choice = 'q'

# ANSI escape sequences for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Define function menu providing options to store, retrieve or quit.  
def menu():
    global choice
    border = "-" * 30
    print(border)
    print(f"{BLUE}|{' ' * 8}Password Manager{' ' * 8}|{RESET}")
    print(border)
    while True:
        print("\nMenu:")
        print(f"{GREEN}1. Store user{RESET}")
        print(f"{GREEN}2. Retrieve user{RESET}")
        print(f"{RED}q. Quit{RESET}")
        print("-" * 30)
        choice = input("Enter your choice: ")
        print("-" * 30)
        if choice == '1':
            store_user()
        elif choice == '2':
            retrieve_user()
        elif choice == 'q':
            print("program terminated")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

# Define function called encrypt_password to encrypt passwords
def encrypt_password(clearText, charSet):
    return "".join([charSet[(charSet.find(c) + 3) % len(charSet)] for c in clearText])

# Define function called decrypt_password to decrypt passwords
def decrypt_password(encText, charSet):
    return "".join([charSet[(charSet.find(c) - 3) % len(charSet)] for c in encText])

# Function to get password with '*' masking
def get_password(prompt="Enter the password: "):
    password = getpass.getpass(prompt)
    masked_password = '*' * len(password)
    print(masked_password)
    return password

# Define function called store_user to store user credentials
def store_user():
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    username = input("Enter your username: ")
    website = input("Enter the website: ")
    password = get_password()
    encrypted_password = encrypt_password(password, charSet)
    with open("credentials.txt", "a") as file:
        file.write(f"{username}\n{website}\n{encrypted_password}\n")
    print(f"{GREEN}Credentials stored successfully!{RESET}")

# Define function to retrieve and display password of user
def retrieve_user():
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    username = input("Enter the username associated with the credentials: ")
    website = input("Enter the website: ")
    try:
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                stored_username = lines[i].strip()
                stored_website = lines[i+1].strip()
                encrypted_password = lines[i+2].strip()
                if stored_username == username and stored_website == website:
                    decrypted_password = decrypt_password(encrypted_password, charSet)
                    border = "|"
                    print(f"\n{border}{'Username' : ^20}{border}{'Website' : ^20}{border}{'Password' : ^20}{border}")
                    print("-" * 65)
                    print(f"{border}{YELLOW}{stored_username : ^20}{RESET}{border}{YELLOW}{stored_website : ^20}{RESET}{border}{YELLOW}{decrypted_password : ^20}{RESET}{border}")
                    print("-" * 65)
                    return
            print(f"{RED}No matching credentials found.{RESET}")
    except FileNotFoundError:
        print(f"{RED}No credentials file found.{RESET}")

if __name__ == "__main__":
    menu()
