#爬取B站番剧信息 Part2
#18124399 冯秦萱
#2021/3/1
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver.exe')
print('browser ready')
driver.implicitly_wait(10)
data=[]

#导入part1数据，通过media_id得到详情页的所有url
df=pd.read_csv(r'E:\数据分析方法\bilibili.csv')
md=list(df['media_id'])
urls=['https://www.bilibili.com/bangumi/media/md{}'.format(md[i]) for i in range(0,2000)]

for url in urls:
    driver.get(url)
    time.sleep(1)
    row=[]
    #设置异常处理，找不到即填入空值
    try:
        obj=driver.find_element_by_xpath('//div[@class="media-info-r"]')
        #标签
        tag=obj.find_elements_by_xpath('.//span[@class="media-tags"]/span[@class="media-tag"]')
        tags=[]
        for t in tag:
            item=t.text
            tags.append(item)
        #评分人数
        comments=obj.find_element_by_xpath('.//div[@class="media-info-review-times"]').text[:-2]
        #发布日期
        pub_date=obj.find_elements_by_xpath('.//div[@class="media-info-time"]/span')
        pub_date=pub_date[0].text[:-2]
        #简介
        intro=obj.find_element_by_xpath('.//div[@class="media-info-intro"]/span[@class="media-info-intro-text"]').text[3:]
        row=[tags,comments,pub_date,intro]
    except:
        row = ['', '', '', '']
    data.append(row)
driver.quit()

#导出part2数据
file=pd.DataFrame(data=data,columns=['tags','comments','pub_date','intro'])
file['media_id']=df['media_id']
file.to_csv(r'E:\数据分析方法\18124399冯秦萱\bilibili_detail.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")
