import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.sql
import sqlalchemy.ext.declarative
from create_db import Novel

Base = sqlalchemy.ext.declarative.declarative_base()
engine = sqlalchemy.create_engine('sqlite:///ncode.db', echo = True)
Session = sqlalchemy.orm.sessionmaker(bind = engine)
session = Session()

def add_db(ncode, nos, channel):
    try:
        novel = session.query(Novel).filter(Novel.ncode == ncode).one()
    except:
        print('new novel')
        novel = Novel(ncode=ncode, nos=nos, channels = str(channel))
        session.add(novel)
    else:
        if channel in novel.channel:
            print('already exists.')
        else:
            novel.channel += '/'+str(channel)
            print('reserved new novel.')
    finally:
        session.commit()
    return
