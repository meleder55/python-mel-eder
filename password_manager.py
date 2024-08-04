import os
#  operating system

# declare Global variable charSet - taken from assignment 
charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "


# define function called rot3_encrypt to encrypt passwords
def rot3_encrypt(clearText):
    return "".join([charSet[(charSet.find(c) + 3) % 95] for c in clearText])


# define function called rot3_decrypt to decrypt passwords
def rot3_decrypt(encText):
    return "".join([charSet[(charSet.find(c) - 3) % 95] for c in encText])


# define function called store_credentials to store user credentials
def store_credentials():
    username = input("Enter your username: ")
    website = input("Enter the website: ")
    password = input("Enter the password: ")
    encrypted_password = rot3_encrypt(password)
    with open("credentials.txt", "a") as file:
        file.write(f"{username}\n{website}\n{encrypted_password}\n")
    print("Credentials stored successfully!")


# define function to retrieve and display password of user
def retrieve_and_display_password():
    username = input("Enter the username associated with the credentials: ")
    website = input("Enter the website: ")
    if os.path.exists("credentials.txt"):
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                stored_username = lines[i].strip()
                stored_website = lines[i+1].strip()
                encrypted_password = lines[i+2].strip()
                if stored_username == username and stored_website == website:
                    decrypted_password = rot3_decrypt(encrypted_password)
                    print(f"Username: {stored_username}\nWebsite: {stored_website}\nPassword: {decrypted_password}")
                    return
            print("No matching credentials found.")
    else:
        print("No credentials file found.")


# Define function menu providing options to store, retrieve or quit.  
def menu():
    while True:
        print("\nMenu:")
        print("1. Add credentials")
        print("2. Retrieve and display password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            store_credentials()
        elif choice == '2':
            retrieve_and_display_password()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
