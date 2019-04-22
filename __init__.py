# -*- coding: utf-8 -*-
# Time    : 2019/4/22 21:44
# Author  : LiaoKong

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from . import commands, views, errors
