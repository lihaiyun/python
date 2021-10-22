from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


if __name__ == '__main__':
    app.run()
