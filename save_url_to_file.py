#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# https://github.com/igoradmtg/

# Example:
# save_url_to_file.py "http://google.com" google.html 5
# save_url_to_file.py "https://2ip.ru/" 2ip_ru.html 15 --proxy-server=socks5://127.0.0.1:9050
# save_url_to_file.py "https://1337x.to/cat/XXX/5/" 1337x_to.html 15 --proxy-server=socks5://127.0.0.1:9050

import sys
import time
from selenium import webdriver

def main():
    if (len(sys.argv)<3) :
        print("Error argument "+str(len(sys.argv)))
        print("Use:")
        print("save_url_to_file.py \"http://google.com\" localfile [timeout sleep]")
        print(" url - load url ")
        print(" localfile - save to file")
        print(" timeout sleep - timeout before save file. Default 10 (seconds)")
        return
    url_download = sys.argv[1]
    file_name = sys.argv[2]
    time_sleep = 10
    if len(sys.argv)>=4:
        time_sleep = int(sys.argv[3])
        
    chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless");
    chrome_options.add_argument("--no-sandbox");
    if len(sys.argv)>=5:
        for i in range(4,len(sys.argv)) :
            print("Add argument",sys.argv[i])
            chrome_options.add_argument(sys.argv[i])
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(4) # seconds
    print("Load url",url_download)
    browser.get(url_download)
    print("Sleep",time_sleep)
    time.sleep(time_sleep)
    print("Save file",file_name)
    with open(file_name, "w", encoding='utf-8') as f:
        f.write(browser.page_source)
    browser.quit()


if __name__ == '__main__':
    main()