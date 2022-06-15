#!/usr/bin/env python3

##################
#   python 3.7   #
##################

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:////home/ec2-user/phillib/database/phillib.db')
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

session = Session()
Base = declarative_base()

def init_db():
    import models
    Base.metadata.create_all(engine)

def startup():
    engine.connect()

def shutdown():
    session.close_all()
    engine.dispose()
