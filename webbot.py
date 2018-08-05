import mechanize
import time
from bs4 import BeautifulSoup
import string
import urllib

start = "http://www.irrelevantcheetah.com/browserimages.html"
filetype = raw_input ("What file type are you looking for?\n")
br = mechanize.Browser()
r = br.open(start)
html = r.read()
soup = BeautifulSoup(html)

for link in soup.find_all('a'):
    linkText = str(link)
    fileName = str(link.get('href'))
    if filetype in fileName:
        image = urllib.URLopener()
        linkGet = http://www.irrelevantcheetah.com + fileName
        filesave = string.lstrip(fileName, '/')
        image.retrieve(linkGet, filesave)