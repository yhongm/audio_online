from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from audiocrawl.spiders.t_models import *

# from t_models import AudioDetaiListlDb
from audiocrawl.spiders.t_models import *


def connect():
    engine = create_engine('sqlite:///crawl.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    return engine, Session


def get():
    return connect()


def init():
    engine, _ = get()
    Base.metadata.create_all(engine)


# def addAudioInfo(**kwargs):
#     _, Session = get()
#     session = Session()
#     try:
#         audioinfo = AudioInfoDb(**kwargs)
#         session.add(audioinfo)
#         session.commit()
#     except Exception:
#         session.rollback()
#         print("exception:" + str(Exception))
#         raise Exception
#     finally:
#         session.close()


def addClassify(**kwargs):
    _, Session = get()
    session = Session()
    try:
        classify = AudioClassifyDb(**kwargs)
        session.add(classify)
        session.commit()
    except Exception:
        session.rollback()
        raise Exception
    finally:
        session.close()


def getClassifyIdByName(name):
    print("getClassifyIdByName:" + name)
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioClassifyDb)

    finally:
        session.close()
    return query.filter(AudioClassifyDb.audio_classify_name == name).first()


def have_classify_count(name):
    print("getClassifyIdByName:" + name)
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioClassifyDb)

    finally:
        session.close()
    return query.filter(AudioClassifyDb.audio_classify_name == name).count()


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
    except Exception as e:
        print("addAudioList,e :" + e)
        session.rollback()
        raise Exception
    finally:
        session.close()


def addAudioDetail(**kwargs):
    _, Session = get()
    session = Session()
    try:
        audioDetail = AudioDetaiListlDb(**kwargs)
        session.add(audioDetail)
        session.commit()
    except Exception as e:
        print("addAudioDetail,e:" + e)
        session.rollback()
        raise Exception
    finally:
        session.close()


def getAllAudio():
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioInfoDb).order_by(AudioInfoDb.id)

    finally:
        session.close()
    return query.all()


def getAllAudioList():
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioListDb).order_by(AudioListDb.id)
    finally:
        session.close()
    return query.all()


def getAudioDetail():
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioDetailDb).join(AudioClassify, isouter=True)
        print("query:" + query)
    finally:
        session.close()
    return query.all()


def getAudioListById(id):
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioDetaiListlDb).order_by(AudioDetaiListlDb.id)

    finally:
        session.close()
        sql = query.filter(AudioDetaiListlDb.audio_list_db_id == id)
        print("sql:" + str(sql))
    return sql.all()


def getAudioListById(id):
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioDetaiListlDb).order_by(AudioDetaiListlDb.id)

    finally:
        session.close()
        sql = query.filter(AudioDetaiListlDb.audio_list_db_id == id)
        print("sql:" + str(sql))
    return sql.all()


def have_audio_deitail_item_count(audio_title, audio_detail_title):
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioDetaiListlDb).order_by(AudioDetaiListlDb.id)

    finally:
        session.close()
        sql = query.filter(and_(
            AudioDetaiListlDb.audio_title == audio_title, AudioDetaiListlDb.audio_detail_title == audio_detail_title))
        print("sql:" + str(sql))
    return sql.count()


def have_audio_count(audio_info_title):
    _, Session = get()
    session = Session()
    try:
        query = session.query(AudioListDb).order_by(AudioListDb.id)
    finally:
        session.close()
    return query.filter(AudioListDb.audio_info_title == audio_info_title).count()
