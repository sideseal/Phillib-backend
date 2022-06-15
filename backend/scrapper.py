#!/usr/bin/env python3

###################
#  python 3.7.10  #
###################

import datetime
from database import startup, shutdown
from models import Article
from controller import add_articles
from sites.aeon import aeon_rss


def main():
    target_sites = [aeon_rss("https://aeon.co/feed.rss"),]

    total_articles_count, status = add_articles(target_sites)

    if status:
        print(f"{datetime.date.today()}: *JOB DONE!* Articles found: {total_articles_count}")
    else:
        print(f"{datetime.datetime.now()}: *ERROR!*")

    return status

if __name__ == "__main__":
    startup()
    main()
    shutdown()
