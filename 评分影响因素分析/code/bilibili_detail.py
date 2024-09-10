#爬取B站番剧信息 Part2
#18124399 冯秦萱
#2021/3/1
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:\Users\Feng\AppData\Local\Google\Chrome\Application\chromedriver.exe')
print('browser ready')
driver.implicitly_wait(10)
data=[]

#导入part1数据，通过media_id得到详情页的所有url
df=pd.read_csv('data/bilibili_168.csv')
md=list(df['media_id'])
urls=['https://www.bilibili.com/bangumi/media/md{}'.format(md[i]) for i in range(0,len(df))]

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
    except:
        tags=0
        # #评分人数
        # comments=obj.find_element_by_xpath('.//div[@class="media-info-review-times"]').text[:-2]
    try:
        #发布日期
        pub_date=obj.find_elements_by_xpath('.//div[@class="media-info-time"]/span')
        pub_date=pub_date[0].text[:-2]
    except:
        pub_date=0
    try:
        #简介
        intro=obj.find_element_by_xpath('.//div[@class="media-info-intro"]/span[@class="media-info-intro-text"]').text[3:]
    except:
        intro=0
    try:
        #长评
        obj1=driver.find_elements_by_xpath('//ul[@class="clearfix"]//li[@class]')
        long_com=obj1[1].text
    except:
        long_com =0
    try:
        short_com=obj1[2].text
    except:
        short_com=0
    try:
        #配音
        obj2 = driver.find_elements_by_xpath('//div[@class="media-tab-detail-r"]/div[@class="media-info-card"]')
        obj3 = obj2[0].find_elements_by_xpath('.//div[@class="mic-evaluate"]/span[@class]')
        t1 = obj3[1].text
        cv = str(t1).replace('\r', ',').replace('\n', ',')
    except:
        cv=0
    try:
        #制作
        obj4 = obj2[1].find_elements_by_xpath('.//div[@class="mic-evaluate"]/span[@class]')
        t2 = obj4[1].text
        staff = str(t2).replace('\r', ',').replace('\n', ',')
    except:
        staff=0
    row=[tags,pub_date,long_com,short_com,cv,staff,intro]

    data.append(row)
driver.quit()

#导出part2数据
file=pd.DataFrame(data=data,columns=['tags','pub_date','long_com','short_com','cv','staff','intro'])
file['media_id']=df['media_id']
file.to_csv('data/bilibili_detail_168.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")
