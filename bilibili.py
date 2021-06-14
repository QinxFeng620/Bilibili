#爬取B站番剧信息 Part1
#18124399 冯秦萱
#2021/3/1
import time
import pandas as pd
import json
import requests

#A.番剧索引信息(api)
a_url='https://api.bilibili.com/pgc/season/index/result?st=1&year=-1&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&style_id=-1&order=4&sort=0&page={}&season_type=1&pagesize=20&type=1'
#B.番剧播放信息（api)
b_url='https://api.bilibili.com/pgc/web/season/stat?season_id={}'
#C.番剧详情信息（selenium）
c_url='https://www.bilibili.com/bangumi/media/md{}'

page =1
data=[]
while page<101:
    print("爬取第",page,'页中')
    #爬取A中信息
    A_url = [a_url.format(page)]
    rep=requests.get(A_url[0],timeout=60)
    rep=rep.json()
    items=rep.get('data').get('list')

    for item in items:

        title=item['title']                 #标题
        episodes=item['index_show']         #集数
        mark=item['badge']                  #标志
        score=item['order']                 #评分
        is_finish=item['is_finish']         #是否完结
        link=item['link']                   #播放链接
        media_id = item['media_id']         #详情id
        season_id=item['season_id']         #播放id

        #爬取B中信息
        B_url=[b_url.format(season_id)]
        rep = requests.get(B_url[0], timeout=60)
        rep = rep.json()
        dic = rep.get('result')

        series_follow=dic['series_follow']  #系列追番人数
        follows=dic['follow']                #追番人数
        coins=dic['coins']                  #投币数
        likes=dic['likes']                  #点赞数
        danmus=dic['danmakus']              #弹幕数
        views=dic['views']                  #播放数

        row=[title,episodes,mark,score,is_finish,link,series_follow,follows,coins,likes,danmus,views,season_id,media_id]
        data.append(row)
    page+=1

#导出part1数据
df=pd.DataFrame(data=data,
                columns=['title','episodes','mark','score','is_finish','link','series_follow','follows','coins','likes','danmus','views','season_id','media_id'])
df.to_csv(r'E:\数据分析方法\18124399冯秦萱\bilibili.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")






