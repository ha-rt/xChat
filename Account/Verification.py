from hashlib import md5

from initialization import database

def VerifyPassword(password, name):
    checkdocument = database.collection("users").document(name.lower())
    getdocument = checkdocument.get()

    if getdocument.exists:
        dictionary = getdocument.to_dict()
        if md5(password.encode('utf-8')).hexdigest() == dictionary["Password"]:
            return True
        else:
            return False
    else:
        print("ERROR: USER DOES NOT EXIST")
        return False

def checkExistance(name):
    checkdocument = database.collection("users").document(name.lower())
    getdocument = checkdocument.get()

    if getdocument.exists:
        return True

    return False