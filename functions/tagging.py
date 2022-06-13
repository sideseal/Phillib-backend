#!/usr/bin/env python3

##################
#   python 3.7   #
##################

import re


Aesthetics = ["Aesthetics"]
Epistemology = [
    "Epistemology",
    "causality",
    "freewill",
    "determinism",
    "teleology",
    "anthropology",
]
Ethics = ["Ethics", "moral", "political"]
Logic = [
    "Logic",
    "deduction",
    "induction",
    "dialectic",
    "mathematical",
    "demonstration",
    "analogy",
]
Metaphysics = [
    "Metaphysics",
    "methodology",
    "ontology",
    "cosmology",
]
Eastern = ["Eastern", "chinese", "japan", "korean", "buddhist", "indian"]
Minds = ["Minds", "psychology", "physicalism", "machine", "consciousness", "mentality"]

CATEGORIES = [Aesthetics, Epistemology, Ethics, Logic, Metaphysics, Eastern, Minds]

def find_relevant_words(text):
    relevant = []

    for category in CATEGORIES:
        for keywords in category:
            # 본문의 단어 중, 카테고리의 단어와 일부만 일치해도 대상으로 포함한다.
            targets = re.findall(keywords[:5], text, re.IGNORECASE)
            if targets:
                relevant += targets
    if not relevant:
        relevant.append("others")

    return relevant

def set_tags(words):
    tags = []
    keyword_relevants = {}

    for word in words:
        word = word.lower()
        try:
            keyword_relevants[word] += 1
        except:
            keyword_relevants[word] = 1
    
    # 각 키워드 단어 카운트의 합의 평균을 구하고, 
    # 평균 미만 카운트를 가지는 키워드는 태깅에 포함하지 않는다.
    keyword_average = sum(keyword_relevants.values()) // len(keyword_relevants)

    for keys, values in keyword_relevants.items():
        if values > keyword_average:
            for category in CATEGORIES:
                for keywords in category:
                    if keys == keywords[:5]:
                        tags.append(category[0])
    if not tags:
        tags.append("others")

    return tags


def tagging(text):
    try:
        words = find_relevant_words(text)
        tags = set_tags(words)
        # 태그 중복 제거
        tmp = set(tags)
        sorted_tags = list(tmp)
        tag = ", ".join(sorted_tags)
        return tag
    except Exception as e:
        print("\nAeon: Tagging job failed. See exception:\n",e)
