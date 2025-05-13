from flask import Flask, render_template, request, redirect
from scraper import fetch_events

app = Flask(__name__)

@app.route('/')
def index():
    events = fetch_events()
    return render_template('index.html', events=events)

@app.route('/get_tickets', methods=['POST'])
def get_tickets():
    email = request.form.get('email')
    url = request.form.get('url')
    print(f"User email: {email}")
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
