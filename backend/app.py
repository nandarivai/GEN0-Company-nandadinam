from flask import Flask, render_template, request, redirect, url_for, flash
from backend.config.firebaseAuth import auth
import os

app = Flask(
    __name__,
    static_folder='../../frontend/assets',     # CSS, JS, IMG
    template_folder='../../frontend/views'     # HTML (register.html)
)

app.secret_key = 'projectDPSnandadinam'

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Email and Password cannot be empty", "danger")
            return redirect(url_for('register'))

        if len(password) < 8:
            flash("Password minimum 8 characters", "danger")
            return redirect(url_for('register'))

        try:
            auth.create_user_with_email_and_password(email, password)
            flash("Registration successful, please login.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            print("Firebase Error:", e)
            error_message = str(e)

            if "EMAIL_EXISTS" in error_message:
                flash("Email already used!", "danger")
            else:
                flash("Error: " + error_message, "danger")
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login')
def login():
    return "<h2>Login page (belum dibuat)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
