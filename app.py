from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/weather')
def home_page():
    x = "temp"

    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)