#!/usr/bin/env python3

##################
#   python 3.7   #
##################

from sqlalchemy import Column, String, Integer
from database import Base, session

class Article(Base):
    __tablename__ = "Articles"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    published = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    rank = Column(Integer)
    
    def __init__(self, id, name, title, link, published, tags, rank):
        self.id = id
        self.name = name
        self.title = title
        self.link = link
        self.published = published
        self.tags = tags
        self.rank = rank

    def __repr__(self):
        return "<Article('%s','%s','%s','%s','%s','%s','%s')>" % (
            str(self.id),
            self.name,
            self.title,
            self.link,
            self.published,
            self.tags,
            self.rank,
        )

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

#    @classmethod
#    def get_or_create(cls, id, name, title, link, published, tags, rank):
#        exists = session.query(Article.id).filter_by(link=link).scalar() is not None
#        if exists:
#            return session.query(Article).filter_by(link=link).first()
#        return cls(
#            id=id,
#            name=name,
#            title=title,
#            link=link,
#            published=published,
#            tags=tags,
#            rank=rank,
#        )

class Comment(Base):
    __tablename__ = "Comments"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    create_at = Column(String, nullable=False)

    def __init__(self, article_id, user_id, comment, create_at):
        self.article_id = article_id
        self.user_id = user_id
        self.comment = comment
        self.create_at = create_at

    def __repr__(self):
        return "<Comment('%s','%s','%s','%s')>" % (
            str(self.article_id),
            str(self.user_id),
            self.comment,
            self.create_at,
        )
