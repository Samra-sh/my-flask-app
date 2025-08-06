from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    site_title = os.getenv("SITE_TITLE", "Default Site")
    return render_template("home.html", site_title=site_title)

@app.route('/about')
def about():
    site_title = os.getenv("SITE_TITLE", "Default Site")
    return render_template("about.html", site_title=site_title)

if __name__ == '__main__':
    app.run(debug=True)
