from flask import Flask,render_template, request, flash, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages


# Email configuration
EMAIL_ADDRESS = 'sumitsaggu2005@gmail.com'
EMAIL_PASSWORD = 'Sumit@123'  # Use App Password for Gmail


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        sender_email = request.form.get('email')
        message = request.form.get('message')

        # Compose email
        email_message = EmailMessage()
        email_message['Subject'] = f'Portfolio Contact from {name}'
        email_message['From'] = EMAIL_ADDRESS
        email_message['To'] = EMAIL_ADDRESS
        email_message.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(email_message)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash('Error sending message. Please try again later.', 'danger')
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
