import os

# Global variable to store passwords
passwords = []

# Function to read users from the file
def read_users():
    global passwords
    if not os.path.exists("users.txt"):
        open("users.txt", "w").close()  # Create the file if it does not exist
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, website, password = line.strip().split(",")
                passwords.append((username, website, decrypt(password)))
    except FileNotFoundError:
        pass

# Function to write users to the file
def write_user(username, website, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{website},{encrypt(password)}\n")

# Function to encrypt the password using ROT3
def encrypt(password):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    encrypted = "".join([charSet[(charSet.find(c) + 3) % 95] for c in password])
    return encrypted

# Function to decrypt the password using ROT3
def decrypt(password):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    decrypted = "".join([charSet[(charSet.find(c) - 3) % 95] for c in password])
    return decrypted

# Function to store password
def store_password():
    username = input("Enter username: ")
    website = input("Enter website: ")
    while True:
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            write_user(username, website, password)
            passwords.append((username, website, password))
            print("Password stored successfully!")
            break
        else:
            print("Passwords do not match. Please try again.")

# Function to retrieve password
def retrieve_password():
    username = input("Enter username: ")
    website = input("Enter website: ")
    for user in passwords:
        if user[0] == username and user[1] == website:
            print(f() )
            print(f"Password for {website} is retrieved successfully!")
            return
    print("No matching username and website found.")

# Main function with menu
def main():
    read_users()
    while True:
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            store_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
