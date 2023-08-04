from os import system

from Messaging import SendMessage, DeleteMessage
from Messaging import LoadMessages

from Encryption import Decrypt

from Account import Account

name,password,signin = None,None,None
def clear(): system('cls')

system("title xChat")

def messagingPlatform(userAccount):
    messages = LoadMessages()
    clear()
    for message in messages:
        if Decrypt(message["User"]).decode() == "admin":
            print("\033[1;31;40m" + Decrypt(message["User"]).decode() + "\033[0;37;40m: " + Decrypt(message["Message"]).decode() + " | " + message["Time"])
        else:
            print(Decrypt(message["User"]).decode() + ": " + Decrypt(message["Message"]).decode() + " | " + message["Time"])
    msg = input("What is your message?: ")

    if msg == "--logout":
        return startLogin()

    SendMessage(msg, userAccount.name)
    return messagingPlatform(userAccount)

def startLogin():
    global name,password,signin

    clear()

    name = input("Username: ")
    password = input("Password: ")
    signin = input("Already Have Account? (y/n): ")

    if signin != "y" and signin != "n":
        print("error")
        return startLogin()

    userAccount = Account(name, password)

    if signin == "y":
        token = userAccount.signin()

        if token == False:
            print("The password is incorrect")
            return startLogin()
        elif token == True:
            messagingPlatform(userAccount)
        else:
            print("An account with this name doesn't exist.")
    else:
        token = userAccount.signup()

        if token == "Exists":
            print("An account with this name already exists")
            return startLogin()

        messagingPlatform(userAccount)
startLogin()