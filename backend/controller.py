#!/usr/bin/env python3

##################
#   python 3.7   #
##################

from database import init_db
from database import session
from models import Article


def delete_entry(idx):
    session.query(Article).filter(Article.name==idx).delete()
    session.commit()
    print("deleted")

def check_article_exists(article_link):
    exists = session.query(Article.id).filter_by(link=article_link).scalar() is not None
    if not exists:
        return True
    else:
        return False

# 모델의 classmethod도 컨트롤러에 포함을 시켜야 할까?
def add_articles(site):
    new_articles_count = 0
    status = False

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

            status = True
            session.commit()

        except Exception as e:
            status = False
            session.rollback()

            print("\nController: Failed to commit article. See exception:\n", e)
            return new_articles_count, status

    return new_articles_count, status

def get_all_articles():
    results = (
        session.query(
            Article.id,
            Article.name,
            Article.title,
            Article.link,
            Article.published,
            Article.tags,
            Article.rank,
        )
        .order_by(Article.published.desc())
        .order_by(Article.name)
        .all()
    )
    session.close()
    return results