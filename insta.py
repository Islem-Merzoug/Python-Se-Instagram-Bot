from selenium import webdriver
from time import sleep
# from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint


class InstagramBot:
    links = []

    comments = [
        'FOLLOW MEEEE, I am working on Motivation🚀•••Programming💻•••Business💰 purposes, don\'t hesitate to follow me !! @learn_and_joy',
        'Nouveau concepte !!!! , je travaille sur la Motivation ••• la Programmation💻 ••• le Business, n\'hésitez pas à me suivre sur @learn_and_joy',
        'New concept, je travaille sur la Motivation ••• la Programmation💻 ••• le Business, suivrez @learn_and_joy',
        '@learn_and_joy est un nouveau concepte, Motivation ••• Programmation💻 ••• Business, n\'hésitez pas à me suivre @learn_and_joy',
        'FOLLOW MEEEE, I am working on Motivation🚀•••Programming💻•••Business💰 purposes, don\'t hesitate to follow me !! @learn_and_joy',
        'Nouveau concepte !!!! , je travaille sur la Motivation ••• la Programmation💻 ••• le Business, n\'hésitez pas à me suivre sur @learn_and_joy',
        'New concept, je travaille sur la Motivation ••• la Programmation💻 ••• le Business, suivrez @learn_and_joy',
        '@learn_and_joy est un nouveau concepte, Motivation ••• Programmation💻 ••• Business, n\'hésitez pas à me suivre @learn_and_joy'

    ]

    accounts = [
        'rifka.bjm', 'stanleyytalks'
    ]

    def __init__(self):
        self.login('learn_and_joy', 'PRETTY@2020')
        # self.login('__islemg__', '*professionalinsta@account#')
        self.like_comment_by_hashtag('bejaia')
        # self.comment_on_account()

    def login(self, username, pw):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.send_keys(pw)
        submit_btn = self.driver.find_element_by_xpath(
            "//button[@type='submit']")
        submit_btn.click()
        sleep(30)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except:
            pass
        # try:
        #     self.driver.find_element_by_xpath(
        #         '/html/body/div[4]/div/div/div[3]/button[2]').click()
        # except:
        #     pass
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]") \
                .click()
            sleep(2)
        except:
            pass

        try:
            sleep(3)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button')\
                .click()
            print('Identifiers saved')
        except:
            pass

        try:
            sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")\
                .click()
            sleep(2)
            print('Secured')
        except:
            pass

    def comment_on_account(self):
        urls = []
        for account in self.accounts:
            # get to profile page
            self.driver.get('https://www.instagram.com/{}/'.format(account))

            # get most recent photo
            links = self.driver.find_elements_by_tag_name('a')

            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(0, 4, 1):
                last_photo_url = valid_links[i].get_attribute('href')
                # print(last_photo_url)
                urls.append(last_photo_url)
                print(urls)


        for url in urls:
            self.driver.get(url)
            # comment on the photo
            try:
                sleep(10)
                self.driver.find_element_by_class_name('RxpZH').click()
                sleep(10)
                self.driver.find_element_by_xpath(
                    "//textarea[@placeholder='Ajouter un commentaire...']").send_keys(self.comments[randint(0, 7)])
                sleep(2)
                # self.driver.find_element_by_xpath(
                #     "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(self.comments[randint(0, 1)])
                # sleep(3)
                self.driver.find_element_by_xpath(
                    "//button[@type='submit']").click()
                # sleep(2)
                # self.driver.get('https://www.instagram.com/{}/'.format(account))
                # self.driver.find_element_by_class_name('/html/body/div[4]/div[1]/div/div/a').click()
                sleep(5)
                print('commented')

            except:
                print('not commented')






    def like_comment_by_hashtag(self, hashtag):
        sleep(randint(5, 15))
        # search_box = self.driver.find_element_by_xpath(
        #     "//input[@placeholder='Rechercher']")
        search_box = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_box.send_keys('#'+hashtag)
        sleep(randint(5, 10))
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').send_keys(Keys.ENTER)
        sleep(randint(1, 5))

        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(0,8,1):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)

            # like
            try:
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span').click()
                sleep(randint(1, 5))
                print('liked')
            except:
                print('not liked')


            # comment
            try:
                self.driver.find_element_by_class_name('RxpZH').click()
                sleep(randint(1, 5))
                # self.driver.find_element_by_xpath(
                #     "//textarea[@placeholder='Ajouter un commentaire...']").send_keys(self.comments[1])
                # sleep(randint(1, 5))

                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(self.comments[randint(0, 7)])
                sleep(randint(1, 10))
                self.driver.find_element_by_xpath(
                    "//button[@type='submit']").click()
                sleep(randint(1, 5))
                print('commented')
            except:
                print('not commented')



# def main():
#     my_bot = Bot()


if __name__ == '__main__':
    object = InstagramBot()
    # main()
