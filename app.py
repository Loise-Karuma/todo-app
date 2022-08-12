from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = false

@app.route('/')
def index():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
