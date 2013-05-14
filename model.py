#!/usr/bin/env python
#-*-coding:utf-8-*-
from db import Connection
from logger import init_log
log = init_log()

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

    def get_user_by_condition(self):
        sql = "select nickname,gender,avatar from sina_user where friends_count < 30 and fans_count < 30"
        return self.query(sql)

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

class NewUser(Connection):

    def __init__(self, **db_setting):
        Connection.__init__(self, **db_setting)

    def add(self,nick_name,avatar_url,gender):
        try:
            sql = "insert into sina_user(nick_name,avatar_url,gender) values (%s,%s,%s);"
            self.execute(sql,nick_name,avatar_url,gender)
        except Exception as e:
            print '*'*100
            print e

class DPComment(Connection):

    def __init__(self, **db_setting):
        Connection.__init__(self,**db_setting)

    def add(self,dianping_id,nickname,avatar,content,star):
        try:
            sql = "insert into dp_comment(dianping_id,nick_name,avatar_url,content,star) values(%s,%s,%s,%s,%s)"
            self.execute(sql,dianping_id,nickname,avatar,content,star)
        except Exception as e:
            log.error(e)

class DPImage(Connection):

    def __init__(self, **db_setting):
        Connection.__init__(self,**db_setting)

    def add(self,dianping_id,image_url):
        try:
            sql = "insert into dp_image(dianping_id,image_url) values (%s,%s)"
            self.execute(sql,dianping_id,image_url)
        except Exception as e:
            log.error(e)


    
        