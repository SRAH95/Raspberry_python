from bs4 import BeautifulSoup
import mechanize
import time
import urllib
import string

start = "http://" + raw_input ("Where would you like to start searching?\n")    
br = mechanize.Browser()    #Creamos un objeto en forma de navegador
r = br.open(start)          #Abrimos la pagina solicitada
html = r.read()             #Lee la pagina solicitada en una unica cadena

soup = BeautifulSoup(html, "lxml")
for link in soup.find_all('a'):
    print (link.get('href'))

    #jkfals;fjaksfjaksljfs;alkflsj
