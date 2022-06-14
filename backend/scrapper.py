#!/usr/bin/env python3

##################
#   python 3.7   #
##################

import datetime
from database import session
from models import Article
from controller import add_articles
from sites.aeon import aeon_rss

def main():
    target_sites = [aeon_rss("https://aeon.co/feed.rss"),]
    total_articles_count = 0
    total_status = False

    for site in target_sites:
        counts, status = add_articles(site)
        if not status:
            break
        total_articles_count += counts

    total_status = status
    if total_status:
        print(f"{datetime.datetime.now()}: *JOB DONE!* Articles found: {total_articles_count}")
    else:
        print(f"{datetime.datetime.now()}: *ERROR!*")

    session.close(); return

if __name__ == "__main__":
    main()
