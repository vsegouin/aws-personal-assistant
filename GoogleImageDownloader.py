import json
import random
import urllib2

import os
from bs4 import BeautifulSoup

SAVE_IMAGE = True
MAX_IMAGE = 1


def get_soup(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'html.parser')


def get_image_from_google(query):
    index = 0
    image_type = "ActiOn"
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
    print url
    # add the directory for your image here
    DIR = "Pictures"
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url, header)

    ActualImages = []  # contains the link for Large original images, type of  image
    for a in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link, Type))
    number_of_images = len(ActualImages)
    print  "there are total", number_of_images, "images"

    if SAVE_IMAGE:
        if not os.path.exists(DIR):
            os.mkdir(DIR)
        DIR = os.path.join(DIR, query.split()[0])

        if not os.path.exists(DIR):
            os.mkdir(DIR)
    ###print images

    print("random" + repr(random.randint(0, number_of_images)));
    imgSelected = ActualImages[random.randint(0, number_of_images)]
    print(imgSelected)
    img = imgSelected[0]
    Type = imgSelected[1]
    try:
        req = urllib2.Request(img, headers={'User-Agent': header})
        raw_img = urllib2.urlopen(req).read()

        if SAVE_IMAGE:
            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print cntr
            if len(Type) == 0:
                f = open(os.path.join(DIR, image_type + "_" + str(cntr) + ".jpg"), 'wb')
            else:
                f = open(os.path.join(DIR, image_type + "_" + str(cntr) + "." + Type), 'wb')

            f.write(raw_img)
            f.close()
        return raw_img

    except Exception as e:
        print "could not load : " + img
        print e
