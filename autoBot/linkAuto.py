from selenium import webdriver
from secrets import username,password
from texts import text

class Linkedin():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\user\\Documents\\chromedriver.exe")

    def login(self):
        self.driver.get("https://www.linkedin.com/")

        self.driver.maximize_window()
    
        sign_in = self.driver.find_element_by_xpath('/html/body/nav/a[3]')
        sign_in.click()

        email_id = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_id.send_keys(username)

        pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
        login_btn.click()

    def status(self):

        create_post = self.driver.find_element_by_class_name('share-box__open')
        create_post.click()

        write_post = self.driver.find_element_by_class_name('mentions-texteditor__contenteditable')
        write_post.send_keys(text)

        post_comment = self.driver.find_element_by_class_name('share-actions__primary-action')
        post_comment.click()

    def connection(self):
        self.driver.find_element_by_xpath('//*[@id="mynetwork-nav-item"]').click()
        #self.driver.find_element_by_xpath('//*[contains(@href,"/mynetwork/invitation-manager/")]').click()
        self.driver.find_element_by_xpath('//a[starts-with(@id,"ember") and contains(@href,"/mynetwork/invitation-manager/")]').click()
        

bot=Linkedin()
bot.login()
#bot.status()
#bot.connection()