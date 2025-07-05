import pyrebase
firebaseConfig = {
  'apiKey': "AIzaSyByxXmm2rcdybavdr_gLZQfNJxK4WVTTMY",
  'authDomain': "dps-project-nan-nam.firebaseapp.com",
  'projectId': "dps-project-nan-nam",
  'storageBucket': "dps-project-nan-nam.firebasestorage.app",
  'messagingSenderId': "914150920458",
  'appId': "1:914150920458:web:6746a701d36dd94d26aaf3",
  'measurementId': "G-PKMX65KBFJ"
};

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def signup():
    email=input("enter your email")
    password=input("enter your password")
    user=auth.create_user_with_email_and_password(email,password)
    print("Successfully Created Account")