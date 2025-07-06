import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyByxXmm2rcdybavdr_gLZQfNJxK4WVTTMY",
  'authDomain': "dps-project-nan-nam.firebaseapp.com",
  'databaseURL': "https://dps-project-nan-nam-default-rtdb.asia-southeast1.firebasedatabase.app/",  # ← Tambahkan ini
  'projectId': "dps-project-nan-nam",
  'storageBucket': "dps-project-nan-nam.appspot.com",  
  'messagingSenderId': "914150920458",
  'appId': "1:914150920458:web:6746a701d36dd94d26aaf3",
  'measurementId': "G-PKMX65KBFJ",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
