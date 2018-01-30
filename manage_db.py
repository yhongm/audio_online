from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


def connect(app):
    engine = create_engine(app.config['DATABASE'], echo=True)
    Session = sessionmaker(bind=engine)
    return engine, Session


def get(app, g):
    if not hasattr(g, 'manage_db_engine'):
        g.manage_db_engine, g.manage_db_session = connect(app)

        return g.manage_db_engine, g.manage_db_session


def init(app, g):
    engine, _ = get(app, g)
    Base.metadata.create_all(engine)


def addAccount(app, g, **kwargs):
    print("addAccount1")
    _, Session = get(app, g)

    print("addAccount2")
    session = Session()
    try:
        manage = ManageDb(**kwargs)
        session.add(manage)
        session.commit()
    except Exception:
        session.rollback()
        print("exception:" + str(Exception))
        raise Exception
    finally:
        session.close()


def getPwdByAccount(app, g, account):
    _, Session = get(app, g)
    session = Session()
    try:
        # mdb = ManageDb(mAccount=account)
        query = session.query(ManageDb)

    finally:
        session.close()
    return query.all()
