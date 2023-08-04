from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import initialize_app

from credentials import FirebaseCredentials

firebaseCredentials = credentials.Certificate(FirebaseCredentials)
initialize_app(firebaseCredentials)

database = firestore.client()
