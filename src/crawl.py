import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
from collections import Counter as cn
import numpy as np

url = "https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all"
options = webdriver.ChromeOptions()
options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(30)
SCROLL_PAUSE_TIME = 2

driver.get(url)

prev_height = driver.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
# 스크롤 가장 아래로 내림
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(2)
  curr_height = driver.execute_script("return document.body.scrollHeight")
  if curr_height == prev_height:
    break
  prev_height = curr_height


print("스크롤 완료")

res = driver.page_source

soup = (bs(res, 'html.parser').select(".job-card-position"))

title = []
for data in soup:
  title.append(data.get_text())

df = pd.DataFrame(soup)
df.head()
df.to_csv("/content/drive/MyDrive/wanted.csv", mode="a")

d = pd.read_csv('/content/drive/MyDrive/wanted.csv')

job = {"프론트엔드": 0,
       "백엔드": 0,
       "안드로이드": 0,
       "IOS": 0,
       "OS": 0,
       "임베디드": 0,
       "풀스택": 0,
       "AI": 0,
       }

value_title = cn(title)


for element in value_title:
  for find_data in job:
    if element.find(find_data) != -1 :
      job[find_data] = job[find_data] + 1
      break;

job_title: str = ["Frontend", "Backend", "Android", "IOS", "OS", "Embedded", "Full-stack", "AI"]
c = []
for k, v in job.items():
  c.append(v)

cv = np.array(c)
x = np.arange(len(c))
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', "#A1B5DC", "#B6B6B6", "#3EAF0E", "#79DAE0"]
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
plt.pie(cv, labels=job_title, autopct='%.1f%%', counterclock=False, startangle=260, colors=colors, wedgeprops=wedgeprops)

plt.title("Developers")
plt.show()

plt.bar(x, c)
plt.xticks(x, job_title, rotation=45)
plt.title("Developers")
plt.show()