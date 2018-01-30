from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired


class YForm(FlaskForm):
    yc = StringField('field1', validators=[DataRequired()])
    yc2 = StringField('field2', validators=[DataRequired])
    submit = SubmitField('submit')


class ManagerForm(FlaskForm):
    mAccount = StringField('account', validators=[DataRequired])
    mPwd = StringField('password', validators=[DataRequired])
    submit = SubmitField('submit')


class AudioInfoForm(FlaskForm):
    audio_info_title = StringField('audio_info_title', validators=[DataRequired])
    audio_info_url = StringField('audio_info_url', validators=[DataRequired])
    submit = SubmitField('submit')


class AudioDetailForm(FlaskForm):
    audio_detail_title = StringField('audio_detail_title', validators=[DataRequired])
    audio_detail_icon_url = StringField('audio_detail_icon_url', validators=[DataRequired])
    audio_detail_describe = StringField('audio_detail_describe', validators=[DataRequired])
    submit = SubmitField('submit')
