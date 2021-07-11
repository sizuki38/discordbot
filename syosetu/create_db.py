# -*- coding:utf-8 -*-
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import true

engine = sqlalchemy.create_engine('sqlite:///ncode.db', echo = True)
Base = declarative_base()
session = sessionmaker(bind=engine)

#----------------------
class Novel(Base):
	__tablename__ = 'novels'
	id = Column(Integer, primary_key = True, autoincrement=True)
	ncode = Column(String,unique = True)
	nos = Column(Integer)

class Middle(Base):
	__tablename__ = 'novelschannels'
	id = Column(Integer, primary_key=True, autoincrement=True)
	novel_id = Column(Integer)
	channel_id = Column(Integer)

class Channel(Base):
	__tablename__ = 'channels'
	id = Column(Integer, primary_key=True, autoincrement=True)
	channel_id = Column(Integer)

Base.metadata.create_all(bind = engine)

#----------------------
def CreateChannel(channel_id):
	channel=Channel()
	if channel.channel_id in channel_id:
		return
	channel.channel_id=channel_id
	session.add(instance=channel)
	session.commit()
def CreateNovel(ncode, nos):
	novel=Novel()
	novel.ncode=ncode
	novel.nos=nos
	session.add(instance=novel)
	session.commit()
def CreateMiddle(novel_id, channel_id):
	novelchannel = Middle()
	novelchannel.novel_id=novel_id
	novelchannel.channel_id=channel_id
	session.add(instance=novelchannel)
	session.commit()

def ReadNovel():#all
	return session.query(Novel).all()
def ReadNovelID(id):#serch id
	return session.query(Novel).filter(Novel.id==id).one()
def ReadNovel(ncode):#serch ncode
	return session.query(Novel).filter(Novel.ncode==ncode).one()

def ReadChannel():#all
	return session.query(Channel).all()
def ReadChannelID(id):#serch id
	return session.query(Channel).filter(Channel.id==id).one()
def ReadChannel(channel_id):#serch channel id
	return session.query(Channel).filter(Channel.channel_id==channel_id).one()

def ReadMiddleNovel(novel_id):
	return session.query(Middle).filter(Middle.novel_id==novel_id).all()
def ReadMiddleChannel(channel_id):
	return session.query(Middle).filter(Middle.channel_id==channel_id).all()
def ReadMiddle(novel_id, channel_id):
	return session.query(Middle).filter((Middle.novel_id==novel_id)&(Middle.channel_id==channel_id)).one()

def UpdateNovel(novel, nos):
	novel.nos = nos
	session.commit()

def DeleteChannel(channel_id):
	channel = ReadChannel(channel_id)
	middles = ReadMiddleChannel(channel.id)
	session.delete(channel)
	session.delete(middles)
	session.commit()
def DeleteChannel(ncode, channel_id):
	novel = ReadNovel(ncode)
	channel = ReadChannel(channel_id)
	middle = ReadMiddle(novel.id, channel.id)
	session.delete(middle)
	session.commit()