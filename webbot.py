'''
from bs4 import BeautifulSoup
import mechanize
import time
import urllib
import string
import os


linkList = []
star = "http://" + raw_input ("Where would you like to start searching?\n")    
filetype = raw_input("What file type are you looking for?\n")               #Estamos pidiendo el tipo de documento que queremos, .pdf, .mp4, etc.         
br = mechanize.Browser()                                                    #Creamos un objeto en forma de navegador
r = br.open(star)                                                          #Abrimos la pagina solicitada
html = r.read()                                                             #Lee la pagina solicitada en una unica cadena
print(html)
soup = BeautifulSoup(html, "lxml")

for link in soup.find_all('a'):
    linkText = str(link)
    fileName = str(link.get('href'))
    if filetype in fileName:
        image = urllib.URLopener()
        linkGet = "http://www.irrelevantcheetah.com" + fileName
        filesave = string.lstrip(fileName, '/')
        image.retrieve(linkGet, filesave)
    elif "htm" in fileName:                                                 # This covers both ".htm" and ".html" filenames
        linkList.append(link)
'''
################################################################################################################################

from bs4 import BeautifulSoup
import mechanize
import urllib
import string

star = "http://" + raw_input ("Where would you like to start searching?\n")    
filetype = raw_input("What file type are you looking for?\n")        
br = mechanize.Browser()                                                    #Creamos un objeto en forma de navegador
r = br.open(star)                                                          #Abrimos la pagina solicitada
html = r.read()                                                             #Lee la pagina solicitada en una unica cadena
soup = BeautifulSoup(html, "html5lib")

for link in soup.find_all('a'):
    fileName = str(link.get('href'))
    if filetype in fileName:
        image = urllib.URLopener()
        linkGet = "http://www.irrelevantcheetah.com" + fileName
        filesave = fileName.replace('/', '_')
        print("Downloading " + filesave + "...\n")
        image.retrieve(linkGet,"/home/pi/Dropbox-Uploader/webbot/" +  filesave)











































