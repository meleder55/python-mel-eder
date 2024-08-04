# declare Global variable charSet - taken from assignment 
charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
choice = 'q'

# define function called encrypt_password to encrypt passwords
def encrypt_password(clearText):
    return "".join([charSet[(charSet.find(c) + 3) % 95] for c in clearText])

# define function called decrypt_password to decrypt passwords
def decrypt_password(encText):
    return "".join([charSet[(charSet.find(c) - 3) % 95] for c in encText])

# define function called store_user to store user credentials
def store_user():
    username = input("Enter your username: ")
    website = input("Enter the website: ")
    password = input("Enter the password: ")
    encrypted_password = encrypt_password(password)
    with open("credentials.txt", "a") as file:
        file.write(f"{username}\n{website}\n{encrypted_password}\n")
    print("Credentials stored successfully!")

# define function to retrieve and display password of user
def retrieve_user():
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
                    decrypted_password = decrypt_password(encrypted_password)
                    print(f"\n{'-'*40}\n| {'Username':<15} | {stored_username:<20} |\n{'-'*40}\n| {'Website':<15} | {stored_website:<20} |\n{'-'*40}\n| {'Password':<15} | {decrypted_password:<20} |\n{'-'*40}")
                    return
            print("No matching credentials found.")
    except FileNotFoundError:
        print("No credentials file found.")

# Define function menu providing options to store, retrieve or quit.  
def menu():
    while True:
        print("\nMenu:")
        print("1. Store user")
        print("2. Retrieve user")
        print("q. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            store_user()
        elif choice == '2':
            retrieve_user()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

        
