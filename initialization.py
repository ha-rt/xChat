from firebase_admin import credentials, firestore, initialize_app
from credentials import FirebaseCredentials

firebaseCredentials = credentials.Certificate(FirebaseCredentials)
initialize_app(firebaseCredentials)

database = firestore.client()
