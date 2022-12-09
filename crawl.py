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

title: str = []
for data in soup:
  title.append(data.get_text())

df = pd.DataFrame(soup)
# print(len(title))
# print(title)
df.head()
df.to_csv("/content/drive/MyDrive/wanted.csv", mode="a")

job = {"프론트엔드": 0,
       "백엔드": 0,
       "안드로이드": 0,
       "IOS": 0,
       "Dev-Ops": 0,
       "OS": 0,
       "임베디드": 0,
       "풀스택": 0,
       "AI": 0,
       "기타" : 0}

value_title = cn(title)


for element in value_title:
  for find_data in job:
    if element.find(find_data) != -1 :
      job[find_data] = job[find_data] + 1
      break;

print(job)