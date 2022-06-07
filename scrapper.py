#!/usr/bin/python3

##################
#   python 3.7   #
##################

from database import init_db, session
from models import Article

def show_tables():
    queries = session.query(Article)
    entries = [dict(
        id=q.id,
        name=q.name,
        title=q.title,
        link=q.link,
        published=q.published,
        tags=q.tags,
        rank=q.rank
        ) for q in queries]
    print(entries)

def delete_entry(id):
    session.query(Article).filter(Article.id==id).delete()
    session.commit()
    print("deleted")

def main():
    init_db()
    # do somethings
    session.close()

if __name__ == "__main__":
    main()
