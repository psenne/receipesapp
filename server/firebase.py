import firebase_admin
from firebase_admin import credentials, firestore, auth

creds = credentials.Certificate("fbsecret.json")
app = firebase_admin.initialize_app(creds)

db = firestore.client()

users = auth.list_users()
print(users.users)