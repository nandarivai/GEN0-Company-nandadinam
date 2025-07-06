import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from firebaseAuth import auth
from flask_cors import CORS

# Konfigurasi path frontend
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    static_folder=os.path.join(project_root, "frontend", "assets"),
    template_folder=os.path.join(project_root, "frontend", "views")
)

CORS(app)
app.secret_key = 'projectDPSnandadinam'


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        except Exception as e:
            error_message = str(e)
            print("Login Error:", error_message)

            if "EMAIL_NOT_FOUND" in error_message:
                flash("Email not registered. Please register first.", "warning")
                return redirect(url_for('register'))
            elif "INVALID_PASSWORD" in error_message:
                flash("Wrong password. Please try again.", "danger")
                return redirect(url_for('login'))
            else:
                flash("Login failed. Check email or password.", "danger")
                return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Email and Password cannot be empty", "danger")
            return redirect(url_for('register'))

        if len(password) < 8:
            flash("Password must be at least 8 characters", "danger")
            return redirect(url_for('register'))

        try:
            auth.create_user_with_email_and_password(email, password)
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            error_message = str(e)
            print("Registration Error:", error_message)

            if "EMAIL_EXISTS" in error_message:
                flash("Email already used. Try logging in.", "danger")
            else:
                flash("Registration error: " + error_message, "danger")

            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', email=session['user'])


@app.route('/about')
def about():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('about.html')


@app.route('/tutors')
def tutors():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('product.html')


@app.route('/subjects')
def subjects():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('service.html')


@app.route('/contact')
def contact():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
