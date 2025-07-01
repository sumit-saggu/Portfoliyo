# Portfoliyo

This is a personal portfolio website built with **Flask** and **Jinja2**.  
It includes Home, About, Projects, and Contact pages, with a working contact form that sends messages to your email.

---

## 🚀 How to Run

1. **Clone or Download this Repository**

2. **Install Requirements**
   ```bash
   pip install flask
   ```

3. **Project Structure**
   ```
   portfoliyo/
   ├── app.py
   ├── base.html
   ├── index.html
   ├── about.html
   ├── projects.html
   ├── contact.html
   ├── static/
   │   └── portfoliyo.JPG
   ```

4. **Configure Email Sending**
   - In `app.py`, set your Gmail and [App Password](https://support.google.com/accounts/answer/185833):
     ```python
     EMAIL_ADDRESS = 'your_email@gmail.com'
     EMAIL_PASSWORD = 'your_app_password'
     ```
   - If you use another provider, update the SMTP settings.

5. **Run the Flask App**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📝 Features

- **Home:** Introduction, profile image, social links.
- **About:** Skills, education, interests.
- **Projects:** List of projects with GitHub links.
- **Contact:** Social links, email, and a contact form that sends messages to your email.

---

## 🖼️ Images

- Place your profile image as `portfoliyo.JPG` inside the `static` folder.

---

## ⚠️ Notes

- **Do not open HTML files directly.** Always use the Flask server URL.
- For the contact form to work, you must configure your email and allow SMTP access.
- All navigation uses Jinja2 and Flask's `url_for`.

---

## 📄 License

This project is for personal and educational use.

---
```# Sumit Kumar Portfolio

This is a personal portfolio website built with **Flask** and **Jinja2**.  
It includes Home, About, Projects, and Contact pages, with a working contact form that sends messages to your email.

---

## 🚀 How to Run

1. **Clone or Download this Repository**

2. **Install Requirements**
   ```bash
   pip install flask
   ```

3. **Project Structure**
   ```
   portfoliyo/
   ├── app.py
   ├── base.html
   ├── index.html
   ├── about.html
   ├── projects.html
   ├── contact.html
   ├── static/
   │   └── portfoliyo.JPG
   ```

4. **Configure Email Sending**
   - In `app.py`, set your Gmail and [App Password](https://support.google.com/accounts/answer/185833):
     ```python
     EMAIL_ADDRESS = 'your_email@gmail.com'
     EMAIL_PASSWORD = 'your_app_password'
     ```
   - If you use another provider, update the SMTP settings.

5. **Run the Flask App**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📝 Features

- **Home:** Introduction, profile image, social links.
- **About:** Skills, education, interests.
- **Projects:** List of projects with GitHub links.
- **Contact:** Social links, email, and a contact form that sends messages to your email.

---

## 🖼️ Images

- Place your profile image as `portfoliyo.JPG` inside the `static` folder.

---

## ⚠️ Notes

- **Do not open HTML files directly.** Always use the Flask server URL.
- For the contact form to work, you must configure your email and allow SMTP access.
- All navigation uses Jinja2 and Flask's `url_for`.

---

## 📄 License

This project is for personal and educational
