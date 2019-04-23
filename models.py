# -*- coding: utf-8 -*-
# Time    : 2019/4/22 21:58
# Author  : LiaoKong

from datetime import datetime
from ext import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
