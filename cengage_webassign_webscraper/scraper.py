#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import wget
import re
import os

def clean_str(x):
    if not isinstance(x, str):
        raise TypeError("expected str instance, {} found".format(type(x))
    return x.replace(" ", "_").replace("'", "").replace(chr(416),"").lower()


with open("unit_names.txt", "r") as f:
    unit_names_list = [line.rstrip("\n").replace(" ","_").replace("'","").replace(".","_").lower()
                       for line in f]

unit_names = {i.split(":_", 1)[0]: i.split(":_", 1)[1].replace(":","") for i in unit_names_list}

# for unit in unit_names:
    # url = "https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_{}.html".format(unit)

try:
    os.mkdir("./tmp")
except FileExistsError:
    pass

try:
    os.mkdir("./mp4_files")
except FileExistsError:
    pass


for unit in ["1_1"]:
    files_to_concat = []
    url = "https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_{}.html".format(unit)

    f = open("larcalcet7_menu_1_1.html")
    html_str = f.read()
    # response = requests.get(url)
    parser = BeautifulSoup(html_str, "html.parser")

    for order_number, a_tag in enumerate(parser.find_all("a", href=True)):
        href = a_tag["href"]
        source_filename = re.search(r"\?filename=(?P<filename>.+?)&title=(?P<title>.*)", href).group("filename")
        mp4_link = "http://wowzahttp.cengage.com/apg-math/{}.mp4".format(source_filename)
        download_filename = "".join(["./tmp/", str(order_number), "_", clean_str(a_tag.text), ".mp4"])
        wget.download(mp4_link, download_filename)
        files_to_concat.append(VideoFileClip(download_filename))

    final_mp4_clip = concatenate_videoclips(files_to_concat)
    final_filename = "".join(["./mp4_files/", unit, "_etf_", unit_names[unit], ".mp4"])
    final_mp4_clip.write_videofile(final_filename)
    print(final_filename)

    f.close()

# https://www.webassign.net/resources/larcalcet7/larcalcet7_lectures_1_1.html
# https://www.webassign.net/resources/larcalcet7/larcalcet7_lectures_15_8.html

# Basically a list of links lmao
#  https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_1_1.html




# https://backpack.mcc.edu/Student/?hideProxyDialog=false 
# https://junebug2.mcc.edu/idp/profile/SAML2/POST/SSO



#  https://mottcc.instructure.com/courses/2710/files/99231
# session.headers.update(
    # {
        # "User-Agent": (
            # "Mozilla/5.0 (X11; Linux x86_64; rv:58.0)"
            # "Gecko/20100101 Firefix/58.0"
        # )
    # }
# }





# login_url = "https://mottcc.instructure.com/courses/2710/files/99231/download?download_frd=1"


#download_url = "https://mottcc.instructure.com/courses/2710/files/99231/download"
#username_id = "username"
#password_id = "password"
#submit_button_id = "SignInButton"
#
#your_username = "dfarmer3"
#your_password = "AFKennedy"
#
#
#options = Options()
#options.headless = False
#driver = webdriver.Firefox(options=options)#  'D:/chromedriver.exe',
#
#
#driver.get(login_url)
#
#for _ in range(1):
    #time.sleep(5)
#
    #driver.find_element_by_id(username_id).send_keys(your_username)
    #driver.find_element_by_id(password_id).send_keys(your_password)
    #time.sleep(1)
    #driver.find_element_by_id(submit_button_id).submit()
#
#
#
## print("5 sec remaining...")
## time.sleep(5)
#
#session = requests.Session()
#cookies = driver.get_cookies()
#
#import pickle
#with open("cookies.pkl", "wb") as f:
    #pickle.dump(cookies, f)#, protocol=pickle.HIGHEST_PROTOCOL)
#
#things_to_download = [99231, 99232]
#
#for thing in things_to_download:
    #for cookie in cookies:
        #session.cookies.set(cookie['name'], cookie['value'])
    #response = session.get(f"https://mottcc.instructure.com/courses/2710/files/{str(thing)}/download")
    #with open(f"./files/test{str(thing)}.pdf", 'wb') as f:
        #f.write(response.content)
    #time.sleep(5)
#driver.close()
#


