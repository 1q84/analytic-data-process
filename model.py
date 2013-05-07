#!/usr/bin/env python
#-*-coding:utf-8-*-
from db import Connection

class User(Connection):

    def __init__(self, **db_setting):
        Connection.__init__(self, **db_setting)


    def add(self,nickname,gender,desc,friends_count,fans_count,weibo_count,avatar):
        try:
            sql = """insert into sina_user(nickname,gender,description,friends_count,fans_count,weibo_count,avatar)
                     values (%s,%s,%s,%s,%s,%s,%s);
                  """
            self.execute(sql,nickname,gender,desc,friends_count,fans_count,weibo_count,avatar)
        except Exception as e:
            print e

class Comment(Connection):

    def __init__(self, **db_setting):
        Connection.__init__(self, **db_setting)


    def add(self,comment_id,shop_id,author,author_id,star,taste,environment,service,content,author_photo,photo_1,photo_2,photo_3,photo_4,photo_5):
        try:
            sql = """insert into dp_comment(comment_id,shop_id,author,author_id,star,taste,environment,service,content,author_photo,photo_1,photo_2,photo_3,photo_4,photo_5)
                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                  """
            self.execute(sql,comment_id,shop_id,author,author_id,star,taste,environment,service,content,author_photo,photo_1,photo_2,photo_3,photo_4,photo_5)
        except Exception as e:
            print e

    

    
        