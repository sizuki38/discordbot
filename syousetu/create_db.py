# -*- coding:utf-8 -*-

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.sql
import sqlalchemy.ext.declarative


engine = sqlalchemy.create_engine('sqlite:///ncode.db', echo = True)
Base = sqlalchemy.ext.declarative.declarative_base()

#----------------------
class Novel(Base):
	__tablename__ = 'novels'
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
	ncode = sqlalchemy.Column(sqlalchemy.String,unique = True)
	nos = sqlalchemy.Column(sqlalchemy.Integer)
	channel = sqlalchemy.Column(sqlalchemy.String)

#----------------------
Session = sqlalchemy.orm.sessionmaker(bind = engine)
session = Session()

Base.metadata.create_all(engine)