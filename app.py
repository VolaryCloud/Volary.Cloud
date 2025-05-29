from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            'name': 'VolaryDDNS',
            'description': 'A simple, secure, and easy-to-use dynamic DNS service.',
            'github': 'https://github.com/VolaryCloud',
            'website': 'https://ddns.volary.cloud',
        }
    ]

    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False)