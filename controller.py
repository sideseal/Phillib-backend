#!/usr/bin/env python3

##################
#   python 3.7   #
##################

from database import init_db
from database import session
from models import Article


def add_entry(id, name, title, link, published, tags, rank):
    t = Article(id, name, title, link, published, tags, rank)
    session.add(t)
    session.commit()
    print("added")

def delete_entry(idx):
    session.query(Article).filter(Article.name==idx).delete()
    session.commit()
    print("deleted")

# session.close()

def check_article_exists(article_link):
    exists = session.query(Article.id).filter_by(link=article_link).scalar() is not None
    if not exists:
        return True
    else:
        return False

def add_articles(site):
    new_articles_count = 0

    for article in site:
        try:
            entry = Article.get_or_create(
                id=article["id"],
                name=article["name"],
                title=article["title"],
                link=article["link"],
                published=article["published"],
                tags=article["tags"],
                rank=article["rank"],
            )

            if entry not in session:
                session.add(entry)
                new_articles_count += 1

            session.commit()

        except Exception as e:
            print("\nController: Failed to commit article. See exception:\n", e)
            session.rollback()

    return new_articles_count
