import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from models import Post, db
from flask_migrate import Migrate

from views.posts import posts_app
import config


app = Flask(__name__)
app.register_blueprint(posts_app)

app.config.from_object(config.DevelopmentConfig)


csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app=app, db=db)





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
