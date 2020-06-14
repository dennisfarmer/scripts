#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import wget
import re
import os



temp_directory = "./tmp"
mp4_directory = "./mp4_files"


def clean_str(x):
    if not isinstance(x, str):
        raise TypeError("expected str instance, {} found".format(type(x)))
    return x.replace(" ", "_").replace("'", "").replace(chr(416),"").lower()


with open("unit_names.txt", "r") as f:
    unit_names_list = [line.rstrip("\n").replace(" ","_").replace("'","").replace(".","_").lower()
                       for line in f]

unit_names = {i.split(":_", 1)[0]: i.split(":_", 1)[1].replace(":","") for i in unit_names_list}


for path in [mp4_directory, temp_directory]:
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


for unit in unit_names:
    
    files_to_concat = []

    url = "https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_{}.html".format(unit)
    
    
    ### Fixes for Cengage's terrible webdesign: ##############################################
    
    # Unit 1.4 is wierdly named "P.4" for no reason at all
    if url == "https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_1_4.html":
        url = "https://www.webassign.net/resources/larcalcet7/menus/larcalcet7_menu_P_4.html"
        
    # Webpages for unit 7.1 and on have a slightly different format for video links
    # However, after 7.1 some of the original formatting is sprinkled in just because the devs
    # felt like it would be a good idea, so both link styles are accounted for
    regex_default = r"video_explanations\/(.+?)\.html"
    regex_alternate = r"\?filename=(.+?)&title=.*" # <-- will raise exception at 
                                                   # unit 7.1 if set as regex_default
    
    ##########################################################################################
    
    
    response = requests.get(url)
    parser = BeautifulSoup(response.content, "html.parser")

    # Iterate over list of <a>...</a> tags
    for order_number, a_tag in enumerate(parser.find_all("a", href=True)):
        href = a_tag["href"]
        
        # Retreve mp4 filename from each a_tag href string
        source_filename = re.search(regex_default, href).group(1)
        if source_filename == "video_wrapper":
            source_filename = re.search(regex_alternate, href).group(1)
        
        # Create link to mp4 file from parsed HTML text, then download to temp folder with wget
        mp4_link = "http://wowzahttp.cengage.com/apg-math/{}.mp4".format(source_filename)
        download_filename = "".join([temp_directory,"/", str(order_number), "_", clean_str(a_tag.text), ".mp4"])
        wget.download(mp4_link, download_filename)
        
        # Load each subsection video into moviepy to be concatenated into a single video covering
        # the entirety of each unit
        files_to_concat.append(VideoFileClip(download_filename))

    print()
    final_mp4_clip = concatenate_videoclips(files_to_concat)
    final_filename = "".join([mp4_directory, "/", unit, "_etf_", unit_names[unit], ".mp4"])
    final_mp4_clip.write_videofile(final_filename)
    print("FINISHED DOWNLOAD - ", final_filename, "\n")
    
    for f in os.listdir(temp_directory):
        os.remove("".join([temp_directory, "/", f]))

os.rmdir(temp_directory)
