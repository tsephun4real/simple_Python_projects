from cryptography.fernet import Fernet
import base64
import hashlib

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?: ")
key = load_key() + master_pwd.encode()  
fer = Fernet(key)

hashed_master_pwd=hashlib.sha256(master_pwd.encode()).digest()[:32]
fernet_key=base64.urlsafe_b64encode(hashed_master_pwd)
fer=Fernet(fernet_key)

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ",", "Password:", fer.decrypt(passw.encode()).decode())  # Corrected decode call

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")  # Corrected decode call

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add)? Press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
