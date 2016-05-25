#!/usr/bin/python
# coding: utf-8

help = """ref2pdf.py

Very simple script to return a DOI from a formatted citation.
Can also return a direct link to download the article from Sci-Hub.

This script uses Crossref Simple Text Query Tool:
http://www.crossref.org/SimpleTextQuery/

Usage is limited to 1000 requests per user/per month, and requires signing up
on Crossref's website. The script needs the email address you used to sign up.

Example:
    Input: ./ref2pdf.py myemail@mydomain.com "J.-P. Francoia, R. Pascal and L. Vial, Chem. Commun., 2015, 51, 1953"
    Output: DOI: http://dx.doi.org/10.1039/C4CC08563A

    Input: ./ref2pdf.py -d myemail@mydomain.com "J.-P. Francoia, R. Pascal and L. Vial, Chem. Commun., 2015, 51, 1953"
    Output: Link to download the article: http://cyber.sci-hub.cc/MTAuMTAzOS9jNGNjMDg1NjNh/francoia2014.pdf

Usage:
  ref2pdf.py   [options] <email> <reference>

Options:
  -h --help    Display help
  -d           Will also output a link to download the artice from Sci-Hub (could be illegal, use at your own risk)
"""


import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer
from docopt import docopt


# Define URLs
URL_CROSSREF = "http://www.crossref.org/SimpleTextQuery/"
URL_SCIHUB = "http://sci-hub.cc/"

# Get the arguments
args = docopt(help)
email = args['<email>']
target = args['<reference>']

# Define the user agent
headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'}

# First, get the form and start a session. This is necessary, posting directly
# the parameters doesn't work
s = requests.session()
s.get(URL_CROSSREF)

payload = {'email': email,
           'command': 'Submit',
           'freetext': target}

# Post the form
req = s.post(URL_CROSSREF, data=payload, headers=headers)

# Traceback (most recent call last):
  # File "./ref2pdf.py", line 65, in <module>
    # doi = soup.a.text
# AttributeError: 'NoneType' object has no attribute 'text'

# Parse the result
strainer = SoupStrainer("td", attrs={"class": "resultB"})
soup = BeautifulSoup(req.text, "lxml", parse_only=strainer)
r = soup("td", attrs={"class": "resultB"})

try:
    doi = soup.a.text
except Exception as e:
    print("ref2pdf could not get the DOI from your reference."
    print("A possible reason is an unregistered email address."

print('DOI: {}'.format(doi))

# If option download not activated, do not request the paper from Sci-Hub
if not args['-d']:
    sys.exit()

doi = doi.split("http://dx.doi.org/")[-1]

# Post the form
payload = {'sci-hub-plugin-check': '', 'request': doi}
req = requests.post(URL_SCIHUB, data=payload, headers=headers)

# Past the result to get the link of the paper
strainer = SoupStrainer("iframe", attrs={"id": "pdf"})
soup = BeautifulSoup(req.text, "lxml", parse_only=strainer)

link_to_pdf = soup.iframe['src']

print('Link to download the article: {}'.format(link_to_pdf))


if __name__ == '__main__':
    pass
