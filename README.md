# About ref2pdf

ref2pdf is a simple script to return a DOI from a formatted citation.
It can also return a direct link to download the article from Sci-Hub
(this option could be illegal, use at your own risk).

This script uses Crossref's [Simple Text Query
Tool](http://www.crossref.org/SimpleTextQuery/).

Usage is limited to 1000 requests per user/per month, and requires signing up
on Crossref's website. The script needs the email address you used to sign up.

```bash
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
```
