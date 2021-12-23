# 基于 B 站番剧信息的点赞量预测

 2020冬-数据分析方法课程大作业
 
B 站上有许多番剧，有的火爆至极，有的却无人问津，作为国内最受年轻人欢迎的番剧平台，其番剧数据为创作者提供了创作目标和方向.通过**爬取 Bilibili 网站**番剧的集数，评分，播放量，投币数等相关信息，利用 python 对这些番剧进行数据挖掘，经过探索性分析和**数据可视化**直观展现出 B 站番剧的人气特征和发展特点，再结合**机器学习算法**，构建了番剧点赞量预测模型并调整优化，最后对实验结果进行了分析。

文件目录大致如下：
* 爬虫程序：`bilibili.py`, `bilibili_detail.py`
* 爬取的数据：`bilibili_data.csv`（2000 rows,18 columns）
* 数据分析程序：`bilibili数据分析.ipynb`（包括数据处理，可视化，模型）
* 处理后的数据：`bilibili_processed.csv`
* 特征工程后的数据：`bilibili_feature.csv`
* 具体内容可以看 ：`中期报告.docx` 和 `Final 报告.pdf`

做完后值得记录的一些点：
* 用**api接口**爬取数据还挺快的（前提是找得到），**selenium**（好玩）不容易被发现。。。
* 一部番剧有多个番剧标签（爬的时候没考虑到，爬取到是一个包含多个标签的字符串），用**正则表达式**来提取这些标签
* **wordcloud** 可以做热门标签的词云图

## 爬取数据
B 站番剧**索引页，播放页和详情页**中含有关于番剧的大量信息。如剧集数，追番人数，投币数，点赞数，弹幕数，播放数，标签等。   
对于这三个页面的信息，并不是访问某一个接口就可以获取全部的研究所需数据字段，而是要结合多个数据接口来爬取。
这里我分了两部分爬取后合并。在 2021 年 2 月 28 日爬取了 B 站 100页，每页 20 个番剧，共 2000 条番剧信息数据。
* 完整的爬虫程序：`bilibili.py`, `bilibili_detail.py`
* 爬取的数据文件：`bilibili_data.csv`
### 1. 爬取程序（bilibili.py, bilibili_detail.py）
#### Part 1 (`bilibili.py`)
**番剧索引页**爬取番剧名，剧集数，分级，评分，是否完结，播放链接，番剧id，详情id  

![1](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/%E8%A7%A3%E9%87%8A/%E7%B4%A2%E5%BC%95%E9%A1%B5.png)

**播放页**爬取系列追番人数，追番人数，投币数，点赞数，弹幕数，播放数，

![2](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/%E8%A7%A3%E9%87%8A/%E6%92%AD%E6%94%BE%E9%A1%B5.png)
#### Part2 (`bilibili_detail.py`)
**详情页**爬取标签，评分人数，发布日期，简介

![3](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/%E8%A7%A3%E9%87%8A/%E8%AF%A6%E6%83%85%E9%A1%B5.png)
### 2. 数据概述（bilibili_data.csv)
**爬取来源**：[bilibili番剧索引网页](https://www.bilibili.com/anime/index/#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=4&st=1&sort=0&page=1)

**工具**：python（主要使用api接口和selenium）

**大小**：2000 rows x 18 columns

![说明](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/%E8%A7%A3%E9%87%8A/%E7%95%AA%E5%89%A7%E4%BF%A1%E6%81%AF%E5%AD%97%E6%AE%B5%E8%AF%B4%E6%98%8E.png)

## 可视化

<div align="center">
 <img src="https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/Top%2010%20%E7%83%AD%E9%97%A8%E6%A0%87%E7%AD%BE.png"/)
</div>  
 
**标签词云**

![说明](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/%E7%83%AD%E9%97%A8%E6%A0%87%E7%AD%BE%E8%AF%8D%E4%BA%91.png)

**特征的皮尔逊系数图**

![说明](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/heatmap.png)

**模型对比**
 
![说明](https://github.com/QinxFeng620/Bilibili-selenium-2020Winter/blob/main/model%20comparison.png)



