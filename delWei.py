from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
import time

class deleter():
    def createBrowserInstance(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://www.baidu.com") 

    def deleteBrowserInstance(self):
        self.browser.close()

    def getFeedList(self):
        return self.browser.find_element_by_class_name("WB_feed") 

    def deleteTopPost(self, feedList):
        # feedList.find 
        box = feedList.find_element_by_class_name("screen_box")
        box.find_element_by_xpath(".//a").click()
        delBtn = box.find_element_by_xpath(".//ul/li[1]/a")
        delBtn.click()
        delConfirm = box.find_element_by_class_name("W_layer")        
        delConfirm.find_element_by_xpath(".//div/p[2]/a[1]").click()
        pass


if __name__ == "__main__":
    inst = deleter()
    inst.createBrowserInstance()
    text = input("input 'OK' to continue\n")
    if text != "OK":
        inst.deleteBrowserInstance()

    while True:
        try:
            for _ in range(50):
                flist = inst.getFeedList()
                inst.deleteTopPost(flist)
                time.sleep(1)
        except (NoSuchElementException, ElementNotVisibleException, WebDriverException):
            text = input("input 'OK' to continue\n")
            if text!="OK":
                inst.deleteBrowserInstance()
            continue