#!/usr/bin/env python3

##################
#   python 3.7   #
##################

import secrets
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, date
from controller import check_article_exists
from functions.tagging import tagging


def get_content_text(link):
    text = ""

    try:
        request_link = urllib.request.Request(link)
        req = urllib.request.urlopen(request_link).read().decode('utf-8')
        content = re.findall(r'<p>(.*?)</p>',str(req))
        for line in content:
            text = text + str(line)
        return text
    except Exception as e:
        print("\nAeon: Failed to read content text. See exception:\n",e)

def get_published_date(time):
    dateFormatter = "%a, %d %b %Y %H:%M:%S"
    format_published = datetime.strptime(time, dateFormatter)
    published = format_published.strftime("%Y-%m-%d")
    return published

def create_secret_id():
    scrap_date = date.today().isoformat().replace("-","")
    rand_num = str(secrets.randbelow(2**12))
    secret_id = scrap_date + rand_num
    return int(secret_id)

def aeon_rss(url):
    article_list = []
    
    try:
        req = urllib.request.urlopen(url).read().decode('utf-8')
        root = ET.fromstring(req)

        for child in root.find('channel').findall('item'):
            id = create_secret_id()
            name = "Aeon"
            title = child[0].text.replace("\xa0", "")
            link = child[1].text
            published = get_published_date((child[4].text)[:-4])
            tags = tagging(get_content_text(link))
            rank = 0
            
            if check_article_exists:
                article = {
                    "id": id,
                    "name": name,
                    "title": title,
                    "link": link,
                    "published": published,
                    "tags": tags,
                    "rank": rank,
                }
                article_list.append(article)

        return article_list

    except Exception as e:
        print("\nAeon: Failed to scrap articles. See exceptions:\n", e)
