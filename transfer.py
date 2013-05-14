#!/usr/bin/env python
#-*-coding:utf-8-*-

from model import User,Comment,NewUser
from config import db_setting,online_db_setting
user = User(**db_setting)
comment = Comment(**db_setting)
online_user = NewUser(**online_db_setting)

res = user.get_user_by_condition()

for item in res:
    nick_name = item.get('nickname')
    avatar = item.get('avatar')
    gender = item.get('gender')
    online_user.add(nick_name,avatar,gender)
