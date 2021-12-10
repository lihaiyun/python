from flask import Flask, render_template
from user_controller import user_controller

app = Flask(__name__)
app.register_blueprint(user_controller)
app.secret_key = 'MyFlaskWebAppKey'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


if __name__ == '__main__':
    app.run(port=5001)
