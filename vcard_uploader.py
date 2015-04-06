
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from time import sleep


class UpVcard:
    def __init__(self):
        self.download_dir = os.getcwd() + "/download/"

        self.fp = webdriver.FirefoxProfile()

        self.fp.set_preference("browser.download.folderList",2)
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.download.dir", self.download_dir)
        # thx dude : http://watirmelon.com/2011/09/07/determining-file-mime-types-to-autosave-using-firefox-watir-webdriver/
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octetstream")

        self.driver = webdriver.Firefox(firefox_profile=self.fp)

    def upload_vcard(self, trusted_vcard_path):
        self.driver.get("http://192.168.1.4/login.html")

        select = Select(self.driver.find_element_by_name("language"))
        select.select_by_visible_text("English")

        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys("1997")
        password.send_keys(Keys.RETURN)

        self.driver.get("http://192.168.1.4/settings_phonebook_transfer.html")
        sleep(5)

        def catch_alert():
            try:
                WebDriverWait(self.driver, 100).until(EC.alert_is_present())

                alert = self.driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except TimeoutException:
                print("no alert -- attempting something crazy")
                self.driver.get("http://192.168.1.4/status.html")
                try:
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())

                    alert = self.driver.switch_to.alert
                    alert.accept()
                    print("alert finally accepted")
                except TimeoutException:
                    print("I give up")
                    raise TimeoutException


            sleep(5)

        for handset_id in range(3):
            print(handset_id)
            self.driver.find_element_by_id("hs_phonebook_transf_radio_" + str(handset_id)).click()
            self.driver.find_element_by_link_text("Delete").click()
            # Catch the delete question
            catch_alert()

            sleep(2)

            # catch the confirmation
            catch_alert()
            self.driver.find_element_by_id("hs_phonebook_transf_radio_" + str(handset_id)).click()

            if True:
                sleep(5)
                input_file = self.driver.find_element_by_id("tdt_file")
                #input_file.clear()
                input_file.send_keys(trusted_vcard_path)
                #input_file.send_keys(Keys.RETURN)

                self.driver.find_element_by_link_text("Transfer").click()
                catch_alert()
                # catch the confirmation

            sleep(5)

        if True:
            self.driver.implicitly_wait(5)
            self.driver.get("http://192.168.1.4/logout.html")

            self.driver.quit()
