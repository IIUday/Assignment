# 🦘 Sydney Event Scraper

A Flask web app that scrapes current events in Sydney from Eventbrite and displays them in a beautiful two-column layout. Users can enter their email and click "Get Tickets" to be redirected to the event's official page.

---

## ✨ Features

- Scrapes title, date, details for upcoming Sydney events
- Responsive design: 2-column layout on desktop
- Simple email form before redirecting to the ticket page
- Built using Flask, Selenium (with undetected-chromedriver), and Jinja2 templating


---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sydney-event-scraper.git
cd event_scraper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
event_scraper/
├── app.py
├── scraper.py
├── templates/
│   └── index.html
└── README.md
└── requirements.txt
```

---

## 🧠 Notes

- Ensure you have Chrome installed.
- `undetected-chromedriver` is used to bypass bot detection on Eventbrite.
- You must be connected to the internet during the first run.

---
