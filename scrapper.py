#!/usr/bin/env python3

##################
#   python 3.7   #
##################

from database import session
from controller import add_articles
from sites.aeon import aeon_rss
from models import Article

def main():
    target_sites = [aeon_rss("https://aeon.co/feed.rss"),]
    total_articles_count = 0

    for site in target_sites:
        counts = add_articles(site)
        total_articles_count += counts

    print("\n\n**JOB DONE!**")
    print(total_articles_count)

    session.close()
    
    return

if __name__ == "__main__":
    main()
