import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv

def getcsv(path):
    csvlist = []
    with open(path, 'r') as f:
        reader = list(csv.reader(f))
    return reader

def savecsv(path,csvlist):
    with open(path,'w') as f:
        i = 0
        for ls1 in csvlist:
            j = 0
            for ls2 in ls1:
                f.write(ls2)
                if j < len(ls1) - 1:
                    f.write(",")
                j += 1
            if i < len(csvlist) - 1:
                f.write("\n")    
            i += 1

driver = webdriver.Chrome('./chromedriver')
driver.get("https://news.yahoo.co.jp/hl?c=game")
url_list = []
log_list = getcsv("yahoo_log.csv")
end = False
for a in driver.find_elements_by_css_selector('#main > div.epCategory > div > ul > li:nth-child(n) > a'):
    url = a.get_attribute('href')
    for log_url in log_list:
        if str(log_url[0]) == str(url):
            end = True
            break
    if end:
        break
    url_list.append([url])

for url in url_list:
    driver.get(url[0])
    for title in driver.find_elements_by_css_selector('#ym_newsarticle > div.hd > h1'): #タイトル
        url.append(title.text)
    for text in driver.find_elements_by_css_selector('#ym_newsarticle > div.articleMain > div.paragraph > p'): #本文
        url.append(text.text)
    time.sleep(1)

driver.quit()
log_list = url_list + log_list

for ls in log_list:
    ls[1] = ls[1].replace("\n","").replace("\u3000","").replace("\xa9","")
    ls[2] = ls[2].replace("\n","").replace("\u3000","").replace("\xa9","")

for ls in url_list:
    ls[1] = ls[1].replace("\n","").replace("\u3000","").replace("\xa9","")
    ls[2] = ls[2].replace("\n","").replace("\u3000","").replace("\xa9","")

savecsv("yahoo_log.csv",log_list)
savecsv("omake/yahoo_onetimelog.csv",url_list)