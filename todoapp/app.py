from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1234@localhost:5432/todoapp'

db  = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ =    'todos'
    id = db.Column(db.Integer , primary_key=True)
    description = db.Column(db.String() , nullable = False)

    def __repr__(self):
        return f'<ToDo {self.id} {self.descreption} >'

db.create_all()

@app.route("/")
def index():
    return render_template('index.html', data=Todo.query.all())