from bs4 import BeautifulSoup
import requests
import sys
import os

# https://isekailunatic.wordpress.com/tsuki-ga-michibiku-isekai-douchuu/

show_traceback = True

BASE_DIR = os.path.dirname( os.path.realpath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

folder = None

while folder is None:
    print("Onde deseja salvar os arquivos")
    folder_name = input("diretorio:")
    folder_name = os.path.join(DOWNLOADS_DIR, folder_name)

    if os.path.isdir(folder_name):
        usar = input("diretorio existe, usar?<s/N>") or "n"
        usar = usar.lower()
        if usar == "s":
            folder = folder_name
            print(folder)
    else:
        print("diretorio nao existe")
        try:
            os.makedirs(folder_name)
            folder = folder_name
            print(folder)
        except:
            if show_traceback:
                print(sys.exc_info())
            folder = None


htmlpage = None

while htmlpage is None:

    url = input("url:")

    if "http://" not in url and "https://" not in url:
        url = "http://" + url

    print("url:", url)

    try:
        htmlpage = requests.get(url)
        print(htmlpage)
    except requests.exceptions.ConnectionError:
        t, v, traceback = sys.exc_info()
        print("problema conectando com url")
        if show_traceback:
            print(t)
            print(v)
            print(traceback)
    except requests.exceptions.RequestException:
        htmlpage = None
        print(sys.exc_info())



tag = input("tag:?")
print("tag:", tag)

attrib = input("atrribs: attr: value value2 $ attr2: value3 : ")
attrib = attrib.split("$")
attr = {}
for a in attrib:
    r = a.split(":")
    attr[r[0]] = r[1]

# {'class': 'entry-content'}
print(attr)
domcument = BeautifulSoup(htmlpage.text, "html.parser")
tag_element = domcument.find(tag, attr)

links = tag_element.find_all("a")

download_default = "n"
for a in links:
    href = a.get('href')
    print(href)

    if download_default == "n":
        download = input("download <s/N>: ") or download_default
    else:
        download = input("download <S/n>: ") or download_default

    if download == "s":
        download_default = "s"
        name = input("name: ")
        try:
            response = requests.get(href)
            htmlfile = os.path.join(folder, name + ".html", "w")
            htmlfile.write(response.txt)
            htmlfile.close()
        except:
            print(sys.exc_info())
