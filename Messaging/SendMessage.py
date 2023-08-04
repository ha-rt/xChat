from datetime import datetime
from datetime import timezone
import uuid
from Encryption import Encrypt

from initialization import database
class SendMessage(object):
    def __init__(self, message, user):
        self.message = message
        self.user = user

        message_payload = {
            "User" : self.user,
            "Message" : self.user,
            "MessageID" : 0,
            "Time" : 0
        }

        message_payload["Message"] = Encrypt(self.message)
        message_payload["Time"] = str(datetime.now(timezone.utc))
        message_payload["MessageID"] = str(uuid.uuid4())
        message_payload["User"] = Encrypt(self.user)

        database.collection("messages").document(message_payload["MessageID"]).set(message_payload)

        self.payload = message_payload

    def returnPaylod(self):
        return self.payload