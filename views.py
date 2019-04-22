# -*- coding: utf-8 -*-
# Time    : 2019/4/22 21:46
# Author  : LiaoKong

from flask import flash, redirect, url_for, render_template

from . import app, db
from models import Message
from forms import HelloForm


@app.route("/", methods=["GET", "POST"])
def index():
    # 获取所有留言
    messages = Message.query.order_by(Message.timestamp.desc()).all()

    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data

        # 实例化模型，创建一条新数据
        message = Message(body=body, name=name)

        db.session.add(message)
        db.session.commit()

        flash("Your message have been sent to the world!")
        return redirect(url_for("index"))

    return render_template("index.html", form=form, messages=messages)
