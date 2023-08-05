from initialization import database

def LoadMessages(server):
    return database.collection(server).order_by("Time").stream()