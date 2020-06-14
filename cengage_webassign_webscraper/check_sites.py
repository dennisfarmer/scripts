#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
import re

with open("unit_names.txt", "r") as f:
    unit_names_list = [line.rstrip("\n").replace(" ","_").replace("'","").replace(".","_").lower()
                       for line in f]

unit_names = {i.split(":_", 1)[0]: i.split(":_", 1)[1].replace(":","") for i in unit_names_list}

for unit in unit_names:

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

    for a_tag in parser.find_all("a", href=True):
        href = a_tag["href"]
        try:
            source_filename = re.search(regex_default, href).group(1)
            if source_filename == "video_wrapper":
                source_filename = re.search(regex_alternate, href).group(1)

        except Exception as e:
            print("ERROR!!!! \n", "Type:", e, "\nUnit: ", unit,sep="")
            break
        
        print(" Unit: ", unit, "\t\tFilename: ", source_filename+".mp4",sep="")
        
# This script was used to make sure regex patterns and urls are working properly before the actual
# webscraping / mp4_download script is used.
#
#
#             OUTPUT:
#
#
#Unit: 1_1              Filename: v02379a.mp4                                                                          
#Unit: 1_1              Filename: v03247a.mp4                                                                           
#Unit: 1_1              Filename: v03247b.mp4                                                                           
#Unit: 1_1              Filename: v00352a.mp4                                                                           
#Unit: 1_1              Filename: v01915a.mp4                                                                           
#Unit: 1_1              Filename: v01915b.mp4                                                                           
#Unit: 1_1              Filename: v02382a.mp4                                                                           
#Unit: 1_2              Filename: v00348a.mp4                                                                           
#Unit: 1_2              Filename: v00915a.mp4                                                                           
#Unit: 1_2              Filename: v03012a.mp4                                                                           
#Unit: 1_2              Filename: v03013a.mp4                                                                           
#Unit: 1_2              Filename: v00274a.mp4                                                                           
#Unit: 1_3              Filename: v03237a.mp4                                                                           
#Unit: 1_3              Filename: v00184a.mp4                                                                           
#Unit: 1_3              Filename: v00386a.mp4                                                                           
#Unit: 1_3              Filename: v00945a.mp4                                                                           
#Unit: 1_3              Filename: v00300a.mp4                                                                           
#Unit: 1_3              Filename: v02022a.mp4                                                                           
#Unit: 1_4              Filename: v00029a.mp4                                                                           
#Unit: 1_4              Filename: v00750a.mp4                                                                           
#Unit: 1_4              Filename: v00812a.mp4                                                                           
#Unit: 1_4              Filename: v00008a.mp4                                                                           
#Unit: 1_4              Filename: v01979a.mp4                                                                           
#Unit: 1_4              Filename: v01726a.mp4                                                                           
#Unit: 1_4              Filename: v00690a.mp4                                                                           
#Unit: 1_4              Filename: v00824a.mp4                                                                           
#Unit: 1_4              Filename: v02084a.mp4                                                                           
#Unit: 1_4              Filename: v00601a.mp4 
#...                    ...
#...                    ...
