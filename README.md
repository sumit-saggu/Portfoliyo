# Portfoliyo

A personal portfolio website built with **Flask** and **Jinja2**.  
It features Home, About, Projects, and Contact pages, with a modern responsive design.

---

## How to Starts

### 1. **Clone or Download the Repository**

### 2. **Install Requirements**
```bash
pip install flask
```

### 3. **Project Structure**
```
portfoliyo/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   └── contact.html
├── static/
│   └── portfoliyo.JPG
```

### 4. **Add Your Profile Image**
- Place your profile image as `portfoliyo.JPG` inside the `static` folder.

### 5. **Run the Flask App**
```bash
python app.py
```

### 6. **Open in Browser**
- Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

##  Features

- **Home:** Introduction, profile image, social links, and a contact button.
- **About:** Skills, education, and interests.
- **Projects:** List of projects with GitHub links and descriptions.
- **Contact:** Social links, email, and a contact form (add backend logic to send emails if needed).
- **Responsive Design:** Works well on desktop and mobile devices.
- **Navigation:** Uses Flask's `url_for` and Jinja2 templating for seamless navigation.
- **Flash Messages:** Displays feedback when the contact form is submitted.

---

##  Technologies Used

- **Python 3**
- **Flask**
- **Jinja2**
- **HTML5 & CSS3**
- **Font Awesome** (for icons)

---

##  Customization

- **Profile Image:** Replace `portfoliyo.JPG` in the `static` folder with your own image.
- **Social Links:** Update your LinkedIn and GitHub URLs in the templates.
- **Projects:** Edit `projects.html` to add or update your project details and links.
- **Contact Form:** To enable email sending, add logic in `app.py` using Flask-Mail or `smtplib`.

---

##  Notes

- **Do not open HTML files directly.** Always use the Flask server URL.
- For the contact form to send emails, you must add backend logic (see Flask-Mail or smtplib).
- All navigation uses Flask's `url_for` and Jinja2 templating.

---

##  License

This project is for personal and educational use.
