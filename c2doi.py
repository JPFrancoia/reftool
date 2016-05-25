#!/usr/bin/python
# coding: utf-8

import sys
import os
from pprint import pprint as p
# import matplotlib.pyplot as plt
# import numpy as np
import requests
import urllib
from bs4 import BeautifulSoup, SoupStrainer


# # Personal modules
# sys.path.append('/home/djipey/informatique/python/batbelt')
# from easyxls import EasyXls
# import batbelt

url = "http://www.crossref.org/SimpleTextQuery/"
target = "J.-P. Francoia, R. Pascal and L. Vial, Chem. Commun., 2015, 51, 1953"


headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'}

# s = requests.session()
# s.get(url)

# payload = {'email': 'jeanpatrick.francoia@gmail.com', 'command': 'Submit', 'freetext': target}
# req = s.post(url, data=payload, headers=headers)


# # with open('req.html', 'w') as output:
# # output.write(req.text)

# strainer = SoupStrainer("td", attrs={"class": "resultB"})
# soup = BeautifulSoup(req.text, "lxml", parse_only=strainer)

# r = soup("td", attrs={"class": "resultB"})

# doi = soup.a

# print(doi.text)

doi = "10.1039/C4CC08563A"

url = "http://sci-hub.cc/"

payload = {'sci-hub-plugin-check': '', 'request': doi}
req = requests.post(url, data=payload, headers=headers)

print(req.text)

# <input name="request" placeholder="enter URL, PMID / DOI or search string" autocomplete="off" autofocus="" type="textbox">

# <div id="open" onclick="javascript:document.forms[0].submit()"><p><img src="/misc/img/key_1.png" align="middle">open</p></div>

if __name__ == '__main__':
    pass
