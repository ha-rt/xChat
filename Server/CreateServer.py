from initialization import database
from hashlib import md5

class Server(object):
    def __init__(self, name, username):
        self.name = name
        checkdocument = database.collection(name).document("owner")
        getdocument = checkdocument.get()

        if getdocument.exists:
            pass
        else:
            payload = {
                "Owner": username
            }

            database.collection(name).document("owner").set(payload)

            passw = input("Would you like to set a password for your server? (n = no, else = password): ")

            if passw != "n":
                payload = {
                    "Password": md5(passw.encode('utf-8')).hexdigest()
                }

                database.collection(name).document("password").set(payload)

    def checkPass(self):
        name = self.name

        checkdocument = database.collection(name).document("password")
        getdocument = checkdocument.get()

        if getdocument.exists:
            dictionary = getdocument.to_dict()

            print(f"{name} is a locked server")

            password = input(f"What is the password to {name}?: ")
            password = md5(password.encode('utf-8')).hexdigest()

            if password == dictionary["Password"]:
                return True
            else:
                return False
        else:
            return True

    def updatePassword(self, username, password):
        name = self.name

        checkdocument = database.collection(name).document("owner")
        getdocument = checkdocument.get()

        if getdocument.exists:
            dictionary = getdocument.to_dict()

            if dictionary["Owner"] == username.lower():
                if password == "n":
                    checkdocument = database.collection(name).document("password")

                    checkdocument.delete()
                    return

                payload = {
                    "Password": md5(password.encode('utf-8')).hexdigest()
                }

                database.collection(name).document("password").set(payload)
                return True
            else:
                print("You do not have permission to run this command.")
                return False
