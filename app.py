from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report = None
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            report = {
                'status': 'UP' if response.status_code == 200 else 'DOWN',
                'status_code': response.status_code,
                'error': None
            }
        except Exception as e:
            report = {
                'status': 'DOWN',
                'status_code': None,
                'error': str(e)
            }
    return render_template('index.html', report=report)

if __name__ != '__main__':
    # This is necessary for Vercel to find the app
    from app import app as application

if __name__ == '__main__':
    app.run(debug=True)
