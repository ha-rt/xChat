from os import system
from pyautogui import sleep

from Messaging import Message, LoadMessages
from Encryption import Decrypt
from Account import Account, checkExistance
from Server import Server

name,password,signin = None,None,None
def clear(): system('cls')

system("title xChat")

def messagingPlatform(userAccount, server):
    messages = LoadMessages(server.name)
    clear()
    for message in messages:
        message = message.to_dict()

        if Decrypt(message["User"]).decode() == "admin":
            print("\033[1;31;40m" + Decrypt(message["User"]).decode() + "\033[0;37;40m: " + Decrypt(message["Message"]).decode() + " | " + message["Time"])
        else:
            print(Decrypt(message["User"]).decode() + ": " + Decrypt(message["Message"]).decode() + " | " + message["Time"])
    msg = input("What is your message?: ")

    if msg == "--logout":
        return startLogin()

    if msg == "--updatepass":
        server.updatePassword(userAccount.name, input("What would you like the new password to be? (n = none, else = password): "))
        return messagingPlatform(userAccount, server)

    if msg == "--switchserv":
        return serverLogin(userAccount)

    message = Message(msg, userAccount.name, server.name)
    message.Send()

    return messagingPlatform(userAccount, server)

def serverLogin(userAccount):
    clear()

    server = input("Which server would you like to connect to?: ")
    if server == "--logout":
        return startLogin()
    if server == "users":
        print("This name has been restricted by the creator of xChat.")
    server = Server(server, name)

    passwordCheck = server.checkPass()

    if passwordCheck == False:
        print("The password you inputted for this server was incorrect, please try again or switch to a different server.")
        sleep(1)
        return serverLogin(userAccount)

    return messagingPlatform(userAccount, server)
def startLogin():
    global name,password,signin
    clear()

    name = input("Username: ")
    password = input("Password: ")

    userAccount = Account(name, password)
    token = None

    if checkExistance(name) == True:
        token = userAccount.signin()

    if checkExistance(name) == False:
        token = userAccount.signup()

    if token == None:
        print("ERROR: THE ACCOUNT LOGIN TOKEN WAS NIL AFTER SIGN PROCESSES")
        sleep(1)
        return startLogin()

    if token == False:
        print("An account was found with the username you inputted, but the password you inputted did not match the accounts password.")
        sleep(1)
        return startLogin()

    if token == True:
        serverLogin(userAccount)

startLogin()