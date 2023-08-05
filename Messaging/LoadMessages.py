from Encryption import Decrypt

from initialization import database

def LoadMessages(server):
    collection = database.collection(server).order_by("Time").stream()
    documents = []

    for document in collection:
        dictionary = document.to_dict()
        documents.append(dictionary)

    # for document in documents:
    #     document["Message"] = Decrypt(document["Message"]).decode()
    #     document["User"] = Decrypt(document["User"]).decode()

    return documents