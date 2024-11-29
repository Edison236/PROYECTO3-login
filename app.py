from flask import Flask, render_template
from dotenv import load_dotenv
from databases.db  import db, init_db
from models import user
from controllers.controller_login import login_bp
from flask_login import LoginManager, login_user, login_required
import os

load_dotenv()
app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

secret_key = os.urandom(24)
app.config["SECRET_KEY"] = secret_key

login_manager = LoginManager(app)

@login_manager.user_loader
def user_loader(user_id):
    usert = user.User.query.get(int(user_id))
    print(usert)
    return usert



db.init_app(app)
init_db(app)

app.register_blueprint(login_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)