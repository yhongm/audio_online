from sqlalchemy import Integer, Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import json

Base = declarative_base()


# 分类表
class AudioClassifyDb(Base):
    __tablename__ = "audio_classify_db"
    id = Column(Integer, primary_key=True, autoincrement=True)
    audio_classify_name = Column(String)


# 音频列表表
class AudioListDb(Base):
    __tablename__ = "audio_list_db"
    id = Column(Integer, primary_key=True, autoincrement=True)
    audio_info_title = Column(String)
    audio_info_preimg = Column(String)

    audio_info_url = Column(String)
    audio_info_author = Column(String)
    audio_info_play_author = Column(String)
    audio_info_describe = Column(String)
    time = Column(Date)

    audio_classify_db_id = Column(Integer, ForeignKey('audio_classify_db.id'))
    audio_classify_db = relationship('AudioClassifyDb', backref=backref('audio_list_db', order_by=id))

    def __repr__(self):
        temp = "<AudioListDb(id='%s',audio_info_title='%s',audio_info_preimg='%s',audio_info_url='%s',audio_info_author='%s',audio_info_play_author='%s',audio_info_describe='%s')>" % (
            self.id, self.audio_info_title, self.audio_info_preimg, self.audio_info_url, self.audio_info_author,
            self.audio_info_play_author, self.audio_info_describe)
        return temp


# 音频详情列表
class AudioDetaiListlDb(Base):
    __tablename__ = "audio_datail_list_db"
    id = Column(Integer, primary_key=True, autoincrement=True)
    audio_title = Column(String)
    audio_detail_title = Column(String, nullable=True)
    audio_detail_url = Column(String)

    audio_list_db_id = Column(Integer, ForeignKey('audio_list_db.id'))
    audio_list_db = relationship('AudioListDb', backref=backref('audio_datail_list_db', order_by=id))
    time = Column(Date)

    def __repr__(self):
        # temp = '%s %s' % (self.audio_detail_title, self.classify_id)
        temp = "<AudioDetailDb(audio_title='%s',audio_detail_title='%s',audio_detail_url='%s')>" % (
            self.audio_title, self.audio_detail_title, self.audio_detail_url)
        return temp


class AudioDetaiListlDbDec(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AudioDetaiListlDb):
            print("return,title:" + obj.audio_title)
            return {
                'id': obj.id,
                'audio_title': obj.audio_title,
                'audio_detail_title': obj.audio_detail_title,
                'audio_detail_url': obj.audio_detail_url
            }
        return json.JSONEncoder.default(obj)
