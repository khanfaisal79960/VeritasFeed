# VeritasFeed

**Tagline:** *Your Daily Pulse of the World.*

[![Live Demo](https://img.shields.io/badge/View%20Live%20Project-%F0%9F%9A%80-blue?style=for-the-badge)](https://khanfaisal.netlify.app/veritasfeed)

---

## 📸 Project Screenshots

<img src="./assets/screenshot_1.png" alt="VeritasFeed Screenshot 1" width="800"/>
<img src="./assets/screenshot_2.png" alt="VeritasFeed Screenshot 2" width="800"/>

---

## 📰 Overview

**VeritasFeed** is a dynamic and live news web application built with **Flask**, designed to provide users with the latest headlines and articles from around the globe. It features a modern, dark theme, category-based browsing, and robust search functionality.

---

## ✨ Features

- **Live News Updates:** Real-time news headlines and articles fetched using NewsAPI.
- **Category Browsing:** View news across categories like Business, Entertainment, Health, Science, Sports, and Technology.
- **Search Functionality:** Find specific articles easily with keyword-based search.
- **Modern UI:** Clean dark-themed interface built with Bootstrap 5 and custom CSS.
- **Responsive Design:** Fully responsive for desktops, tablets, and mobile devices.
- **Fixed Footer:** Always-visible footer with developer and copyright info.

---

## 🛠️ Technologies Used

**Backend:**
- Python 3.13.2
- Flask (Web Framework)
- Requests (HTTP Library)

**Frontend:**
- HTML5
- CSS3 (Custom styling + animations)
- JavaScript
- Bootstrap 5
- Font Awesome (Icons)

**API:**
- [NewsAPI.org](https://newsapi.org)

---

## 🔑 API Setup: NewsAPI.org

VeritasFeed uses [NewsAPI.org](https://newsapi.org) to retrieve data. To use it:

1. Visit [https://newsapi.org](https://newsapi.org) and sign up.
2. Get your free API key from your dashboard.

### Set as Environment Variable

**Windows (Temporary):**

```bash
set NEWS_API_KEY=YOUR_NEWS_API_KEY_HERE
```

**PowerShell:**

```powershell
$env:NEWS_API_KEY="YOUR_NEWS_API_KEY_HERE"
```

**macOS/Linux (Temporary):**

```bash
export NEWS_API_KEY="YOUR_NEWS_API_KEY_HERE"
```

For permanent setup, add the export line to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`.

---

## 📁 Project Structure

```
veritasfeed/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── category.html
│   ├── search.html
│   └── error.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        ├── placeholder_news.jpg
        ├── placeholder_tech.jpg
        └── placeholder_sports.jpg
```

---

## 🚀 Setup and Run Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd veritasfeed
```

### 2. Create `requirements.txt`
```text
Flask==3.0.3
requests==2.31.0
```

### 3. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 4. Activate the Environment

**Windows:**
```bash
.env\Scriptsctivate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Add Placeholder Images

Place these files inside `static/images/`:

- `placeholder_news.jpg`
- `placeholder_tech.jpg`
- `placeholder_sports.jpg`

### 7. Run the Flask App
```bash
flask run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 👤 Developer

**Khan Faisal**

- 🔗 [Portfolio](https://khanfaisal.netlify.app)
- 🐙 [GitHub](https://github.com/khanfaisal79960)
- 💼 [LinkedIn](https://www.linkedin.com/in/khanfaisal79960)
- ✍️ [Medium](https://medium.com/@khanfaisal79960)
- 📸 [Instagram](https://instagram.com/mr._perfect_1004)
