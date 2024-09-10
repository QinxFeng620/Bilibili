import pandas as pd
df1=pd.read_csv('data/data_processed.csv')
# df2=pd.read_csv('data/bilibili_detail_136.csv')
df3=pd.read_csv('data/pub_real_date.csv')
df=pd.merge(df1,df3,on='season_id',how='left')
# df=pd.concat([df1, df3], axis=0, ignore_index=True)
df.to_csv('data/data.csv',index=False,encoding="utf_8_sig")
print("文件输出完毕")
