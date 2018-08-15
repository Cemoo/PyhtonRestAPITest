from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route("/")
def hello():
    return "Cemal den size selamlar canlar"

if __name__ == '__main__':
    app.run(debug=True)


