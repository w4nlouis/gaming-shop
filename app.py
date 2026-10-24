from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:@localhost/gaming_shop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
@app.route("/")
def home():
    return "Gaming shop system is alive"
@app.route("/dbtest")
def dbtest():
    db.session.execute(text("SELECT 1"))
    return "Database connected"
