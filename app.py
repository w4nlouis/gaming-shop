from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:@localhost/gaming_shop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False, default="operator")
    active = db.Column(db.Boolean, default=True)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)
@app.route("/")
def home():
    return "Gaming shop system is alive"
@app.route("/dbtest")
def dbtest():
    db.session.execute(text("SELECT 1"))
    return "Database connected"
with app.app_context():
    db.create_all()