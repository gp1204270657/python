#coding=utf-8
from selenium import webdriver

chrom_options=webdriver.ChromeOptions()
chrom_options.add_argument('--headless')
driver=webdriver.Chrome(chrome_options=chrom_options)
driver.get('https://www.baidu.com')
print('----------->',driver.title)