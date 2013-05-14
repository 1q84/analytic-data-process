#!/usr/bin/env python
#-*-coding:utf-8-*-

import csv
from model import User,Comment,DPComment,DPImage
from config import db_setting,online_db_setting
from utils import covert_count
from logger import init_log
log = init_log()
user = User(**db_setting)
comment = Comment(**db_setting)
dp_comment = DPComment(**online_db_setting)
dp_image = DPImage(**online_db_setting)

def parse_sina_user(file_path):
    reader = csv.DictReader(file(file_path,'r'))
    count = 0
    for line in reader:
        count+=1
        nickname = line.get('屏幕名')
        if not nickname:
            continue
        gender = line.get('性别','男')
        if gender=='男':
            gender=0
        else:
            gender=1
        vip_desc = line.get('VIP描述')
        if vip_desc:
            continue
        desc = line.get('自我介绍')
        friends_count = covert_count(line.get('关注'))
        fans_count = covert_count(line.get('粉丝'))
        feed_count = covert_count(line.get('微博'))
        avatar = line.get('头像')
        try:
            user.add(nickname,gender,desc,friends_count,fans_count,feed_count,avatar)
        except Exception as e:
            print e
        print 'execute file %s count is -----------------------------------------------%d'%(file_path,count)


def parse_dp_comment(file_path):
    reader = csv.DictReader(file(file_path,'r'))
    count = 0
    for line in reader:
        count+=1
        comment_id = line.get('comment_id')
        shop_id = line.get('shop_id')
        if not comment_id or not shop_id:
            continue
        author = line.get('author')
        author_id = line.get('author_id')
        star = covert_count(line.get('star'))
        taste = covert_count(line.get('taste'))
        environment = covert_count(line.get('environment'))
        service = covert_count(line.get('service'))
        content = line.get('content')
        author_photo = line.get('author_photo')
        photo_1 = line.get('photo1')
        photo_2 = line.get('photo2')
        photo_3 = line.get('photo3')
        photo_4 = line.get('photo4')
        photo_5 = line.get('photo5')
        try:
            comment.add(comment_id,shop_id,author,author_id,star,taste,environment,service,content,author_photo,photo_1,photo_2,photo_3,photo_4,photo_5)
        except Exception as e:
            print e
        print 'execute file %s count is -----------------------------------------------%d'%(file_path,count)
        if count > 10:
            break
def parse_online_dp_comment(file_path):
    reader = csv.DictReader(file(file_path,'r'))
    count = 0
    for line in reader:
        count+=1
        comment_id = line.get('comment_id')
        shop_id = line.get('shop_id')
        if not comment_id or not shop_id:
            continue
        author = line.get('author')
        author_id = line.get('author_id')
        star = covert_count(line.get('star'))
        taste = covert_count(line.get('taste'))
        environment = covert_count(line.get('environment'))
        service = covert_count(line.get('service'))
        content = line.get('content')
        author_photo = line.get('author_photo')
        photo_1 = line.get('photo1')
        photo_2 = line.get('photo2')
        photo_3 = line.get('photo3')
        photo_4 = line.get('photo4')
        photo_5 = line.get('photo5')
        dp_comment.add(shop_id,author,author_photo,content,star)
        if photo_1:
            dp_image.add(shop_id,photo_1)
        if photo_2:
            dp_image.add(shop_id,photo_2)
        if photo_3:
            dp_image.add(shop_id,photo_3)
        if photo_4:
            dp_image.add(shop_id,photo_4)
        if photo_5:
            dp_image.add(shop_id,photo_5)
        log.info('execute file %s count is -----------------------------------------------%d'%(file_path,count))
        print 'execute file %s count is -----------------------------------------------%d'%(file_path,count)

def start_save_user(path):
    import  glob
    fileList = glob.glob(path)
    for file_path in fileList:
        parse_sina_user(file_path)

def start_save_comment(path):
    import  glob
    fileList = glob.glob(path)
    for file_path in fileList:
        parse_online_dp_comment(file_path)

if __name__=="__main__":
    start_save_comment('/Users/seaeast/Desktop/dp/*.csv')


