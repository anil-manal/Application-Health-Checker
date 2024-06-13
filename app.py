from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def check_application_health(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            status = 'up'
        else:
            status = 'down'
        return {'status': status, 'status_code': status_code}
    except requests.exceptions.RequestException as e:
        return {'status': 'down', 'error': str(e)}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        report = check_application_health(url)
        return render_template('index.html', report=report, url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
