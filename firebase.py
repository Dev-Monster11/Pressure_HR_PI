import firebase_admin
from firebase_admin import credentials, db, storage, firestore
import json
from PyQt5.QtCore import QObject

class FirebaseBackend(QObject):
    def __init__(self):
        super(FirebaseBackend, self).__init__()

        cred = credentials.Certificate("healcarepi-firebase-adminsdk-vs134-730b714463.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://healcarepi-default-rtdb.europe-west1.firebasedatabase.app/',
            'storageBucket': 'healcarepi.appspot.com'
        })
        self.store = firestore.client()
    def uploadFile(filename):
        pass

