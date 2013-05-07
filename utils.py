#!/usr/bin/env python
#-*-coding:utf-8-*-

def covert_count(param):
    if str(param).isdigit():
        param = int(param)
    else:
        param = 0
    return param