from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1234@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(), nullable=False)


def __repr__(self):
    return f"<Person ID:{self.id}, name:{self.name}>"

db.create_all()


@app.route('/')
def index():
    person = Person.query.one()
    return 'Hello world, ' + person.name + ' Radi' #  persons الى هو  Table مكتبتش اسم ال Person ملحوظه مهمه انا كتبت اسم الكلاس الي عمل الداتابيز الى هو