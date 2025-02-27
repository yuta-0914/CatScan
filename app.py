from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy
from flaskext.markdown import Markdown
#from flask_login import UserMixin, LoginManager
#import os

# パイソンで”$ sudo pip3 install Flask-Markdown”を入力してマークダウンを有効にする
app = Flask(__name__)
Markdown(app)

#ログインサインイン機能
#app.config['SECRET_KEY'] = os.urandom(24)
#db = SQLAlchemy(app)

#login_manager = LoginManager()
#login_manager.init_app(app)

# ここでデータベースのURLを指定
#　db_uri = "mysql+pymysql://root:@charest=utf8"
#　app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#　db = SQLAlchemy(app) 

# ここでclassを定義
# class　POST(db.Model)
#        __tablename__=""
#        =db.Column(db.Integer, primary_key=True, autoincrement=True)
#        =db.Column(db.Integer)
#        =db.Column(db.Text())

# トップページのルート
@app.route('/')
def index():
    message = "Hello CatScan!!"
    return render_template('index.html', massage = message )

# 判別結果のルート
@app.route("/result")
def result():
    message = "This Cat!!"
    return render_template("result.html", massage = message )

#　自分のプロフィールのルート
@app.route("/profile")
def profile():
    message = "Your Profile!!"
    return render_template("profile.html", message = message )

#　猫図鑑のルート
@app.route("/book")
def book():
    message = "Cats Book!!"
    return render_template("book.html", message = message )

#　サインインとログイン画面のルートについては後々作成
#class User(UserMixin, db.Model):
   # id = db.Column(db.Integer,primary_key=True)
   # username = db.Column(db.String(30), unique = True)
   # password = db.Column(db.String(12))

