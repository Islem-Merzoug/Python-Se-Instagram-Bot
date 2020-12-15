from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox()

        # self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)

    def auth(self,username,pw):
        #Authentification
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span')\
        #     .click()
        # sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('Authentified')

        # Security code
        # sleep(120)
        # self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/button')\
        #     .click()
        # print('Security code confiemed')

        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button')\
            .click()
        print('Identifiers saved')

        sleep(20)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")\
            .click()
        sleep(2)
        print('Secured')

        # targeting pages
    def targeting(self, target):
        self.driver.get(target)
        self.driver.implicitly_wait(20)
        print('targeted')

    def like_and_comment(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]')\
            .click()
        print('liked and commented   ')



        sleep(10)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
        #     .send_keys('follow me :D')

        comment = self.driver.find_element_by_xpath("//textarea[@placeholder='Ajouter un commentaire...']").send_keys('follow me :D')






if __name__ == '__main__':
    object = InstagramBot()
    object.auth('learn_and_joy', 'PRETTY@2020')
    object.targeting("https://www.instagram.com/stanleytalksen/")
    # object.targeting("https://www.instagram.com/melou.me/")
    object.like_and_comment()

