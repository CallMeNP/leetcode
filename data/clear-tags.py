#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import json
tag_set=set()
clear_tags=[]
with open('tags.json','r') as f:
    tags=json.load(f)
    for i in tags:
        if i['pathname'] in tag_set:
            continue
        clear_tags.append(i)
        tag_set.add(i['pathname'])
print(clear_tags,len(clear_tags),len(tags))

print(json.JSONEncoder().encode(clear_tags))
