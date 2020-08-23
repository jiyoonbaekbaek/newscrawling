# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
browser.get('https://www.cnbc.com/search/?query=covid-19&qsearchterm=covid-19')
time.sleep(10) #파이썬 일시 정지 
for x in range(10):
    time.sleep(0.1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    #페이지 하단으로 스크롤 
    

soup=bs(browser.page_source,'html.parser')
result_link=soup.findAll(class_='resultlink')
result_link_list=[]
for result in result_link:
    if result.attrs['href']:
        result_link_list.append(result.attrs['href'])
        
    
   

#%%
print(result_link_list)
#%%
from urllib.request import urlopen
for items in result_link_list:
    html=urlopen(items)
    bss=bs(html,'html.parser')
    rough_contents=bss.findAll(class_='group')
    for tag in bss.findAll(class_='group'):
        print(tag.text)
    


   
    
