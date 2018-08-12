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

################################################################################################################################

'''linkList = []
base = "http://" + raw_input ("Where would you like to start searching?\n")    
filetype = raw_input("What file type are you looking for?\n")               #Estamos pidiendo el tipo de documento que queremos, .pdf, .mp4, etc.         
br = mechanize.Browser()                                                    #Creamos un objeto en forma de navegador
r = br.open(base)                                                           #Abrimos la pagina solicitada
html = r.read()         

def downloadFiles (html, base, filetype, filelist):
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        linkText = str(link.get('href'))
        if filetype in linkText:
            image = urllib.URLopener()
            linkGet = base + linkText
            filesave = string.lstrip(linkText, '/')
            image.retrieve(linkGet, filesave)
        elif "htm" in linkText:                                             # Covers both "html" and "htm"
            linkList.append(link)'''
