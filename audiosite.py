import requests
from flask import Flask, render_template, request, redirect, url_for, g
from flask_bootstrap import Bootstrap

from c_form import YForm, ManagerForm, AudioInfoForm, AudioDetailForm
import audio_db
import manage_db
from models import *
import os

import json


# from test import testA


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.update({'SECRET_KEY': 'secret',
                       'DATABASE': 'sqlite:///crawl.sqlite'
                       })
    app.config.from_envvar('FRESH_TOMATOES_SETTINGS', silent=True)
    return app


app = create_app()


@app.route('/')
def index():
    # db.init(app, g)
    manage_db.init(app, g)
    # mdb = ManageDb()

    # list = db.getAllValue(app, g)
    alds = audio_db.getAllAudioList(app, g)
    classifys = audio_db.getAllAudioClassifys(app, g)
    yform = YForm()
    return render_template("index.html", yform=yform, alds=alds, classifys=classifys)


@app.route('/githook', methods=['POST'])
def git_hook():
    # pwd = request.args["pwd"]
    # data = request.data
    # return render_template("test.html", rwd=pwd, data=data)
    # return render_template("error.html")
    d = request.get_data()
    print("d:" + str(d))
    states = os.system('sh /home/git_update.sh')
    print("states:" + str(states))
    return "success"


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/manager')
def manager():
    # managerAccList = manage_db.getPwdByAccount(app, g, "admin")

    yform = YForm()
    mform = ManagerForm()
    return render_template("manager_login.html", yform=yform, mform=mform)


@app.route('/audiomanager')
def audio_manager():
    yform = YForm()
    aiform = AudioInfoForm()
    adeform = AudioDetailForm()
    adlist = audio_db.getAllAudioList(app, g)  # audio detail list
    print("adlist:" + str(adlist[0]))
    return render_template("audio_manager.html", yform=yform, aiform=aiform, adeform=adeform, adlist=adlist)


@app.route('/add', methods=['POST'])
def add():
    yform = YForm(request.form)
    print("add,yc1:" + str(yform.yc.data))
    print("add,yc2:" + str(yform.yc2.data))
    manage_db.addAccount(app, g, mAccount=str(yform.yc.data), mPwd=str(yform.yc2.data))
    audio_db.addValue(app, g, value=yform.yc.data)

    return redirect(url_for('index'))


@app.route('/get_audio_classify', methods=['POST', 'GET'])
def get_audio_classify():
    print("get_audio_classify")
    # res = request.get_data(parse_form_data=False, as_text=True)
    # print("res:" + res)
    # id = json.loads(res)['id']
    # print("id:" + id)
    try:
        # id = request.args["id"]
        data = request.get_data()
        # print("get_audio_classify,data:" + data)
        # print("data:" + str(data))
        dict = json.loads(data)
        # uid = request.args["uid"]
        # print("id:" + id + ",uid:" + uid)
        id = dict['id']
        print("id:" + str(id))
    except Exception as e:
        print("get_audio_classify e:" + str(e))
    j = {"result": "success"}
    alds_by_claaifyid = audio_db.getAudioByClassifyId(app, g, id)
    print("length:" + str(len(alds_by_claaifyid)))
    return json.dumps(alds_by_claaifyid, cls=AudioListDbDec, ensure_ascii=False)


@app.route('/submit_audio_info', methods=['POST'])
def submit_audio_info():
    audioInfoForm = AudioInfoForm(request.form)
    print("sai,audio_title:" + audioInfoForm.audio_title.data)
    print(("sai audio_url:" + audioInfoForm.audio_url.data))
    audio_db.addAudioInfo(app, g, title=str(audioInfoForm.audio_title.data),
                          audio_url=str(audioInfoForm.audio_url.data))
    return redirect(url_for('index'))


@app.route('/submit_audio_detail', methods=['POST'])
def submit_audio_detail():
    audioDetailForm = AudioDetailForm(request.form)
    print("sad,audio_title:" + audioDetailForm.audio_detail_title.data)
    print("sad,audio,icon:" + audioDetailForm.audio_detail_icon_url.data)
    print("sad,audio,describe:" + audioDetailForm.audio_detail_describe.data)
    audio_db.addAudioDetail(app, g, audio_info_title=str(audioDetailForm.audio_title.data),
                            audio_info_preimg=str(audioDetailForm.audio_icon_url.data),
                            audio_info_describe=str(audioDetailForm.audio_describe.data))
    return redirect(url_for('index'))


@app.route('/mlogin', methods=['POST'])
def mlogin():
    mform = ManagerForm(request.form)
    account = mform.mAccount.data
    pwd = mform.mPwd.data
    print("m account:" + str(account))
    print("m pwd:" + str(pwd))
    mal = manage_db.getPwdByAccount(app, g, account)
    isRight = False
    for m in mal:
        if m.mPwd == pwd:
            isRight = True
            break

    if (isRight):
        return redirect(url_for('index'))
    else:
        return redirect(url_for('error'))


@app.route('/detail')
def detail():
    yform = YForm(request.form)
    print("detail:" + request.args['audio_id'])
    audio_id = request.args['audio_id']
    adls = audio_db.getAudioListById(app, g, audio_id)
    # ald = audio_db.getAudioDetailById(app, g, audio_id)
    return render_template("detail.html", yform=yform, adls=adls)


@app.route('/go_audio_play')
def audio_play():
    id = request.args['id']

    ads = audio_db.getAudioListById(app, g, id)
    ab = ads[0].audio_detail_title

    print("ds:" + str(ab))
    # print("ads:" + str(ads.__dict__))
    js = json.dumps(ads, cls=AudioDetaiListlDbDec, ensure_ascii=False)
    print("js:" + js)

    return render_template("audio_play.html", js=js, id=id)


# @app.route('/c_audio_detail')
# def c_audio_detail():
#     return render_template("")
@app.route('/getAudioListById/', methods=['GET', 'POST'])
def get_audio_list_by_id():
    if request.method == 'GET':
        id = request.args['id']

        print("d1:" + str(id))

        ads = audio_db.getAudioListById(app, g, id)
        ab = ads[0].audio_detail_title

        print("ds:" + str(ab))
        # print("ads:" + str(ads.__dict__))
        js = json.dumps(ads, cls=AudioDetaiListlDbDec, ensure_ascii=False)
        print("js:" + js)
        return js
        # tl=[]
        # testa = testA(1, 3)
        # ta = testa.__dict__
        # testb = testA(4, 5)
        # tb = testb.__dict__
        # tl.append(ta)
        # tl.append(tb)
        # jsont = json.dumps(tl)
        # return jsont
    else:
        d = request.get_data()
        # dict1 = json.loads(d)
        # print("d2:" +)

        return "<h3>不支持get</h3>"


def convertListToDict(ads):
    ds = []
    for ad in ads:
        d = ad.__dict__
        ds.append(d)
    return ds


@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s</h1>' % name


if __name__ == '__main__':
    app.run()
