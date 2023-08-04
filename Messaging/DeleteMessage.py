from initialization import database
class DeleteMessage(object):
    def __init__(self, messageid):
        checkdocument = database.collection("messages").document(messageid)
        getdocument = checkdocument.get()

        if getdocument.exists:
            checkdocument.delete()
        else:
            print("ERROR: MESSAGE DELETED DOES NOT EXIST")