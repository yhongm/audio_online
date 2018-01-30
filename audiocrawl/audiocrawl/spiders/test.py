# from sqlalchemy import create_engine
# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import aliased
# from sqlalchemy import and_
# from sqlalchemy import or_
# from sqlalchemy.orm.exc import MultipleResultsFound
# from sqlalchemy.orm.exc import NoResultFound
# from sqlalchemy import text
# from sqlalchemy import func
# from sqlalchemy import ForeignKey
# # from audiocrawl.spiders \
# import crawl_audio_db
# from sqlalchemy.orm import relationship, backref
#
# # from audiocrawl.spiders.t_models import AudioClassifyDb
# # from t_models import AudioListDb
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#
#
# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", backref=backref('addresses', order_by=id))
#
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address
#
#
# def testsqlorm():
#     # pass
#     crawl_audio_db.init()
#     crawl_audio_db.addClassify(audio_classify_name="相声小品")
#     # crawl_audio_db.addClassify(audio_classify_name="second_menu")
#     # crawl_audio_db.addClassify(audio_classify_name="three_menu")
#     # name = crawl_audio_db.getClassifyIdByName("first_menu")
#     # print("name:" + str(name.id))
#     # audio_title = Column(String)
#     # audio_detail_title = Column(String, nullable=True)
#     # audio_detail_url = Column(String)
#     #
#     # classify_id = Column(Integer, ForeignKey('audio_classify.id'))
#     # audio_info_title = Column(String)
#     # audio_info_preimg = Column(String)
#     #
#     # audio_info_url = Column(String)
#     # audio_info_author = Column(String)
#     # audio_info_play_author = Column(String)
#     # audio_info_describe = Column(String)
#     # ad1 = AudioDb(audio_info_title="yhongm", audio_info_preimg="www.baidu.com", audio_info_url="www.baidu.com",
#     # ad1 = AudioDb( audio_info_title="yhongm")
#     # crawl_audio_db.addAudioListDb(ad1)
#     # ad2 = AudioListDb(audio_info_title="yhongm2", audio_info_preimg="www.baidu.com222",
#     #                   audio_info_url="www.baidu.com789",
#     #                   audio_classify_db_id=name.id)
#     # crawl_audio_db.addAudioListDb(ad2)
#     name = crawl_audio_db.getClassifyIdByName("相声小品")
#     print("name:"+str(name.id))
#     # print("name:"+name.audio_db[0].audio_detail_title)
#     # print("test id:" + str(list(name)[0].id) + ",test title :" + str(list(name)[0].audio_classify_name))
#     # crawl_audio_db.addAudioDetail(audio_title="aaa", audio_detail_title="aaa1",
#     #                               audio_detail_url="http://www.baidu.com/1", classify_id=str(list(name)[0].id))
#     #
#     # crawl_audio_db.getAudioDetail()
#     # init()
#     # print("version:" + sqlalchemy.__version__)
#     #
#     # ed_user = User(name='ed', fullname='Ed Jones')
#     # add(ed_user)
#     # ed_user1 = User(name='ed1', fullname='Ed Jones1')
#     # add(ed_user1)
#     # ed_user2 = User(name='edw2', fullname='Ewd Jones1')
#     # add(ed_user2)
#     # Session = connect()
#     # session = Session()
#     # for name, fullname in session.query(User.name, User.fullname):
#     #     # for instance in session.query(User).order_by(User.id):
#     #     print(name, fullname)
#     #
#     # for row in session.query(User, User.name).all():
#     #     print(
#     #         row.User.fullname, row.name)
#     #
#     # for row in session.query(User.fullname.label('name_label')).all():
#     #     print("name:" + row.name_label)
#     #
#     # user_alias = aliased(User, name='user_alias')
#     # for row in session.query(user_alias, user_alias.name).all():
#     #     print(
#     #         str(row.user_alias) + ",name:" + str(row.user_alias.name))
#     #
#     # for u in session.query(User).order_by(User.id)[1:3]:
#     #     print("id:" + str(u.id))
#     #
#     # query = session.query(User)
#     # query.filter(User.name == 'ed')  # equals
#     # query.filter(User.name != 'ed')  # not equals
#     # query.filter(User.name.like('%ed%'))  # LIKE
#     # query.filter(User.name.in_(['ed', 'wendy', 'jack']))  # IN
#     # query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))  # IN
#     #
#     # query.filter(~User.name.in_(['ed', 'wendy', 'jack']))  # not IN
#     # query.filter(User.name == None)
#     # # is None
#     # query.filter(User.name != None)  # not None
#     #
#     # query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
#     # query.filter(User.name == 'ed', User.fullname == 'Ed Jones')  # and
#     # query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')  # and
#     # query.filter(or_(User.name == 'ed', User.name == 'wendy'))  # or
#     # query.filter(User.name.match('wendy'))  # match
#     #
#     # query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
#     # query.all()
#     #
#     # first = query.first()
#     # print("first.name:" + first.name + ",first.fullname:" + first.fullname)
#     #
#     # # try:
#     # #     user = query.one()
#     # #     print("one:" + user.name)
#     # # except MultipleResultsFound:
#     # #     print("e:" + str(MultipleResultsFound))
#     #
#     # try:
#     #     user = query.filter(User.id == 99).one()
#     # except NoResultFound:
#     #     print("not :" + str(NoResultFound))
#     #
#     # for user in session.query(User).filter(text("id<3")).order_by(text("id")).all():
#     #     print("user:" + user.name)
#     # count = session.query(User).filter(User.name.like('%ed')).count()
#     # print("count:" + str(count))
#     # q1 = session.query(func.count(User.name), User.name).group_by(User.name).all()
#     # print("q1:" + str(q1))
#     # q2 = session.query(func.count('*')).select_from(User).scalar()
#     # print("q2:" + str(q2))
#     # q3 = session.query(func.count(User.id)).scalar()
#     # print("q3:" + str(q3))
#     #
#     # addresses = relationship("Address", order_by="Address.id", backref="user")
#     #
#     # jack = User(name='jackoow2111tt', fullname='Jack Bean')
#     # jack.addresses
#     # print("address:" + str(jack.addresses))
#     # jack.addresses = [Address(email_address='jack@google.com'), Address(email_address='j25@yahoo.com'), Address(email_address='j11125@yahoo.com')]
#     # add(jack)
#     #
#     # jack = session.query(User)
#     # ojack = jack.filter_by(name='jackoow2111tt').one()
#     # print("ojact.addresses:" + str(ojack.addresses))
#     #
#     # for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(
#     #         Address.email_address == 'jack@google.com').all():
#     #     print("u:" + u + ",a:" + a)
#
#
# def connect():
#     engine = getC()
#     Session = sessionmaker(bind=engine)
#     return Session
#
#
# def getC():
#     engine = create_engine('sqlite:///test001.sqlite', echo=True)
#     return engine
#
#
# def init():
#     engine = getC()
#     Base.metadata.create_all(engine)
#
#
# def add(user):
#     Session = connect()
#     session = Session()
#     try:
#
#         session.add(user)
#         session.commit()
#     finally:
#         session.close()
#
#
# if __name__ == "__main__":
#     testsqlorm()
