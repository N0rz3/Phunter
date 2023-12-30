from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .text import *
from time import sleep

class Annuaire:
    def setup_driver():
        browser = input(f"[{YELLOW}?{WHITE}] What's your browser? Chrome or Firefox? (c/f): ")

        if browser.lower() == 'c':
            options = Options()

            service = Service(ChromeDriverManager().install())

            try:
                driver = webdriver.Chrome(service=service, options=options)
                print(f"[{GREEN}>{WHITE}] Driver setup completed\n")

                return driver

            except Exception:
                print(f"[{RED}-{WHITE}] Error while driver setup\n")

        elif browser.lower() == 'f':
            options = FirefoxOptions()

            try:
                driver = webdriver.Firefox(options=options)
                print(f"[{GREEN}>{WHITE}] Driver setup completed\n")

                return driver

            except Exception:
                print(f"[{RED}-{WHITE}] Error while driver setup\n")

    def annuaire(p_n, output=False, file=None):
        if output:
            succes = 0

        driver = Annuaire.setup_driver()

        driver.get('https://www.pagesjaunes.fr/annuaireinverse')
        print(f"[{RED}!{WHITE}] You have 10s for accept")
        sleep(10)

        driver.find_element(By.XPATH, '//*[@id="quoiqui"]').send_keys(p_n)
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="form_motor_pagesjaunes"]/div/div[2]/div/button').click()
        sleep(1)

        try:
            pn = p_n.replace("+", "")

            result = driver.find_element(By.XPATH, '//*[@id="SEL-nbresultat"]')

            print(f"\n[{GREEN}>{WHITE}] {result.text} result{'s' if int(result.text.strip()) > 1 else ''} found in PageBlanche")
            print(f"[{YELLOW}={WHITE}] Link => {BLUE}https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={pn}&univers=annuaireinverse&idOu={WHITE}")

            if output != False:
                with open(file, 'w') as output_file:
                    output_file.write(f"[>] {result.text} result{'s' if int(result.text.strip()) > 1 else ''} found in PageBlanche\n[=] Link => https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={pn}&univers=annuaireinverse&idOu=")
                    succes += 1

        except:
            print(f"\n[{RED}-{WHITE}] Not result found in PageBlanche")
            if output != False:
                with open(file, 'w') as output_file:
                    output_file.write("[-] Not result found in PageBlanche")
                    succes += 1
 
        driver.quit()

        if output:
            print(f"\n[{GREEN}>{WHITE}] ✍️ Output saved ({GREEN}{succes}{WHITE})")
