from Account import Verification
from initialization import database

from hashlib import md5

from uuid import uuid4
from Account import VerifyPassword

class Account(object):
    def __init__(self, name: object, password: object) -> object:
        self.name = name
        self.password = password

    def signup(self):
        name = self.name
        password = self.password

        checkdocument = database.collection("users").document(name.lower())
        getdocument = checkdocument.get()

        if getdocument.exists:
            return "Exists"
        else:
            user_paylod = {
                "Name" : name,
                "Password" : md5(password.encode('utf-8')).hexdigest(),
                "UserID" :  str(uuid4()),
            }

            database.collection("users").document(user_paylod["Name"].lower()).set(user_paylod)

            return True

    def signin(self):
        name = self.name
        password = self.password

        checkdocument = database.collection("users").document(name.lower())
        getdocument = checkdocument.get()

        if getdocument.exists:
            return VerifyPassword(password, name)
        else:
            return "None"