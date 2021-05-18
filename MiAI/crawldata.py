from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='E:\Documents\Python\logincrawl\chromedriver')
browser.get("https://www.facebook.com/groups/miaigroup")
sleep(2)
expand = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]/span/span")
expand.click()

comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")


# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
for comment in comment_list:
    print(comment)
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    # poster = comment.find_element_by_class_name("pq6dq46d")
    # content = comment.find_element_by_class_name("_3l3x")
    # print("*", poster.text,":", content.text)





