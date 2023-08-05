from datetime import datetime,timezone
import uuid
from Encryption import Encrypt
from Messaging import DeleteMessage
from initialization import database

class Message(object):
    def __init__(self, message, user, server):
        self.message = message
        self.user = user
        self.server = server
        self.message_id = str(uuid.uuid4())

    def Send(self):
        server = self.server
        message_id = self.message_id
        message = self.message
        user = self.user

        message_payload = {
            "User": Encrypt(user),
            "Message": Encrypt(message),
            "MessageID": message_id,
            "Time": str(datetime.now(timezone.utc))
        }

        database.collection(server).document(message_payload["MessageID"]).set(message_payload)

    def Delete(self):
        print("WARNING: THE DELETE FUNCTION IS CURRENTLY NOT IN USAGE AND WILL NOT WORK")

        # message_id = self.message_id
        # server = self.server
        #
        # DeleteMessage(message_id, server)