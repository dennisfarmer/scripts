#!/usr/bin/env python3

import pyperclip
import re

def main():
    option = ""
    print("Q to exit")
    option = input("Enter to load from clipboard: ")
    while option.upper() != "Q":
        url = re.sub(r".?((?:[Ll]aunch)\?.*|(?:[Pp]lugin)\?.*)",
                     r"/launch?&displayDownloadIcon=True",
                     pyperclip.paste()
                     )
        pyperclip.copy(url)
        option = input("Enter to load from clipboard: ")

if __name__ == "__main__":
    main()
