#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:13:00 2020

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
browser.get('https://www.yna.co.kr/safe/news/3')
time.sleep(10)
for x in range(10):
    time.sleep(0.1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    
soup=bs(browser.page_source,'html.parser')
result_link=soup.findAll('a')
result_link_list=[]
for result in result_link:
    result_link_list.append(result)

browser.close()
#%%
result_link_tlist=[]
for result in result_link_list:
    if result.attrs['href']:
        result_link_tlist.append(result.attrs['href'])
#%%
print(result_link_tlist)
result_clear=[]
for result in result_link_tlist:
    if result.startswith('//www.yna.co.kr/view/A'):
        result_clear.append(result)
#%%
print(result_clear)

#%%
from urllib.request import urlopen 
last_url=   '//www.yna.co.kr/view/AKR20200824024900002?section=safe/news'
html=urlopen('https:'+last_url)
bsss=bs(html,'html.parser')
rough_title=bsss.findAll(class_='tit')
for result in rough_title:
    print(result.text)
    f=open('0823_'+result.text+'.txt',mode='wt',encoding='utf-8')
    f.write(result.text)
    f.close()
   
   
    

html=urlopen('https:'+ last_url)
bss=bs(html,'html.parser')
rough_contents=bss.select('#articleWrap > div > p')
for contents in bss.select('#articleWrap > div > p'):
        print(contents.text)
       

#%%
f=open('0823_'+result.text+'.txt',mode='wt',encoding='utf-8')
f.write(result.text+contents.text)
f.close




