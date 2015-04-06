
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from time import sleep


class DownVcard:
    def __init__(self):
        self.download_dir = os.getcwd() + "/download/"

        filelist = [f for f in os.listdir(self.download_dir) if f.endswith(".vcf")]
        for f in filelist:
            os.remove(self.download_dir + f)

        self.fp = webdriver.FirefoxProfile()

        self.fp.set_preference("browser.download.folderList",2)
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.download.dir", self.download_dir)
        # thx dude : http://watirmelon.com/2011/09/07/determining-file-mime-types-to-autosave-using-firefox-watir-webdriver/
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octetstream")

        self.driver = webdriver.Firefox(firefox_profile=self.fp)

    def download_vcard(self):
        self.driver.get("http://192.168.1.4/login.html")

        select = Select(self.driver.find_element_by_name("language"))
        select.select_by_visible_text("English")

        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys("1997")
        password.send_keys(Keys.RETURN)

        self.driver.get("http://192.168.1.4/settings_phonebook_transfer.html")
        for teledir_number in range(3):

            if teledir_number:
                teledir_number = str(teledir_number)
                self.driver.find_element_by_id("hs_phonebook_transf_radio_" + teledir_number).click()
                self.driver.find_element_by_link_text("Save").click()

                download_file_path = self.download_dir + "teledir(" + teledir_number + ").vcf.part"
            else:
                self.driver.find_element_by_id("hs_phonebook_transf_radio_0").click()
                self.driver.find_element_by_link_text("Save").click()
                download_file_path = self.download_dir + "teledir.vcf.part"

            sleep(5)
            print(download_file_path)
            while os.path.isfile(download_file_path):
                sleep(1)
            while os.path.isfile(download_file_path):
                sleep(1)
            print("done !")
            sleep(5)
            if teledir_number == "2":
                self.driver.implicitly_wait(5)
                self.driver.get("http://192.168.1.4/logout.html")
                self.driver.implicitly_wait(5)
                self.driver.quit()
