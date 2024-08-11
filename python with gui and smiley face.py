import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Define function menu providing options to store, retrieve or quit.
def menu():
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("500x500")  # Make the window bigger

    # Create a canvas and draw a smiley face with "Welcome!" text
    canvas = tk.Canvas(root, width=500, height=300)
    canvas.pack()
    # Draw face
    canvas.create_oval(150, 50, 350, 250, fill="yellow", outline="black")
    # Draw eyes
    canvas.create_oval(200, 100, 230, 130, fill="white", outline="black")
    canvas.create_oval(270, 100, 300, 130, fill="white", outline="black")
    canvas.create_oval(210, 110, 220, 120, fill="black")
    canvas.create_oval(280, 110, 290, 120, fill="black")
    # Draw mouth
    canvas.create_arc(200, 150, 300, 200, start=0, extent=-180, fill="black", outline="black")
    # Add "Welcome!" text
    canvas.create_text(250, 30, text="Welcome!", font=("Arial", 24))

    def on_store():
        store_user(root)

    def on_retrieve():
        retrieve_user(root)

    def on_quit():
        messagebox.showinfo("Info", "Program terminated")
        root.quit()
        root.destroy()

    ttk.Button(root, text="Store User", command=on_store).pack(pady=10)
    ttk.Button(root, text="Retrieve User", command=on_retrieve).pack(pady=10)
    ttk.Button(root, text="Quit", command=on_quit).pack(pady=10)

    root.mainloop()

# Define function called encrypt_password to encrypt passwords
def encrypt_password(clearText, charSet):
    return "".join([charSet[(charSet.find(c) + 3) % len(charSet)] for c in clearText])

# Define function called decrypt_password to decrypt passwords
def decrypt_password(encText, charSet):
    return "".join([charSet[(charSet.find(c) - 3) % len(charSet)] for c in encText])

# Function to get password with '*' masking
def get_password(prompt="Enter the password: "):
    password = simpledialog.askstring("Input", prompt, show='*')
    return password

# Define function called store_user to store user credentials
def store_user(root):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    username = simpledialog.askstring("Input", "Enter your username:")
    website = simpledialog.askstring("Input", "Enter the website:")
    password = get_password()
    encrypted_username = encrypt_password(username, charSet)
    encrypted_website = encrypt_password(website, charSet)
    encrypted_password = encrypt_password(password, charSet)
    with open("credentials.txt", "a") as file:
        file.write(f"{encrypted_username}\n{encrypted_website}\n{encrypted_password}\n")
    messagebox.showinfo("Info", "Credentials stored successfully!")

# Define function to retrieve and display password of user
def retrieve_user(root):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    username = simpledialog.askstring("Input", "Enter the username associated with the credentials:")
    website = simpledialog.askstring("Input", "Enter the website:")
    encrypted_username = encrypt_password(username, charSet)
    encrypted_website = encrypt_password(website, charSet)
    try:
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                stored_username = lines[i].strip()
                stored_website = lines[i+1].strip()
                encrypted_password = lines[i+2].strip()
                if stored_username == encrypted_username and stored_website == encrypted_website:
                    decrypted_password = decrypt_password(encrypted_password, charSet)
                    messagebox.showinfo("Credentials", f"Username: {username}\nWebsite: {website}\nPassword: {decrypted_password}")
                    return
            messagebox.showerror("Error", "No matching credentials found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No credentials file found.")

if __name__ == "__main__":
    menu()
