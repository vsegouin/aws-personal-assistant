import json
import random
from urllib.request import urlopen, Request

import os
from bs4 import BeautifulSoup

SAVE_IMAGE = True
MAX_IMAGE = 1

class GoogleImageDownloader:

    def get_soup(url, header):
        return BeautifulSoup(urlopen(Request(url, headers=header)), 'html.parser')


    def get_image_from_google(query):
        query = query.split()
        query = '+'.join(query)
        url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
        print(url)
        # add the directory for your image here
        directory = "Pictures"
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/"
                          "537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
        soup = get_soup(url, header)

        actual_images = []  # contains the link for Large original images, type of  image
        for a in soup.find_all("div", {"class": "rg_meta"}):
            link, image_type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            actual_images.append((link, image_type))
        number_of_images = len(actual_images)
        print("there are total", number_of_images, "images")

        if SAVE_IMAGE:
            if not os.path.exists(directory):
                os.mkdir(directory)
            directory = os.path.join(directory, query.split()[0])

            if not os.path.exists(directory):
                os.mkdir(directory)

        img_selected = actual_images[random.randint(0, number_of_images)]
        img = img_selected[0]
        image_type = img_selected[1]
        try:
            req = Request(img, headers={'User-Agent': header})
            raw_img = urlopen(req).read()

            if SAVE_IMAGE:
                cntr = len([i for i in os.listdir(directory) if image_type in i]) + 1
                print(cntr)
                if len(image_type) == 0:
                    f = open(os.path.join(directory, image_type + "_" + str(cntr) + ".jpg"), 'wb')
                else:
                    f = open(os.path.join(directory, image_type + "_" + str(cntr) + "." + image_type), 'wb')

                f.write(raw_img)
                f.close()
            return raw_img

        except Exception as e:
            print("could not load : " + img)
            print(e)
