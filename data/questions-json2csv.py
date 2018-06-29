#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import json

all = json.load(open(r"./all.json"))
translations = json.load(open(r"./translations.json"))
questions = dict()

for i in all['stat_status_pairs']:
    questions[i['stat']['frontend_question_id']] = {
        "id": i['stat']['frontend_question_id'],
        "title_en": i['stat']['question__title'],
        "slug_title": i['stat']['question__title_slug'],
        "difficulty_level": i['difficulty']['level']
    }

for i in translations['data']['translations']:
    questions[i['question']['questionId']]['title_zh']=i['title']

# print(i['stat']['frontend_question_id'], i['stat']['question__title'],
#      i['stat']['question__title_slug'], i['difficulty']['level'])

print(questions)
