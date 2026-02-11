from flask import Flask, request, render_template, redirect, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ==============================
# EMAIL CONFIGURATION
# ==============================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# ==============================
# DATABASE INIT
# ==============================

def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ==============================
# ROUTES
# ==============================

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Save to database
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
        conn.commit()
        conn.close()

        # Send email to YOU
        
        try:
             sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

    # Email to YOU
             admin_email = Mail(
                 from_email='your_verified_email@example.com',
                 to_emails='your_verified_email@example.com',
                 subject='New Contact Form Submission',
                 plain_text_content=f"""
                 Name: {name}
                 Email: {email}
                 Message: {message}
                 """
             )
             sg.send(admin_email)

             # Confirmation to USER
             user_email = Mail(
                 from_email='your_verified_email@example.com',
                 to_emails=email,
                 subject='Thanks for contacting Pranjal Sharma',
                 plain_text_content=f"""
                 Hi {name},
                  Thank you for reaching out! 🚀
                 I’ve received your message and will get back to you soon.

                 Best regards,
                 Pranjal Sharma
                 """
             )
             sg.send(user_email)
            
        except Exception as e:
            print("Email Sending Failed!!")
        
        flash("Message sent successfully!")
        return redirect("/contact")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
