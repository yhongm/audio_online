from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


def connect(app):
    engine = create_engine(app.config['DATABASE'], echo=True)
    Session = sessionmaker(bind=engine)
    return engine, Session


def get(app, g):
    if not hasattr(g, 'db_engine'):
        g.db_engine, g.db_session = connect(app)

        return g.db_engine, g.db_session


def init(app, g):
    engine, _ = get(app, g)
    Base.metadata.create_all(engine)


def getClassifyIdByName(app, g, name):
    print("getClassifyIdByName:" + name)
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioClassifyDb)

    finally:
        session.close()
    return query.filter(AudioClassifyDb.audio_classify_name == name).first()


def getAudioIdByTitle(audio_title):
    print("getAudioIdByTitle:" + audio_title)
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioListDb)

    finally:
        session.close()
    return query.filter(AudioListDb.audio_info_title == audio_title).first()


def addAudioListDb(ald):
    _, Session = get()
    session = Session()
    try:
        # audioDetail = AudioDetailDb(ad)
        session.add(ald)
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


# 添加音频数据
def addAudioDetail(app, g, **kwargs):
    _, Session = get(app, g)
    session = Session()
    try:
        ald = AudioListDb(**kwargs)
        session.add(ald)
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


# 获取所有音频数据
def getAllAudioList(app, g):
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioListDb).order_by(AudioListDb.id)
    finally:
        session.close()
    return query.filter(AudioListDb.id < 100).all()


def getAllAudio():
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioInfoDb).order_by(AudioInfoDb.id)

    finally:
        session.close()
    return query.all()


def getAudioListById(app, g, id):
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioDetaiListlDb).order_by(AudioDetaiListlDb.id)
    finally:
        session.close()

    return  list(reversed(query.filter(AudioDetaiListlDb.audio_list_db_id == id).all()))


def getAllAudioClassifys(app, g):
    _, Session = connect(app)
    session = Session()
    try:
        query = session.query(AudioClassifyDb).order_by(AudioClassifyDb.id)
    finally:
        session.close()
    return query.all()


def getAudioByClassifyId(app, g, classifyId):
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioListDb).order_by(AudioListDb.id)
    finally:
        session.close()
    return query.filter(AudioListDb.audio_classify_db_id == classifyId).all()


def deleteInvalidData(app, g):
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioDetaiListlDb)

        # query.filter_by((AudioDetaiListlDb.audio_detail_title[0:4] == "http"))
        dbs = query.all()
        print("dbs:" + str(len(dbs)))
        for db in dbs:
            if db.audio_detail_url != None:
                print("db:" + str(db.audio_detail_url[0:4]))
                if str(db.audio_detail_url[0:4]) != 'http':
                    print("delete db:" + str(db))
                    session.delete(db)
                    session.commit()

        # for db in dbs:
        #     session.delete(db)


    finally:
        session.close()


def getAudioDetailById(app, g, audio_id):
    _, Session = get(app, g)
    session = Session()
    try:
        query = session.query(AudioListDb).order_by(AudioListDb.audio_info_title)
    except Exception as e:
        print("getAudioDetailById,e:" + e)
    finally:
        session.close()
    return query.filter(AudioListDb.id == audio_id).first()
