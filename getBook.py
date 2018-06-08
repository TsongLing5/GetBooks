import time
import urllib


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib import request



# url ='http://music.163.com/#/my/m/music/playlist?id=14514582'
# url='http://music.163.com/#'
# url='http://music.163.com/#/login'
from selenium.webdriver.support.wait import WebDriverWait

# url='http://www.my285.com/WUXIA/jinyong/sdxl/001.htm'    #神雕侠侣
# url='http://www.my285.com/wuxia/jinyong/yttlj/001.htm'   #一天屠龙记
# url="http://www.my285.com/wuxia/jinyong/sdyxz/001.htm"     #射雕英雄传
url='http://www.my285.com/wuxia/jinyong/xajh/001.htm'    #笑傲江湖


fp = open("笑傲江湖.txt","w")
index=331 #神雕侠侣 327   倚天屠龙记295  射雕英雄传283  笑傲江湖331

driver = webdriver.Chrome()
# driver.set_page_load_timeout(10)


driver.get(url)
# driver.execute_script('window.stop()')


    # now_handle =  driver.current_window_handle #得到当前窗口句柄
    # driver.implicitly_wait(10)

driver.maximize_window()
driver.implicitly_wait(5)
# driver.set_page_load_timeout(30)
# driver.set_script_timeout(30)

for i in range(0,327):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup)

    tables=soup.findAll('table')
    tab=tables[2]
    tr=tab.tbody.findAll('tr')
    title=tr[1].getText()
    print(title)
    content=tr[3].getText()
    print(content)



    fp.write(title)
    # time.sleep(1)
    fp.write(content)
    # next()

    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "下一页"))
    # )
    # nextpPage = driver.find_element_by_partial_link_text("下一页")
    # nextpPage.click()


    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "下一页"))
        )

    except TimeoutException:
        print("我凑，没找到")

    finally:
        print("找到啦！")

    try:
        driver.find_element_by_partial_link_text(u"下一页").click()
        # nextPage=driver.find_element_by_partial_link_text(u"下一页")
        # nextPage.click()
    except TimeoutException:
        print("我凑，链接超时啦！")
    finally:
        pass


    # try:
    #
    #     nextpPage = driver.find_element_by_partial_link_text("下一页")
    #     nextpPage.click()
    # except TimeoutException:
    #     soup = BeautifulSoup(driver.page_source, "html.parser")
    #     print(soup)
    #     print("我凑！又出事了！")
    #     # driver.execute_script('windows.stop()')
    #     # print(soup)
    # finally:
    #     print("Finally!")




    # time.sleep(1)
    # for td in tr[3].findAll('td'):
        # print(td.getText())
        # fp.write(tr[1])
    # try:


    # except TimeoutException:
    # time.sleep(10)
    # driver.execute_script('window.stop()')

fp.close()


def NextPage():
    try:
        pass
        # nextpPage = wait.until(driver.find_element_by_partial_link_text("下一页"))
        # nexit.until(EC.element_to_be_clickable(By.LINK_TEXT))
        # nextpPage.click()tpPage = wa


    except TimeoutException:
        return NextPage()



# def main():
#     pass
#
# if __name__=='__main__':
#     main()


# t=driver.find_element_by_xpath("//tbody/tr[6]/td/a[3]")
# t.click()
# print(t)

# driver.find_element_by_xpath("//a[@text='js-primary u-btn2 u-btn2-2']").click()

    # for td in tr.findAll('td'):


# driver.find_ele


# driver.implicitly_wait(10)


# driver.switch_to.frame( driver.find_element_by_id("g_iframe"))
# a= driver.find_elements_by_xpath("//div[@class='u-alt']/ul/li/a")
# a[3].click()


# driver.find_element_by_id("index-enter-default").click()
# page.click()
# driver.get("http://www.python.org")

# assert "EZ0000000" in driver.title

# time.sleep(10)
# page = request.urlopen(url)
#
# # soup = BeautifulSoup(driver.page_source, "html.parser")
# soup = BeautifulSoup(page)
# print(soup)
# # current_na`mes = soup.select('div.g-mn3 f-pr j-flag')
# # current_names=soup.find_all
#
# print("####################")
# # current_names=soup.find('table')
# # current_names=soup.find_all('div', class_='m-table')
# for x in soup.findAll("b"):
#     print(x['title'])

# tab=current_names[0]
#
# print(tab)
# for t in current_names:
#     print(t)
# for tr in tab.tbody.findAll('tr'):
#
#     td=tr.findAll('td')
#     # td[1].find_all()
#     print(td[1])



# current_names=soup.find('table', attrs={'class':'m-table '})
# print(tab)
# for song in current_names:
#     print(song.find_all(["b","a"]).get('title'))
# cuu=soup.find_all('b')
#
#
# # elem=driver.find_element_by_id("auto-id-P4ymh7dRGVCi7hc4")
# # elem = driver.find_element_by_id("kw")
# # elem.send_keys("周杰伦")      #input selenium
# #getList.py:14
# # elem.send_keys(Keys.RETURN)     #input return
# # print(driver.page_source)    #print web sorce


# import os, sys
# import urllib
# import urllib.request
# import urllib.parse
# # import urllib2
# from bs4 import BeautifulSoup
#
# # 体彩 排列5
# URL="https://music.163.com/#/playlist?id=14514582"
# # URL = "http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw"
# page = urllib.request.urlopen(URL)
# soup = BeautifulSoup(page)
# page.close()
#
# # fp = open("pl5.txt", "w")
# tables = soup.findAll('table')
# tab = tables[2]
# # for t in tables:
# #     for tr in t. tab.tbody.findAll('tr'):
# #         print(tr)
# #         # for td in tr.findAll('td'):
# #         #     print(td)
# for tr in tab.tbody.findAll('tr'):
#     print(tr)
#     # for td in tr.findAll('td'):
#     #     text = td.getText().encode('cp936') + '!'
#     #     # fp.write(text)
#     #     print(text)
#     # fp.write('\n')
# #
# # fp.close()