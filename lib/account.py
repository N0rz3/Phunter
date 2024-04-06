from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .text import *

class Amazon:
    def setup_driver():
        browser = input(f"[{YELLOW}?{WHITE}] What's your browser? Chrome or Firefox? (c/f): ")

        if browser.lower() == 'c':
            options = Options()
            
            service = Service(ChromeDriverManager().install())

            try:
                driver = webdriver.Chrome(service=service, options=options)
                print(f"[{GREEN}>{WHITE}] Driver setup completed\n")

                return driver, browser.lower()

            except Exception:
                print(f"[{RED}-{WHITE}] Error while driver setup\n")

        elif browser.lower() == 'f':
            options = FirefoxOptions()

            try:
                driver = webdriver.Firefox(options=options)
                print(f"[{GREEN}>{WHITE}] Driver setup completed\n")

                return driver, browser.lower()

            except Exception:
                print(f"[{RED}-{WHITE}] Error while driver setup\n")

    def amazon(p_n, output=False, file=None):
        if output:
            succes = 0

        driver, browser = Amazon.setup_driver()
        print(f"[{YELLOW}~{WHITE}] Phone number: {BLUE}{p_n}{WHITE}")

        driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
        print(f"[{YELLOW}={WHITE}] Checking...")
        
        if browser == 'f':
            input(f"\n[{RED}!{WHITE}] Press ENTER when you have validate the 🤖 Captcha")
            print()
        
        try:
            driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys(p_n)

            driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        except:
            exit(f"[{BLUE}INFO{WHITE}] Error")

        try:
            element = driver.find_element(By.ID, 'auth-password-missing-alert')

            if element:
                print(f"[{GREEN}>{WHITE}] Is connected to Amazon")
                if output != False:
                    with open(file, 'w') as output_file:
                        output_file.write(f"[>] {p_n} is connected to Amazon")
                        succes += 1

            else:
                print(f"[{RED}-{WHITE}] Is not connected to Amazon")
                if output != False:
                    with open(file, 'w') as output_file:
                        output_file.write(f"[-] {p_n} is not connected to Amazon")
                        succes += 1

        except:
            print(f"[{RED}-{WHITE}] Is not connected to Amazon")
            if output != False:
                    with open(file, 'w') as output_file:
                        output_file.write(f"[-] {p_n} is not connected to Amazon")
                        succes += 1

        driver.quit()

        if output:
            print(f"\n[{GREEN}>{WHITE}] ✍️ Output saved ({GREEN}{succes}{WHITE})")
            if output != False:
                    with open(file, 'w') as output_file:
                        output_file.write(f"[-] {p_n} is not connected to Amazon")
                        succes += 1

        driver.quit()

        if output:
            print(f"\n[{GREEN}>{WHITE}] ✍️ Output saved ({GREEN}{succes}{WHITE})")
