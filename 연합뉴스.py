#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:56:01 2020

@author: baekjiyoon
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup as bs
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
browser.get('https://www.yna.co.kr/safe/index?site=navi_safe_depth01')
time.sleep(10)
for x in range(10):
    time.sleep(0.1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    
soup=bs(browser.page_source,'html.parser')
result_link=soup.select('#container > div > div.inner > section > div > div.list-wrap > div > ul.list01 > li:nth-child(1) > article > div.news-con > a')
result_link_list=[]
for result in result_link:
    result_link_list.append(result)

        
    



#%%
result_link_tlist=[]
for result in result_link_list:
    if result.attrs['href']:
        result_link_tlist.append(result.attrs['href'])
#%%
print(result_link_tlist)
from urllib.request import urlopen
for items in result_link_tlist:
    html=urlopen('https:'+ items)
    bss=bs(html,'html.parser')
    rough_contents=bss.select('#articleWrap > div > p')
    for contents in bss.select('#articleWrap > div > p'):
        print(contents.text)