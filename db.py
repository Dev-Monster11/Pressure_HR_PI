import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore
import json
from PyQt5.QtCore import QObject

class DataBackend(QObject):
    def __init__(self):
        super(DataBackend, self).__init__()

        cred = credentials.Certificate("healcarepi-firebase-adminsdk-vs134-730b714463.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://healcarepi-default-rtdb.europe-west1.firebasedatabase.app/',
            'storageBucket': 'healcarepi.appspot.com'
        })
        self.store = firestore.client()
    def uploadFile(filename):
        pass

