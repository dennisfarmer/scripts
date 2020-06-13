#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options  #imports
import requests
import time
# https://backpack.mcc.edu/Student/?hideProxyDialog=false 
# https://junebug2.mcc.edu/idp/profile/SAML2/POST/SSO



#  https://mottcc.instructure.com/courses/2710/files/99231





# old:
# https://backpack.mcc.edu/Student/?hideProxyDialog=false  
login_url = "https://junebug2.mcc.edu/idp/profile/SAML2/POST/SSO;jsessionid=E5399198E62B1D652288463915A7FFB0?execution=e1s1"

login_url = "https://backpack.mcc.edu/Student/?hideProxyDialog=false"

login_url = "https://mottcc.instructure.com/courses/2710/files/99231/download?download_frd=1"


download_url = "https://mottcc.instructure.com/courses/2710/files/99231/download"
username_id = "username"
password_id = "password"
submit_button_id = "SignInButton"

your_username = "XXXXXXXX"
your_password = "XXXXXXXXX"


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)#  'D:/chromedriver.exe',


driver.get(login_url)

for _ in range(1):
    time.sleep(5)

    driver.find_element_by_id(username_id).send_keys(your_username)
    driver.find_element_by_id(password_id).send_keys(your_password)
    time.sleep(1)
    driver.find_element_by_id(submit_button_id).submit()



# print("5 sec remaining...")
# time.sleep(5)

session = requests.Session()
cookies = driver.get_cookies()

import pickle
with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)#, protocol=pickle.HIGHEST_PROTOCOL)

things_to_download = [99231, 99232]

for _id in things_to_download:
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    response = session.get(f"https://mottcc.instructure.com/courses/2710/files/{str(_id)}/download")
    with open(f"./files/test{str(_id)}.pdf", 'wb') as f:
        f.write(response.content)
    time.sleep(5)
driver.close()



