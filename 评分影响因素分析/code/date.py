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
#D.地区+评分人数（api)
d_url='https://api.bilibili.com/pgc/review/user?media_id={}'
e_url='https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=4&st=1&sort=0&page={}&season_type=1'

page =1
data=[]
for page in range(0,114):
    print("爬取第",page,'页中')
    #爬取A中信息
    A_url = [e_url.format(page)]
    rep=requests.get(A_url[0],timeout=60)
    rep=rep.json()
    items=rep.get('result').get('data')

    for item in items:

        title=item['title']                 #标题
        season_id=item['season_id']         #播放id
        dic = item.get('order')
        pub_real_date=dic["pub_real_time"]
        row=[title,season_id,pub_real_date]
        data.append(row)
    print("第{}页爬取结束！".format(page))
    page+=1

#导出part1数据
df=pd.DataFrame(data=data,
                columns=['title','season_id','pub_real_date'])
df.to_csv('data/pub_real_date.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")