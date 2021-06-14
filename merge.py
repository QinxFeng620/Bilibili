import pandas as pd
df1=pd.read_csv('bilibili.csv')
df2=pd.read_csv('bilibili_detail.csv')

df=pd.merge(df1,df2,on='media_id')
df.to_csv(r'E:\数据分析方法\18124399冯秦萱\bilibili_data.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")